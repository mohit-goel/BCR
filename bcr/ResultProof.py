
class ResultProof:
    def __init__(self,listOfResultSt,operationName,operationId):
        self.listOfResultSt = listOfResultSt
        self.operationName = operationName
        self.operationId = operationId
        
    def getlistOfResultSt(self):
        return self.listOfResultSt
    
    def addStatement(self,st):
        self.listOfResultSt.append(st)
        
    
    def setlistOfOrderSt(self,listOfResultSt):
        self.listOfResultSt = listOfResultSt
        
    def __str__(self):
     return self.listOfResultSt + "," + str(self.operationName) + "," + str(self.operationId)
        
        
     