import numpy as np


class NaiveBayes:
    def __init__(self, labels, x_vectors, mode='MLE'):
        self.labels = labels.reshape((-1))
        self.vectors = x_vectors
        assert mode in ['MLE', 'Bayes']
        self.mode = mode
    
    def MLE(self,x):
        class_ = np.unique(self.labels)
        class_count = np.bincount(self.labels)
        class_distri = class_count[1:] / self.labels.shape[0]
        p_list = []
        for j,c in enumerate(class_):
            p = 1
            vector_yj = self.labels==c
            size_yj = vector_yj.sum()
            for i,x_i in enumerate(x):
                vector_xi = self.vectors[:,i]==x_i
                size_yj_xi = (vector_yj & vector_xi).sum()
                p = size_yj_xi/size_yj * p
            p = class_distri[j] * p
            p_list.append(p)
        max_index = np.argmax(p_list)
        return class_[max_index]
    
    def Bayes(self, x, lambda_=1):
        class_ = np.unique(self.labels)
        class_count = np.bincount(self.labels)
        class_distri = (class_count[1:] + lambda_)/ \
                            (self.labels.shape[0] + class_.shape[0]*lambda_)
        p_list = []
        for j,c in enumerate(class_):
            p = 1
            vector_yj = self.labels==c
            size_yj = vector_yj.sum()
            for i,x_i in enumerate(x):
                class_num_xi = np.unique(self.vectors[:,i]).shape[0]
                vector_xi = self.vectors[:,i]==x_i
                size_yj_xi = (vector_yj & vector_xi).sum()
                p = (size_yj_xi + lambda_)/ (size_yj + class_num_xi*lambda_)* p
            p = class_distri[j] * p
            p_list.append(p)
        max_index = np.argmax(p_list)
        return class_[max_index]

    def __call__(self,x,**kwargs):
        if self.mode == 'MLE':
            return self.MLE(x)
        else:
            lambda_ = kwargs.setdefault('lambda_',1)
            return self.Bayes(x,kwargs['lambda_'])

if __name__ == '__main__':
    labels = np.array([1,1,2,2,1,1,1,2,2,2,2,2,2,2,1]) 
    vectors = np.array([
                        [1,1],[1,2],[1,2],[1,1],[1,1],
                        [2,1],[2,2],[2,2],[2,3],[2,3],
                        [3,3],[3,2],[3,2],[3,3],[3,3]])
    nb = NaiveBayes(labels=labels, x_vectors=vectors, mode='Bayes')
    c = nb(np.array([2,1]))
    print(c)
                
                

        
