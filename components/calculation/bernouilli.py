import random as r


def bernouilli(p=.5):
    if r.random() > p:
        return 0

    return 1


def experience(n, p=.5, target=1):
    count = 0
    for _ in range(n):
        if bernouilli(p) == target:
            count += 1

    return count


def print_bernouilli_result_array(number_range, n, p=.5, target=1):
    return [experience(n, p, target) for _ in range(number_range)]
