import numpy as np

class BaseLearner:
    ''' decision tree stump'''
    def __init__(self, dim=None, value=None, left_label=None, right_label=None):
        self.dim, self.value = dim, value
        self.left_label, self.right_label = left_label, right_label
   
    @staticmethod
    def cal_var(labels):
        if labels.shape[0] == 1:
            return 0
        if np.unique(labels).shape[0] == 1:
            return 0
        return np.var(labels) * labels.shape[0]
    
    def split_dataset(self, dim, value, dataset, labels):
        left_mask = dataset[:,dim-1] <= value
        left_dataset = dataset[left_mask,:]
        left_labels = labels[left_mask]
        
        right_mask = dataset[:,dim-1] > value
        right_dataset = dataset[right_mask, :]
        right_labels = labels[right_mask]
        
        return left_dataset, left_labels, right_dataset, right_labels

    def fit(self, dataset, labels):
        dims = dataset.shape[1]
        min_var = np.inf
        min_var_dim, min_var_value = None,None

        for dim in range(dims):
            for value in np.unique(dataset[:,dim]):
                _, left_labels, _, right_labels = self.split_dataset(dim+1, value, dataset, labels)
                var = self.cal_var(left_labels) + self.cal_var(right_labels)
                if var < min_var:
                    min_var = var
                    min_var_dim, min_var_value = dim+1, value
        _, left_labels, _, right_labels = self.split_dataset(min_var_dim, min_var_value, dataset, labels)
        self.left_label, self.right_label = np.mean(left_labels), np.mean(right_labels)
        self.dim, self.value = min_var_dim, min_var_value
    

    def __call__(self, x):
        if x[self.dim-1] <= self.value:
            return self.left_label
        else:
            return self.right_label

    

class BoostTree:
    def __init__(self, dataset, labels, num_learners):
        assert isinstance(dataset, np.ndarray), "dataset must be numpy.ndarray"
        assert dataset.ndim == 2, "dataset should have 2 dims"
        assert labels.shape[0] == dataset.shape[0], "len(labels) should equal to len(datset)"
        self.dataset = dataset
        self.labels = labels
        self.num_learners = num_learners
        self.dataset_size = dataset.shape[0]
        self.learners = []
    
    def cal_residual(self, learner, dataset, labels):
        residual = np.zeros(self.dataset_size)
        for i,x,y in enumerate(zip(dataset, labels)):
            predict = learner(x)
            residual[i] = y - predict
        return residual

    def fit(self):
        residual = self.labels
        for _ in range(self.num_learners):
            learner = BaseLearner()
            learner.fit(self.dataset, residual)
            residual = self.cal_residual(learner, self.dataset, residual)
            self.learners.append(learner)
    
    def forward(self, x):
        output = np.zeros(self.num_learners)
        for i, learner in enumerate(self.learners):
            output[i] = learner(x)
        
        output_ = np.sum(output)
        return output_

