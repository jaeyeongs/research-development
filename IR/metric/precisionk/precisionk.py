def top_N_precision(self, predict_list, topk):
    '''[ [ 0, 1, 0, 0, ..., 0 ]
        [ 1, 0, 0, 0, ..., 0 ]
        [ 0, 0, 0, 1, ..., 0 ]
        [ 0, 1, 0, 0, ..., 0 ]
        ]
        '''
    c, m = [0] * topk, 0
    for idx, predict in enumerate(predict_list):
        if 1 in predict:
            c[predict.index(1)] += 1
        m += 1
    top_n_precision = [sum(c[:idx + 1]) / m for idx, e in enumerate(c)]

    return top_n_precision