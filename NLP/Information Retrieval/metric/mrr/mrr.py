def mrr_measure(self, predict_list):
    ''''[ [ 0, 1, 0, 0, ..., 0 ]
    [ 1, 0, 0, 0, ..., 0 ]
    [ 0, 0, 0, 1, ..., 0 ]
    [ 0, 1, 0, 0, ..., 0 ]
    ]
    '''
    score = 0
    for predict in predict_list:
        if 1 not in predict:
            continue
        score += 1 / (predict.index(1) + 1)
    return score / len(predict_list)