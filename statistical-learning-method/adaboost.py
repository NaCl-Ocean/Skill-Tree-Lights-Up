import numpy as np

            
class BaseLearner:
    '''decision tree stump'''
    def __init__(self, dim, value, left_label=None, right_label=None,):
        self.left_label = None
        self.right_label = None
        self.dim = dim
        self.value = value
    def split_dataset(self, dim, value, dataset, labels, weights):
        left_mask = dataset[:,dim-1] <= value
        left_dataset = dataset[left_mask,:]
        left_labels = labels[left_mask]
        left_weights = weights[left_mask]
        right_mask = dataset[:,dim-1] > value
        right_dataset = dataset[right_mask, :]
        right_labels = labels[right_mask]
        right_weights = weights[right_mask]
        return left_dataset, left_labels, left_weights, right_dataset, right_labels, right_weights
        
    def fit(self, dataset, labels, weights):
        dims = dataset.shape[1]
        min_error = np.inf
        min_error_dim, min_error_value = None, None
        min_error_left_label, min_error_right_label = None, None
        for dim in range(dims):
            for value in np.unique(dataset[:,dim]):
                _, left_labels, left_weights, _, right_labels, right_weights = self.split_dataset(dim+1, value, dataset, labels, weights)
                error_1 = np.sum(left_weights[left_labels==1]) +  np.sum(right_weights[right_labels==-1])
                error_2 = np.sum(left_weights[left_labels==-1]) + np.sum(right_weights[right_labels==1])
                error = error_1 if error_1<error_2 else error_2
                left_label = 1 if error_1 < error_2 else -1
                right_label = 0 - left_label
                if error < min_error:
                    min_error = error
                    min_error_dim, min_error_value = dim+1, value
                    min_error_left_label, min_error_right_label = left_label, right_label
        self.left_label, self.right_label = min_error_left_label, min_error_right_label
        self.dim, self.value = min_error_dim, min_error_value
        return min_error

    def __call__(self, x):
        if x[self.dim-1] <= self.value:
            return self.right_label
        else:
            return self.left_label


class Adaboost:
    def __init__(self, dataset, labels, num_learners):
        assert isinstance(dataset, np.ndarray), "dataset must be numpy.ndarray"
        assert dataset.ndim == 2, "dataset should have 2 dims"
        assert labels.shape[0] == dataset.shape[0], "len(labels) should equal to len(datset)"
        self.dataset = dataset
        self.labels = labels
        self.num_learners = num_learners
        self.dataset_size = dataset.shape[0]
        self.learners = []
        self.weights = np.zeros(num_learners)
    
    def cal_alpha(self, error):
        return np.log((1-error)/error)/2
    
    def cal_weights(self, weights, alpha, labels, dataset, stump):
        predict = np.zeros(self.dataset_size)
        for i,x in enumerate(dataset):
            predict[i] = stump(x)
        weights_new = weights * np.exp(-alpha * labels * predict)
        z = np.sum(weights * np.exp(-alpha * labels * predict))
        weights_new = weights_new / z
        return weights_new
    
    def fit(self):
        data_weights = np.ones(self.dataset_size) / self.dataset_size
        for i in range(self.num_learners):
            learner = BaseLearner(dim=None, value=None)
            error = learner.fit(self.dataset, self.labels, data_weights)
            alpha = self.cal_alpha(error)
            data_weights = self.cal_weights(data_weights, alpha, self.labels, self.dataset, learner)
            self.learners.append(learner)
            self.weights[i] = alpha
    
    def forward(self, x):
        output = np.zeros(self.num_learners)
        for i in range(self.num_learners):
            output[i] = self.learners[i](x)
        sum_output = np.sum(output * self.weights)
        if sum_output >= 0:
            return 1
        else:
            return -1

    def valid(self):
        error_num = 0
        for x,y in zip(self.dataset,self.labels):
            predict = self.forward(x)
            if predict != y:
                error_num += 1
        return error_num / self.dataset_size
if __name__ == '__main__':
    from sklearn.datasets import load_iris
    import pandas as pd
    train_dataset = np.array([
                            [0,1,3],[0,3,1],[1,2,2],[1,1,3],[1,2,3],[0,1,2],[1,1,2],[1,1,1],[1,3,1],[0,2,1]
                            ])
    train_labels = np.array([-1,-1,-1,-1,-1,-1,1,1,-1,-1])
    adaboost = Adaboost(train_dataset, train_labels, num_learners=10)
    adaboost.fit()
    train_error = adaboost.valid()
    print(f'train error:{train_error}')

    

