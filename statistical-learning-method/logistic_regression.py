import numpy as np
import sklearn

class LogisticRegressionModel:
    def __init__(self, dim, bias=True, lr=1,stop_iter_thresh=1e-4):
        assert bias == True, 'Not supported with no bias'
        self.w = np.ones((dim+1),dtype=np.float32)
        self.dim = dim
        self.stop_iter_thresh = stop_iter_thresh
        self.lr = lr

    @staticmethod
    def sigmoid(x):
        return np.exp(x)/(1+np.exp(x))

    def train(self,dataset,labels,iter_num=1000):
        self.dataset = dataset.astype(np.float32)
        self.labels = labels
        dataset_size = self.dataset.shape[0]
        self.dataset = np.hstack((self.dataset,np.ones((dataset_size,1))))
        for i in range(iter_num):
            z = np.dot(self.dataset,self.w.T)
            predict = self.sigmoid(z)
            grad = self.dataset*(self.labels-predict).reshape(self.labels.shape[0],-1)
            grad = grad.sum(axis=0)
            self.w = self.w+ self.lr * grad
            if (i+1)%5 == 0:
                predict[predict>=0.5] = 1
                predict[predict<=0.5] = 0
                acc = (predict==labels).sum()/dataset_size
                print(f'acc:{acc}')
               
            
              
    
    def valid(self):
        predict = self.forward(self.dataset)
        acc = (predict==self.labels).sum()/self.dataset.shape[0]
        return acc

    def forward(self, x):
        
        x_ = x.reshape((-1,self.dim))
        x_ = np.hstack((x_,np.ones((x_.shape[0],1))))
        y = np.dot(x_,self.w.T)
        pro = (np.exp(y)/(1+np.exp(y))).reshape(-1)
        pro[pro>=0.5] = 1
        pro[pro<=0.5] = 0
        return pro

        
if __name__ =='__main__':
    model = LogisticRegressionModel(dim=3,lr=1e-1)
    dataset = np.array([
                [3,3,3],
                [4,3,2],
                [2,1,2],
                [1,1,1],
                [-1,0,1],
                [2,-2,1],
    ])
    labels = np.array([1,1,1,0,0,0])
    model.train(dataset,labels,iter_num=1000)
    print(model.forward(np.array([1,2,-2])))