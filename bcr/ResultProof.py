
class ResultProof:
    def __init__(self,listOfResultSt,operationName,operationId):
        self.listOfResultSt = listOfResultSt
        self.operationName = operationName
        self.operationId = operationId
        
    def getlistOfResultSt(self):
        return self.listOfResultSt
    
    def setlistOfOrderSt(self,listOfResultSt):
        self.listOfResultSt = listOfResultSt
        
    def __str__(self):
     return listOfResultSt + "," + str(operationName) + "," + str(operationId)
        
        
     