import numpy as np

class TreeNode:
    def __init__(self, dim, value=None, left=None, right=None, is_leaf=False, label=None):
        self.dim = dim
        self.value = value
        self.left = left
        self.right = right
        self.is_leaf = is_leaf
        self.label = label
        if self.is_leaf:
            assert self.label is not None, "leaf node should have label"
    
    def __call__(self, x):
        if self.is_leaf:
            return self.label
        else:
            if x[self.dim - 1] > self.value:
                return self.left(x)
            else:
                return self.right(x)

class DecisionTree:
    '''
    for regression
    '''
    def __init__(self,dim, train_dataset, labels):
        self.dataset = train_dataset
        self.labels = labels
        self.root = None
        self.dim = dim
        self.construct_tree(train_dataset, labels, self.root)
    
    @staticmethod
    def cal_var(labels):
        return np.var(labels)*labels.shape[0]
    
    def split_dataset(self, dataset, labels, dim, value):
        left_dataset = dataset[dataset[:,dim-1] > value,:]
        left_label = labels[dataset[:, dim-1] > value]
        right_dataset = dataset[dataset[:,dim-1]<=value, :]
        right_label = labels[dataset[:,dim-1] <=value]
        return left_dataset, left_label, right_dataset, right_label
    
    def get_min_var_dimandvalue(self, dataset, labels):
        min_var = np.inf
        min_var_dim = 0
        min_var_value = 0
        for i in range(self.dim):
            for value in np.unique(dataset[:,i]):
                _, left_label,_,right_label = self.split_dataset(dataset,labels,dim=i+1,value=value)
                if left_label.shape[0] <=1:
                    left_var = 0
                else:
                    left_var = self.cal_var(left_label)
                if right_label.shape[0] <= 1:
                    right_var = 0
                else:
                    right_var = self.cal_var(right_label)
                var = left_var + right_var
                if var < min_var:
                    min_var,min_var_dim,min_var_value = var, i+1, value
        return min_var, min_var_dim, min_var_value


    def construct_tree(self, dataset, labels, current_node):
        if np.unique(labels).shape[0] == 1:
            current_node.label = np.mean(labels)
            current_node.left, current_node.right = None, None
            current_node.is_leaf = True
            return
        if dataset.shape[0] <= 3:
            current_node.label = np.mean(labels)
            current_node.left, current_node.right = None, None
            current_node.is_leaf = True
            return
        
        _, split_dim, split_value = self.get_min_var_dimandvalue(dataset, labels)
        if current_node is None:
            current_node = TreeNode(dim=split_dim, value=split_value,)
            current_node.label = np.mean(labels)
            self.root = current_node
        else:
            current_node.dim, current_node.value = split_dim, split_value
            current_node.label = np.mean(labels)
        
        left_dataset, left_labels, right_dataset, right_label = self.split_dataset(dataset,labels,dim=split_dim,value=split_value)
        left_node = TreeNode(dim=None)
        self.construct_tree(left_dataset, left_labels, left_node)
        current_node.left = left_node
        right_node = TreeNode(dim=None)
        self.construct_tree(right_dataset, right_label, right_node)
        current_node.right = right_node
    
    def forward(self, x):
        return self.root(x)
    def valid(self, dataset, labels):
        error = 0
        for x,y in zip(dataset,labels):
            output = self.forward(x)
            error += np.linalg.norm((output-y))
        return error/dataset.shape[0]

    
if __name__ == '__main__': 
    from sklearn.datasets import load_boston 
    import pandas as pd
    dataset = load_boston()
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    train_labels = dataset.target[0:400]
    train_dataset = df.loc[0:399].values
    tree  = DecisionTree(train_dataset.shape[1], train_dataset, train_labels)
    test_dataset = df.loc[400:].values
    test_labels = dataset.target[400:]
    test_error = tree.valid(test_dataset, test_labels)
    print(f'test error:{test_error}')
    train_error = train_error = tree.valid(train_dataset,train_labels )
    print(f'train error:{train_error}')
