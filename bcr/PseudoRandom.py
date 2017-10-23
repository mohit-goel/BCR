import random
class PseudoRandom:
    
   
    def select_random_elements_of_list(self,l, num_required_elements,seed):
        len_of_list = len(l)            
        sample = []
        random.seed(seed)
        for i in range(num_required_elements):
            index = random.randint(0,len_of_list-1)
            sample.append(l[index])
       
        return sample