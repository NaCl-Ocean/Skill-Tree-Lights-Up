import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import  train_test_split
class SVM:
    def __init__(self,dataset, labels, dim, iter_num=100, C=1,kernel='linear'):
        self.dataset = dataset
        self.labels = labels
        assert np.all(np.equal(np.unique(self.labels),np.array([-1,1]))), "only support binary classify "

        self.C = C
        self.dim = dim
        self.dataset_size = dataset.shape[0]

       
        self.b = np.zeros(1)
        self.alpha = np.zeros((self.dataset_size),dtype=np.float32)
        
        assert kernel in ['linear','poly','gaussian'], 'only support linear, ploy and gaussian kernel'
        if kernel == 'linear':
            self.kernel_func = self.LinearKernel
        elif kernel == 'poly':
            self.kernel_func = self.PolyKernel
        else:
            self.kernel_func = self.GaussainKernel
        
        self.iter_num = iter_num

    

    @staticmethod
    def LinearKernel(x1,  x2):
        return np.dot(x1,x2.T)


    @staticmethod
    def PolyKernel(x1,x2,p=2):
        return np.power(np.dot(x1,x2.T)+1,k)
    
    @staticmethod
    def GaussainKernel(x1,x2,sigma):
        temp = np.linalg.norm(x1-x2,2)
        temp = np.power(temp,2)
        temp = - temp / (2 * sigma^2)
        return np.exp(temp)
    
    def forward(self, x, sign=False):
        output = 0
        for i in range(self.dataset_size):
            output += self.alpha[i] * self.labels[i] * self.kernel_func(self.dataset[i], x)
        output += self.b
        if sign:
            output = 1 if output > 0 else -1
        return output


    
    def cal_gi(self):
        gi = np.zeros(self.dataset_size)
        for i,x in enumerate(self.dataset):
            gi[i] = self.forward(x)
        return gi
    
    def cal_Ei(self):
        Ei = self.cal_gi() -self.labels
        return Ei
    @staticmethod
    def check_kkt(g, labels, alpha, C,index=None):
        if index is not None:
            labels = labels[index]
            alpha = alpha[index]
            g = g[index]
        
        # 0 < alpha < c
        mask1_1 = (alpha < C )& (alpha > 0)
        mask1_2 = (labels * g) == 1
        mask1 = mask1_1 & mask1_2

        # alpha = 0
        mask2_1 = alpha == 0
        mask2_2 = (labels * g) >=1
        mask2 = mask2_1 & mask2_2

        # alpha = C
        mask3_1 = (alpha == C)
        mask3_2 = (labels * g) <= 1
        mask3 = mask3_2 & mask3_1

        mask = mask1 | mask2 | mask3
        return mask





    def train(self):
        
        for i in range(self.iter_num):

            # cal Ei and gi
            gi = self.cal_gi()
            Ei = self.cal_Ei()

            # choose alpha_1
            index = np.array([i for i,alpha_i in enumerate(self.alpha) if 0 < alpha_i < self.C])
            if index.size!= 0:
                satisfy_kkt = self.check_kkt(gi, self.labels, self.alpha, self.C, index)
                not_satisfy_kkt = ~satisfy_kkt
            else:
                satisfy_kkt = np.array([1])
                not_satisfy_kkt = np.array([0])
            if np.any(satisfy_kkt) == True:
                satisfy_kkt = self.check_kkt(gi,self.labels,self.alpha,self.C)
                not_satisfy_kkt = ~satisfy_kkt
                index_not_satisfy_kkt = np.arange(0,self.dataset_size,1)[not_satisfy_kkt]
                alpha1_index = index_not_satisfy_kkt[0]
            else:
                # traverse the entire dataset
                index_not_satisfy_kkt = index[not_satisfy_kkt]
                alpha1_index = index_not_satisfy_kkt[0]
            
            # choose alpha_2
            if Ei[alpha1_index] > 0:
                alpha2_index = np.argmin(Ei)
            else:
                alpha2_index = np.argmax(Ei)
            alpha1_old, alpha2_old = self.alpha[alpha1_index], self.alpha[alpha2_index]
            E_alpha1, E_alpha2 = Ei[alpha1_index], Ei[alpha2_index]
            y_alpha1 , y_alpha2 = self.labels[alpha1_index], self.labels[alpha2_index]
            x_alpha1, x_alpha2 = self.dataset[alpha1_index], self.dataset[alpha2_index]

            if self.labels[alpha1_index] == self.labels[alpha2_index]:
                L = max(0, alpha1_old + alpha2_old - self.C)
                H = min(self.C, alpha1_old + alpha2_old)
            else:
                L = max(0, alpha2_old - alpha1_old)
                H = min(self.C, self.C + alpha2_old - alpha1_old)
            
            # cal alpha_2_new_unc
            eta = self.kernel_func(x_alpha1, x_alpha1) + \
                    self.kernel_func(x_alpha2, x_alpha2) - \
                    2 * self.kernel_func(x_alpha1, x_alpha2)
            alpha_2_new_unc = alpha2_old + y_alpha2 * (E_alpha1 - E_alpha2) / eta

            # cal alpha_2_new
            if alpha_2_new_unc > H:
                alpha_2_new = H
            elif L <= alpha_2_new_unc <= H:
                alpha_2_new = alpha_2_new_unc
            else:
                alpha_2_new = L
            
            # cal alpha_1_new
            alpha_1_new = alpha1_old + y_alpha1 * y_alpha2 * (alpha2_old - alpha_2_new)


            # cal b_new
            b1_new = -E_alpha1 - y_alpha1 * self.kernel_func(x_alpha1,x_alpha1) * (alpha_1_new - alpha1_old) - \
                    y_alpha2 * self.kernel_func(x_alpha1, x_alpha2) * (alpha_2_new - alpha2_old) + self.b
            b2_new = -E_alpha2 - y_alpha1 * self.kernel_func(x_alpha1 ,x_alpha2) * (alpha_1_new - alpha1_old) - \
                    y_alpha2 * self.kernel_func(x_alpha2, x_alpha2) *(alpha_2_new - alpha2_old) + self.b
            

            # update alpha and b
            if 0 < alpha_1_new < self.C and 0 < alpha_2_new < self.C:
                self.b = b1_new
            else:
                self.b = (b1_new + b2_new) /2
            self.alpha[alpha1_index] = alpha_1_new
            self.alpha[alpha2_index] = alpha_2_new

    def valid(self,dataset,labels):
        right_count = 0
        for x,y in zip(dataset,labels):
            predict = self.forward(x,sign=True)
            if predict == y:
                right_count += 1
        acc = right_count / dataset.shape[0]
        return acc


if __name__ == '__main__':
    # prepare data
    iris = load_iris()
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['label'] = iris.target
    data.columns = [
        'sepal length', 'sepal width', 'petal length', 'petal width', 'label'
    ]
    data = np.array(data.iloc[:100, [0,1,-1]])
    data[:,-1] = np.where(data[:,-1]==0, -1, 1)
    train_labels = data[:,-1]
    train_dataset = data[:,0:-1]

    # train
    svm = SVM(train_dataset, train_labels, dim=2)
    svm.train()
    print(svm.forward(np.array([1,1]),sign=True))
    print(f'b:{svm.b}, alpha:{svm.alpha}')
    print(f'acc:{svm.valid(train_dataset, train_labels)}')
