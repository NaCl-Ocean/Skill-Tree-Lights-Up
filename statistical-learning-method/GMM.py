import numpy as np


class GaussianModel:
    def __init__(self, dim, mean=None, variance=None, weight=None):
        self.dim = dim
        if mean is None:
            self.mean = np.zeros(self.dim)
        else:
            assert mean.shape[0] == self.dim
            self.mean = mean
        if variance is None:
            self.variance = np.ones(self.dim)
        else:
            assert variance.shape[0] == self.dim
            self.variance = variance
        self.weight = 1 if weight is None else weight
    def forward(self, x):
        output = 1 / (np.sqrt(2 * np.pi) * self.variance)
        output *= np.exp( -np.power(x - self.mean, 2) / ( 2*np.power(self.variance,2) ) )
        return output * self.weight
    
    def update(self, mean, variance, weight):
        self.mean = mean
        self.variance = variance
        self.weight = weight
    
    def print_parameter(self):
        print(f'mean:{self.mean}, variance:{self.variance}, weight:{self.weight}')
            
class GMM:
    def __init__(self, num, dim, dataset, weights=None):
        '''Not implement Termination condition'''
        self.num = num
        self.dim = dim
        self.weights = np.ones(self.num) / self.num if weights is None else weights
        # init is important, but i can't find a good way to solve this problem
        # https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html
        self.base_gaussian_models = [GaussianModel(dim, mean=np.mean(dataset, axis=0)*np.random.rand()*10, \
                                                    variance=np.std(dataset, axis=0)*np.random.rand()*10 , weight=weight) \
                                        for _,weight in zip(range(num),self.weights)]
        self.dataset = dataset
        self.dataset_size = dataset.shape[0]
        
    def fit(self):
        for _ in range(10):
            # cal response factor
            response_factor = np.zeros((self.dataset_size, self.num))
            for i,x in enumerate(self.dataset):
                response_factor[i] = [model.forward(x) for model in self.base_gaussian_models]
                response_factor[i] = response_factor[i] / np.sum(response_factor[i])
            
            # cal new parameter
            for k in range(self.num):
                response_factor_sum = np.sum(response_factor[:,k])
                mean_k = np.sum(response_factor[:,k].reshape(-1, 1) * self.dataset) / response_factor_sum
                variance_k = np.sum(response_factor[:,k].reshape(-1,1) * np.power(self.dataset - self.base_gaussian_models[k].mean,2))  \
                            / response_factor_sum
                weight_k = response_factor_sum / self.dataset_size
                self.base_gaussian_models[k].update(mean_k, np.sqrt(variance_k), weight_k)
    
    def print_parameter(self):
        for model in self.base_gaussian_models:
            model.print_parameter()

    

if __name__ == '__main__':
    dataset = np.array([-67,-48, 6, 8, 14, 16, 23, 24, 28, 29, 41, 49, 56, 60, 75])
    dataset = dataset.reshape((-1, 1))
    gmm = GMM(num = 2, dim=1, dataset=dataset, weights=None)
    gmm.fit()
    gmm.print_parameter()



