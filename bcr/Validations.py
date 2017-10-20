from State import  State
class Validations:
    
    
    def shouldReplicaAcceptRequest(self,state):
       
        if state.value is not State.ACTIVE.value:
            return False
        
        else:
            return True
            
        
        