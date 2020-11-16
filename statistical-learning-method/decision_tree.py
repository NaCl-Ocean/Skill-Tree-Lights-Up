import numpy as np


class Treenode:
    '''
    for classify 
    '''
    def __init__(self, dim, funcs, next_nodes=None, label=None, is_leaf=False):
        self.dim = dim
        self.funcs = funcs
        self.next_nodes = next_nodes
        self.label = label
        self.is_leaf = False
        if self.is_leaf:
            assert self.funcs is None and self.next_nodes is None, "this is a leaf node"
        else:
            assert len(self.funcs)== len(self.next_nodes), "the number of funcs should be equal to child nodes"
    
    def __call__(self,x):
        if self.is_leaf:
            return self.label
        for func, node in zip(self.funcs, self.next_nodes):
           if x[self.dim-1] == func:
               return node(x)

class DecisionTree:
    def __init__(self, dataset, dim_to_name, labels, label_to_name, epsilon=0.1, mode='ID3'):
        self.dataset = dataset
        self.dim_to_name = dim_to_name
        self.root = None
        self.labels = np.array(labels)
        self.label_to_name = label_to_name
        self.epsilon = epsilon
        self.full_dims = list(self.dim_to_name.keys())
        assert mode in ['ID3','C4.5'], "only support ID3 and C4.5"
        self.mode = mode
        if np.unique(self.labels).shape[0] == 1:
            # if all instances belong to one class, then the tree has only root node
            self.root = Treenode(dim=0,funcs=None,
                            next_nodes=None,label=np.unique(self.labels)[0])
        assert self.labels.shape[0] >0 , "the number of labels should > 0"
        assert self.labels.shape[0] == self.dataset.shape[0], "the num of labels should be equal to the num of instances"

        if self.mode == 'ID3':
            self.construct_tree_ID3()
        else:
            self.construct_tree_C45()

   
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

   

    def _construct_tree(self,dataset,labels,current_node,current_dims,info_gain_func):
        if np.unique(labels).shape[0] == 1:
            current_node.label = np.unique(labels)[0]
            current_node.funcs, current_node.next_nodes = None, None
            current_node.is_leaf = True
            return
        max_info_gain, max_info_gain_dim = info_gain_func(current_dims, labels,dataset)
        # create root node
        if current_node == None:

            current_node = Treenode(dim=max_info_gain_dim, funcs=[], next_nodes= [], label=None)
            current_node.label = np.unique(labels)[np.argmax(np.bincount(labels))]
            self.root = current_node
        
        # all dim of current node has info gain < epsilon, current node is a leaf node
        if max_info_gain < self.epsilon:
            labels_count = np.bincount(labels)
            labels_ = np.unique(labels)
            current_node.label = labels_[np.argmax(labels_count)]
            current_node.is_leaf = True
            current_node.funcs = None
            current_node.next_nodes = None
            return 
        
        current_node.dim = max_info_gain_dim
        current_node.label = np.unique(labels)[np.argmax(np.bincount(labels))]
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
            current_node.funcs.append(class_i)
            self._construct_tree(next_dataset, next_labels, next_node, next_dims,info_gain_func)
        
    def construct_tree_ID3(self):
        self._construct_tree(self.dataset, self.labels, self.root, self.full_dims,
                            self.get_max_information_gain)
    

    def get_max_info_gain_ratio(self, dims, labels, dataset):
        max_info_gain_ratio = 0
        max_info_gain_ratio_index = None
        for dim in dims:
            current_information_gain = self.cal_infomation_gain(dim,labels,dataset)
            entropy_dim = self.cal_entropy(dataset[:,dim-1])
            current_info_gain_ratio = current_information_gain/entropy_dim
            if current_info_gain_ratio > max_info_gain_ratio:
                max_info_gain_ratio = current_info_gain_ratio
                max_info_gain_ratio_index = dim
        return max_info_gain_ratio, max_info_gain_ratio_index

    def construct_tree_C45(self):
        self._construct_tree(self.dataset,self.labels,self.root,self.full_dims,
                            self.get_max_info_gain_ratio)

        
    def forward(self,x):
        return self.label_to_name[self.root(x)]


class CARTTreeNode:
    def __init__(self, dim, feature,left,right ,label=None,is_leaf=False):
        self.dim = dim
        self.feature = feature
        self.left,self.right = left,right
        self.label = label
        self.is_leaf = is_leaf
        if self.is_leaf:
            assert self.left is None and self.right is None, "this is a leaf node"
        
    
    def __call__(self,x):
        if self.is_leaf:
            return self.label
        if x[self.dim-1] == self.feature:
            return self.left(x)
        else:
            return self.right(x)

class CARTTree(DecisionTree):
    '''
    for classify
    '''
    def __init__(self,dataset, dim_to_name, labels, label_to_name, epsilon=0.1):
        self.dataset = dataset
        self.dim_to_name = dim_to_name
        self.labels = np.array(labels)
        self.label_to_name = label_to_name
        self.epsilon = epsilon
        self.full_dims = list(self.dim_to_name.keys())
        self.root = None
        self.construct_tree(self.dataset, self.labels, self.root, self.full_dims)

    @staticmethod
    def cal_gini_coef(labels):
        labels_ = np.unique(labels)
        if labels_.shape[0] == 1:
            gini_coef = 0
            return gini_coef
        labels_count = np.bincount(labels)
        labels_pro = labels_count[1:]/labels.shape[0]
        gini_coef = 1 - np.sum(np.power(labels_pro,2))
        return gini_coef

    def cal_gini_coef_in_feature(self,dataset,feature,labels):
        dataset_feature_true = dataset[dataset==feature]
        labels_feature_true = labels[dataset==feature]
        gini_feature_true = self.cal_gini_coef(labels_feature_true)
        dataset_feature_false = dataset[dataset!=feature]
        labels_feature_false = labels[dataset!=feature]
        gini_feature_false = self.cal_gini_coef(labels_feature_false)
        gini_coef = (dataset_feature_true.shape[0] / dataset.shape[0]) * gini_feature_true \
                    + (dataset_feature_false.shape[0] / dataset.shape[0]) * gini_feature_false
        return gini_coef
    
    def get_min_gini_coef_in_dim(self,dim,labels,dataset):
        dataset_dim = dataset[:,dim-1]
        dim_class = np.unique(dataset_dim)
        min_gini_coef, mini_gini_coef_class = 1.5,None
        for i,class_i in enumerate(dim_class):
            gini_coef_classi = self.cal_gini_coef_in_feature(dataset_dim,class_i,labels)
            if gini_coef_classi < min_gini_coef:
                min_gini_coef = gini_coef_classi
                mini_gini_coef_class = class_i
        return min_gini_coef, mini_gini_coef_class

    
    def construct_tree(self, dataset, labels, current_node, current_dims):
        if np.unique(labels).shape[0] == 1:
            current_node.label = np.unique(labels)[0]
            current_node.is_leaf = True
            current_node.left, current_node.right = None, None
            return
        
        if len(current_dims) == 0:
            current_node.label = np.unique(labels)[np.argmax(np.bincount(labels))]
            current_node.left, current_node.right = None, None
            current_node.is_leaf = True
            return
        
        min_min_gini_coef,min_min_gini_coef_feature = 1.5,None
        mini_gini_coef_dim = None
        for dim in current_dims:
            min_gini_coef, min_gini_coef_feature = self.get_min_gini_coef_in_dim(dim, labels, dataset)
            if min_gini_coef < min_min_gini_coef:
                min_min_gini_coef = min_gini_coef
                min_min_gini_coef_feature = min_gini_coef_feature
                mini_gini_coef_dim = dim
         # create root node
        if current_node == None:
            current_node = CARTTreeNode(dim=mini_gini_coef_dim, feature=min_gini_coef_feature,
                                        left=None,right=None,label=None)
            self.root = current_node

        current_node.dim = mini_gini_coef_dim
        current_node.label = np.unique(labels)[np.argmax(np.bincount(labels))]

        dim_class = dataset[:,mini_gini_coef_dim-1]
        next_dims = current_dims.copy()
        next_dims.remove(mini_gini_coef_dim)

        # left child node
        left_dataset = dataset[dim_class==min_gini_coef_feature,:]
        left_labels = labels[dim_class==min_gini_coef_feature]
        left_node = CARTTreeNode(dim=None,feature=None,left=None,right=None,label=None)
        current_node.left = left_node
        self.construct_tree(left_dataset, left_labels,left_node, next_dims)

        # right child node
        right_dataset = dataset[dim_class!=min_gini_coef_feature,:]
        right_labels = labels[dim_class!=min_gini_coef_feature]
        right_node = CARTTreeNode(dim=None,feature=None,left=None,right=None,label=None)
        current_node.right = right_node
        self.construct_tree(right_dataset, right_labels, right_node, next_dims)

    def forward(self,x):
        return self.label_to_name[self.root(x)]
        
            
        


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
    #decisiontree = DecisionTree(dataset,dim_to_name,labels,label_to_name)
    decisiontree = CARTTree(dataset,dim_to_name,labels,label_to_name)
    x = np.array([1,1,2,2])
    precdict = decisiontree.forward(x)
    print(precdict)
