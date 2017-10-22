from State import  State
from Crypto import Crypto
class Validations:
    

    def __init__(self):
        self.crypto = Crypto()
        
        
    def shouldReplicaAcceptRequest(self,state):

        if state.value is not State.ACTIVE.value:
            return False
        else:
            return True
        
    def validationOfResultProof(self,result,resultProof,replicaPublicList):
        if len(resultProof.getlistOfResultSt()) < (len(replicaPublicList)) :
            print("Result Proof validation fail: Result Statement of some replica missing")
            return False
        
        resultStList = resultProof.getlistOfResultSt()
        for i in range(len(resultStList)):
            currentEncodedSt = resultStList[i];
            currentKey = replicaPublicList[i];
            decodeSt = self.crypto.isSignatureVerified(currentKey,currentEncodedSt)
            if (decodeSt is None):
                print("Result proof validation fail: Signature not verified")
                return False
                
            if(not self.crypto.verifyHashes(result, decodeSt.result)):
                print("Result proof validation fail: Result doesn't match Result Stmt of some replica")
                return False
       
        return True
    
    def responseReceivedWithCorrectOperation(self,operationName,operationId,receivedOperationName,receivedOperationId):
        return (operationName == receivedOperationName) and (operationId == receivedOperationId)
    
        
            
        
        