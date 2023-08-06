import numpy as np


class SEFRClassifier:
    def __init__(self):
        self.weights = []
        self.bias = 0

    def fit(self, train_predictors, train_target):
        """
        This is used for training the classifier on data.
        Parameters
        ----------
        train_predictors : float, either list or numpy array
            are the main data in DataFrame
        train_target : integer, numpy array
            labels, should consist of 0s and 1s
        """
        X = train_predictors
        X = np.array(train_predictors, dtype="float32")

        self.y = train_target
        self.y = np.array(train_target, dtype="int32")

        # pos_labels are those records where the label is positive
        # neg_labels are those records where the label is negative
        pos_labels = np.sign(self.y) == 1
        neg_labels = np.invert(pos_labels)

        # pos_indices are the data where the labels are positive
        # neg_indices are the data where the labels are negative
        pos_indices = X[pos_labels, :]
        neg_indices = X[neg_labels, :]

        # avg_pos is the average value of each feature where the label is positive
        # avg_neg is the average value of each feature where the label is negative
        avg_pos = np.mean(pos_indices, axis=0)  # Eq. 3
        avg_neg = np.mean(neg_indices, axis=0)  # Eq. 4

        # weights are calculated based on Eq. 3 and Eq. 4

        self.weights = (avg_pos - avg_neg) / (avg_pos + avg_neg + 0.0000001)  # Eq. 5


        # For each record, a score is calculated. If the record is positive/negative, the score will be added to posscore/negscore
        sum_scores = np.dot(X, self.weights)  # Eq. 6

        pos_label_count = np.count_nonzero(self.y)
        neg_label_count = self.y.shape[0] - pos_label_count

        # pos_score_avg and neg_score_avg are average values of records scores for positive and negative classes
        pos_score_avg = np.mean(sum_scores[self.y == 1])  # Eq. 7
        neg_score_avg = np.mean(sum_scores[self.y == 0])  # Eq. 8

        # bias is calculated using a weighted average

        self.bias = (neg_label_count * pos_score_avg + pos_label_count * neg_score_avg) / (neg_label_count + pos_label_count)  # Eq. 9

    def predict(self, test_predictors):
        """
        This is for prediction. When the model is trained, it can be applied on the test data.
        Parameters
        ----------
        test_predictors: either list or ndarray, two dimensional
            the data without labels in
        Returns
        ----------
        predictions in numpy array
        """
        X = test_predictors
        if isinstance(test_predictors, list):
            X = np.array(test_predictors, dtype="float32")

        temp = np.dot(X, self.weights)
        self.preds = np.where(temp <= self.bias, 0 , 1)
        return self.preds

    # Calculate accuracy percentage between two lists
    def score(self,y, preds):
        correct = 0
        for i in range(len(y)):
            if y.array[i] == preds[i]:
                correct += 1
        return correct / float(len(y)) * 100.0

    def get_params(self,deep=False):
        return { }
