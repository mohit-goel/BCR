import numpy as np
from itertools import permutations
import random
class PseudoRandom:
    
    def select_random_indices(self,num_required_elements, total_indices,seed):
        np.random.seed(seed)
        perm = np.random.permutation(total_indices)
        return perm[0:num_required_elements]

    def select_random_elements_of_list(self,l, num_required_elements,seed):
        len_of_list = len(l)            
        sample = []
        random.seed(seed)
        for i in range(num_required_elements):
            index = random.randint(0,len_of_list-1)
            sample.append(l[index])
       
        return sample


if __name__ == "__main__":
        list2 = ['put','get','slice','append']
        
       
        
        
        
        pseudoRandom  = PseudoRandom()
        seed = 89
        lf = pseudoRandom.select_random_elements_of_list(list2,100,seed)
        
        #lf = permutations(lf)
        print(len(lf))
        for i in lf:
            print(i)
        
        print(pseudoRandom.select_random_elements_of_list(list2,3,seed))
        
        

