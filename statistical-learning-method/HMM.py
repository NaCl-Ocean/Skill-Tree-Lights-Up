import numpy as np

class MarkovChain:
    def __init__(self,hidden_state_num, observation_state_num):
        self.hidden_state_num = hidden_state_num
        self.observation_state_num = observation_state_num
    
    def ProbabilityCal(self, mode,init_pro, transition_pro, observation_pro, observation_sequence,observation_name):
        assert mode in ['forward','backward'], "only support forward algorithm and backward algorithm"
        assert transition_pro.shape == (self.hidden_state_num,self.hidden_state_num), \
                            'transition probability shape should be hidden_state_num*hidden_state_num'
        assert observation_pro.shape ==  (self.observation_state_num, self.hidden_state_num), \
            'observation probability shape should be observation_state_num*hidden_state_num'
        assert init_pro.shape == (self.hidden_state_num,),\
            'inital probability shape should be hidden_state_num'
        if mode == 'forward':
            return self._forward_cal_probability(init_pro, transition_pro, observation_pro, observation_sequence, observation_name)
        else:
            return self._backward_cal_probability(init_pro, transition_pro, observation_pro, observation_sequence, observation_name)
    
    def _forward_cal_probability(self, init_pro, transition_pro, observation_pro, observation_sequence, observation_name):
        len_sequence = len(observation_sequence)
        alpha = np.zeros((len_sequence,self.hidden_state_num))
        index = observation_name.index(observation_sequence[0])
        alpha[0] = init_pro * observation_pro[index,:]
        for t in range(1, len_sequence):
            observation_index = observation_name.index(observation_sequence[t])
            alpha[t] = [np.sum(alpha[t-1]* transition_pro[:,i])*observation_pro[observation_index, i] for i in range(self.hidden_state_num) ]
        output = np.sum(alpha[-1,:])
        return output, alpha
    
    def _backward_cal_probability(self, init_pro, transition_pro, observation_pro, observation_sequence, observation_name):
        len_sequence = len(observation_sequence)
        beta = np.zeros((len_sequence, self.hidden_state_num))
        beta[-1,:] = 1
        for t in range(len_sequence-2, -1, -1):
            index = observation_name.index(observation_sequence[t+1])
            beta[t] = [np.sum(transition_pro[i,:]*observation_pro[index,:]*beta[t+1]) for i in range(self.hidden_state_num)]
        index = observation_name.index(observation_sequence[0])
        output = np.sum(beta[0] * observation_pro[index] * init_pro)
        return output, beta
    
    @staticmethod
    def cal_gamma(alpha, beta, hidden_state_index, t):
        temp = alpha[t,hidden_state_index] * beta[t, hidden_state_index]
        return temp / np.sum(alpha[t,:]*beta[t,:])

    def LearnParam(self, mode, observation_sequences, observation_name, **kwargs):
        assert mode in ['supervised', 'unsupervised']
        if mode == 'supervised':
            assert 'hidden_name' in kwargs,'need hidden state name'
            assert 'hidden_sequence' in kwargs, 'need hidden state sequence'
            self._learn_param_supervised(observation_sequence, observation_name, kwargs['hidden_sequence'], kwargs['hidden_name'])
        else:
            self._learn_param_unsupervised(observation_sequence, observation_name)
    
    def _learn_param_supervised(self, observation_sequences, observation_name, hidden_sequences, hidden_name):
        # cal transition_pro
        transition_pro = np.zeros(self.hidden_state_num, self.hidden_state_num)
        for i, name_i in enumerate(hidden_name):
            for j,name_j in enumerate(hidden_name):
                transition_pro[i,j] = np.sum(np.diff(hidden_sequences,axis=-1)==0)
            transition_pro[i] = transition_pro[i]/np.sum(transition_pro[i])

        observation_pro = np.zeros((self.observation_state_num, self.hidden_state_num))
        # cal observation_pro
        for j,name_j in enumerate(hidden_name):
            for k,name_k in enumerate(observation_name):
                observation_pro[k,j] = np.sum(hidden_sequences==name_j & observation_sequences==name_k)
            observation_pro[:,j] = observation_pro[:,j] / np.sum(observation_pro[:,j])

        # cal init_pro
        init_pro = [np.sum(hidden_sequences[:,0]==state) for state in hidden_name]
        init_pro = init_pro / np.sum(init_pro)
        return transition_pro, observation_pro, init_pro
    

    def _learn_param_unsupervised(self,observation_sequences,observation_name):
        # ToDo

    def Predict(self, mode, init_pro, transition_pro, observation_pro, observation_sequence, observation_name, hidden_name):
        assert mode in ['approximate', 'viterbi']
        if mode == 'approximate':
            return self._approximate(init_pro, transition_pro, observation_pro, observation_sequence, observation_name, hidden_name)
        else:
            return self._viterbi(init_pro, transition_pro, observation_pro, observation_sequence, observation_name, hidden_name)
    
    def _approximate(self, init_pro, transition_pro, observation_pro, observation_sequence, observation_name, hidden_name):
        _, alpha = self._forward_cal_probability(init_pro, transition_pro, observation_pro, observation_sequence, observation_name)
        _, beta = self._backward_cal_probability(init_pro, transition_pro, observation_pro, observation_sequence, observation_name)
        sequence_len = len(observation_sequence)
        hidden_state_sequence = []
        for t in range(sequence_len):
            gamma_t = [self.cal_gamma(alpha, beta, i, t) for i in range(self.hidden_state_num)]
            max_gamma_state_index = np.argmax(gamma_t)
            hidden_state_sequence.append(hidden_name[max_gamma_state_index])
        return hidden_state_sequence
    
    def _viterbi(self, init_pro, transition_pro, observation_pro, observation_sequence, observation_name, hidden_name):
        sequence_len = len(observation_sequence)
        delta = np.zeros((sequence_len, self.hidden_state_num))
        psi = np.zeros((sequence_len, self.hidden_state_num))
        index = observation_name.index(observation_sequence[0])
        delta[0] = init_pro * observation_pro[index]
        psi[0] = 0
        for t in range(1, sequence_len):
            index = observation_name.index(observation_sequence[t])
            delta[t] = [np.max(delta[t-1]* transition_pro[:,i])*observation_pro[index,i] for i in range(self.hidden_state_num)]
            psi[t] = [np.argmax(delta[t-1]* transition_pro[:,i]) for i in range(self.hidden_state_num)]
        max_pro = np.max(delta[-1])
        max_pro_node = []
        hidden_state_index = np.argmax(delta[-1])
        max_pro_node.append(hidden_state_index)
        for t in range(sequence_len-1, 0, -1):
            hidden_state_index = int(psi[t,hidden_state_index])
            max_pro_node.append(hidden_state_index)
        max_pro_node = [max_pro_node[i] for i in range(len(max_pro_node)-1, -1, -1)]
        return max_pro_node, max_pro
            







if __name__ =='__main__':
    transition_pro = np.array([
                            [0.5,0.2,0.3],
                            [0.3,0.5,0.2],
                            [0.2,0.3,0.5]])
    observation_pro = np.array([
                        [0.5,0.4,0.7],
                        [0.5,0.6,0.3]])
    init_pro = np.array([0.2,0.4,0.4])
    observation_name = ['红','白']
    observation_sequence = ['红','白','红','白']
    markovchain= MarkovChain(3,2)
    # pro = markovchain.ProbabilityCal('backward', init_pro,transition_pro,observation_pro,observation_sequence, observation_name)
    # print(pro)
    node_path,_ = markovchain.Predict('viterbi', init_pro, transition_pro, observation_pro, observation_sequence, observation_name,None)
    print(node_path)

