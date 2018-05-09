import numpy as np


def precision_at_k(y_pred, y, k=1):
    tp = .0
    for i in range(k):
        tp += (y_pred[i] in set(y))

    return tp / k


def average_precision(y_pred, y, k=1):
    precisions = list()
    tp = .0
    for i in range(len(y_pred)):
        if (y_pred[i] in set(y)):
            tp += 1
            precisions.append(tp / (i + 1))

    return np.mean(np.array(precisions))


def main():
    a_pred = [1, 0, 3, 0, 0, 6, 0, 0, 9, 10]
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    b_pred = [0, 2, 0, 0, 5, 0, 7, 0, 0, 0]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(average_precision(a_pred, a))
    print(average_precision(b_pred, b))


if __name__ == '__main__':
    main()