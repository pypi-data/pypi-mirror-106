import numpy as np
import pandas as pd


def precision(predictions, label_ids, id2tkn, id2type, token_types={'cui'}, prediction_scope='one', shifted_labels=False,
        predictions_are_scores=True, old_data=None, topk=1, start=0):
    r''' Calculate precision for next concept prediction.

    Args:
        predictions:
            Expected shape <batch_size> x <sequence_length> x <vocabulary_size>
        label_ids:
            Expected shape <batch_size> x <sequence_length>
        id2tkn:
            Map from ID to tokens
        id2type:
            Map from ID to token type (e.g. `age`, `cui`, ...)
        token_types (Set[str], optional, defaults to `{'cui'}`:
            On what token types to calculate the Precision. Leave empoty to include all token types.
        prediction_scope:
            How much into the future should we look to accept something as correct:
                - `one` has to be the next concept
                - `age` until the next age token
                - `any` whenever
        shifted_labels:
            Are labels == input_ids, or shifted by one to the left
        predictions_are_scores:
            Are predictions scores for each label_id or really label_ids already
        old_data:
            If set it will load old values for tp/fp/positives/negatives and continue ontop of those
        topk:
            How many predicted labels to consider when calculating precision
        start:
            At what point to start - we will look only at the precision of concepts at positions after start

    Return (Dict[str, ]):
        precision:
            Precision
        tp:
            Number of True positives
        fp:
            Number of False positives
        positives:
            For each label ID a count of positive examples
        negatives
            For each label ID a count of negative examples
    '''
    if predictions_are_scores:
        outputs = np.argsort(-1 * predictions, axis=2)
    else:
        outputs = predictions

    tp = 0
    fp = 0
    positives = {}
    negatives = {}
    # If not shifted_labels label = prediction - 1
    label_position_shift = 0 if shifted_labels else 1
    # If labels are not shifted move the start by one
    start += 0 if shifted_labels else 1

    if old_data:
        tp = old_data['tp']
        fp = old_data['fp']
        positives = old_data['positives']
        negatives = old_data['negatives']

    def prediction_end_index(i, lbl):
        r''' Used below to get the end index for different
        prediction scopes
        '''
        if prediction_scope == 'one':
            return i + 1
        elif prediction_scope == 'any':
            return len(lbl)
        elif prediction_scope == 'age':
            end = len(lbl)
            for j in range(i, len(lbl)):
                if id2type.get(lbl[j], 'unk') == 'age':
                    end = j
                    break
            return end

    for ind, lbl in enumerate(label_ids):
        if start < len(lbl):
            for i in range(start, len(lbl)):
                tkn = str(id2tkn.get(lbl[i], lbl[i]))
                if not token_types or id2type.get(lbl[i], 'unk') in token_types:
                    end = prediction_end_index(i, lbl)

                    # If predictions are scores we can do topk, if not just do simple label match
                    if (predictions_are_scores and any([out in lbl[i:end] for out in outputs[ind][i-label_position_shift][0:topk]])) or \
                        (not predictions_are_scores and outputs[ind][i-label_position_shift] in lbl[i:end]):
                        tp += 1
                        positives[tkn] = positives.get(tkn, 0) + 1
                    else:
                        fp += 1
                        negatives[tkn] = negatives.get(tkn, 0) + 1

    prec = tp / (tp + fp)

    return {'precision': prec, 'tp': tp, 'fp': fp, 'positives': positives, 'negatives': negatives}


def sort_precision_output(precision_output, cdb, main='positives'):
    d = precision_output
    if main == 'positives':
        other = 'negatives'
    else:
        other = 'positives'

    out = sorted([(
        "{:.2f}".format(tp / (tp + d[other].get(cui, 1))), 
        cdb.get_name(cui),
        tp,
        d[other].get(cui, 0),
        cui) for cui, tp in sorted(d[main].items(), key=lambda x: x[1], reverse=True)],
        key=lambda x: x[0], reverse=True)

    out = pd.DataFrame(out, columns=['precision', 'name', main, other, 'cui'])

    return out


class ComputePrecisionHF(object):
    r''' Used for computing precison when working with HF trainer
    '''

    def __init__(self, id2tkn, id2type, batch_size=1000, **kwargs):
        self.id2tkn = id2tkn
        self.id2type = id2type
        self.batch_size = batch_size
        self.kwargs = kwargs

    def __call__(self, p):
        # We will do this in batches, because it can be very memory demanding
        metrics_data = None
        start = 0
        while start < len(p.predictions):
            predictions = np.argmax(p.predictions[start:start+self.batch_size], axis=2) # For speed do not send predictions as scores
            label_ids = p.label_ids[start:start+self.batch_size]
            metrics_data = precision(predictions, label_ids=label_ids, id2tkn=self.id2tkn, id2type=self.id2type, old_data=metrics_data,
                                     predictions_are_scores=False, **self.kwargs)
            start += self.batch_size

        return {
            'precision': metrics_data['precision'],
        }
