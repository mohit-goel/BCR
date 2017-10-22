import numpy as np
from itertools import permutations
class PseudoRandom:
    
    def select_random_indices(self,num_required_elements, total_indices,seed):
        np.random.seed(seed)
        perm = np.random.permutation(total_indices)
        return perm[0:num_required_elements]

    def select_random_elements_of_list(self,l, num_required_elements,seed):
        len_of_list = len(l)
        while(num_required_elements>len_of_list):
            l = l + l
            len_of_list = len_of_list +2
        
        indices = self.select_random_indices(num_required_elements, len_of_list,seed)
        sample = [l[i] for i in indices]
        return sample
   
if __name__ == "__main__":
        list2 = ['put','get','put','append']
        
       
        
        
        
        pseudoRandom  = PseudoRandom()
        seed = 89
        lf = pseudoRandom.select_random_elements_of_list(list2,50,seed)
        
        lf = permutations(lf)
        
        for i in lf:
            print(i)
        
        print(pseudoRandom.select_random_elements_of_list(list2,3,seed))
        
        

