import numpy as np


class Metrics:
    def __init__(self, y_true: np.ndarray, y_pred: np.ndarray):
        (
            self.true_positives,
            self.false_positives,
            self.false_negatives,
            self.true_negatives,
        ) = Metrics.get_confusion_matrix(y_true, y_pred).flatten()

    def get_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        if len(y_true) != len(y_pred):
            raise Exception("Size of y_true and y_pred doesn't match")

        confusion_matrix = np.zeros([2, 2])
        for i in range(y_true):
            c_yt = y_true[i]
            c_yp = y_pred[i]
            if c_yt == c_yp:
                if c_yt:
                    confusion_matrix[0][0] += 1
                else:
                    confusion_matrix[1][1] += 1
            else:
                if c_yt:
                    confusion_matrix[0][1] += 1
                else:
                    confusion_matrix[1][0] += 1
            return confusion_matrix
