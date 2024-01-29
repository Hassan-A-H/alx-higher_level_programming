#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""

    if len(my_list) == 0:
        return (0)

    mul_score_weight = sum(list(map(lambda x: x[0] * x[1], my_list)))
    sum_weight = sum(list(map(lambda x: x[1], my_list)))
    average = mul_score_weight / sum_weight
    return (average)
