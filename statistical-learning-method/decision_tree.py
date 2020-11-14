import numpy as np


class Treenode:
    def __init__(self, dim, funcs, next_nodes=None, label=None):
        self.dim = dim
        self.funcs = funcs
        self.next_nodes = next_nodes
        self.label = label
        if self.label is not None:
            assert self.funcs is None and self.next_nodes is None, "this is a leaf node"
        else:
            assert len(self.funcs)== len(self.next_nodes), "the number of funcs should be equal to child nodes"
    
    def __call__(self,x):
        if self.label is not None:
            return self.label
        for func, node in zip(self.funcs, self.next_nodes):
           if func(x[self.dim]):
               return node

class DecisionTree:
    def __init__(self, dataset, dim_to_name, labels, label_to_name, epsilon=0.1):
        self.dataset = dataset
        self.dim_to_name = dim_to_name
        self.root = None
        self.labels = np.array(labels)
        self.label_to_name = label_to_name
        self.epsilon = epsilon
        self.full_dims = list(self.dim_to_name.keys())
        if np.unique(self.labels).shape[0] == 1:
            # if all instances belong to one class, then the tree has only root node
            self.root = Treenode(dim=0,funcs=None,
                            next_nodes=None,label=np.unique(self.labels)[0])
        assert self.labels.shape[0] >0 , "the number of labels should > 0"
        assert self.labels.shape[0] == self.dataset.shape[0], "the num of labels should be equal to the num of instances"

        self.construct_tree(self.dataset, self.labels, self.root, self.full_dims)
    
   
    @staticmethod
    def cal_entropy(labels):
        labels_ = np.unique(labels)
        if labels_.shape[0] ==1:
            return 0
        labels_count = np.bincount(labels)
        lables_pro = labels_count[1:]/labels.shape[0]
        entropy = (-lables_pro*np.log2(lables_pro)).sum()
        return entropy
    
    
    def cal_infomation_gain(self, dim, labels, dataset):
        origin_entropy = self.cal_entropy(labels)
        dataset_dim = dataset[:,dim-1]
        dim_class = np.unique(dataset_dim)
        dim_class_count = np.bincount(dataset_dim)
        condition_entropy = 0
        for i,class_i in enumerate(dim_class):
            class_i_pro = dim_class_count[i+1]/dataset_dim.shape[0]
            labels_class_i = labels[dataset_dim==class_i]
            class_i_entropy = self.cal_entropy(labels_class_i)
            condition_entropy = condition_entropy + class_i_entropy * class_i_pro
        infomation_gain = origin_entropy - condition_entropy
        return infomation_gain

            
    def get_max_information_gain(self,dims,labels,dataset):
        max_information_gain = 0
        max_information_gain_dim = None
        for dim in dims:
            current_information_gain = self.cal_infomation_gain(dim,labels,dataset)
            if current_information_gain > max_information_gain:
                max_information_gain = current_information_gain
                max_information_gain_dim = dim
        return max_information_gain, max_information_gain_dim

    def construct_tree(self, dataset, labels, current_node, current_dims,):
        # when current dataset has only one class, current node is a leaf node
        if np.unique(labels).shape[0] == 1:
            current_node.label = np.unique(labels)[0]
            current_node.funcs, current_node.next_nodes = None, None
            return
        max_info_gain, max_info_gain_dim = self.get_max_information_gain(current_dims, labels,dataset)
        # create root node
        if current_node == None:
            current_node = Treenode(dim=max_info_gain_dim, funcs=[], next_nodes= [], label=None)
        
        # all dim of current node has < epsilon info gain, current node is a leaf node
        if max_info_gain < self.epsilon:
            labels_count = np.bincount(labels)
            labels_ = np.unique(labels)
            current_node.label = labels_[np.argmax(labels_count)]
            current_node.funcs = None
            current_node.next_nodes = None
            return 
        
        current_node.dim = max_info_gain_dim
        dim_class = dataset[:,max_info_gain_dim-1]
        dim_class = np.unique(dim_class)
        next_dims = self.full_dims.copy()
        next_dims.remove(max_info_gain_dim)
        for i, class_i in enumerate(dim_class):
            next_dataset = dataset[dataset[:,max_info_gain_dim-1] == class_i,:]
            next_labels = labels[dataset[:,max_info_gain_dim-1] == class_i]
            if next_dataset.shape[0] == 0:
                continue
            next_node = Treenode(dim=None, funcs=[],next_nodes=[], label=None)
            current_node.next_nodes.append(next_node)
            current_node.funcs.append(lambda x: x==class_i)
            self.construct_tree(next_dataset, next_labels, next_node, next_dims)
        



if __name__ == '__main__':
    dataset = np.array([
                        [1,1,1,1],
                        [1,1,1,2],
                        [1,2,1,2],
                        [1,2,2,1],
                        [1,1,1,1],
                        [2,1,1,1],
                        [2,1,1,2],
                        [2,2,2,2],
                        [2,1,2,3],
                        [2,1,2,3],
                        [3,1,2,3],
                        [3,1,2,2],
                        [3,2,1,2],
                        [3,2,1,3],
                        [3,1,1,1]
                        ])
    dim_to_name = {1:'age',2:'work',3:'house',4:'credit'}
    labels = [1,1,2,2,1,1,1,2,2,2,2,2,2,2,1]
    label_to_name = {1:'no',2:'yes'}
    decisiontree = DecisionTree(dataset,dim_to_name,labels,label_to_name)
