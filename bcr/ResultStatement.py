
class ResultStatement:
    
    def __init__(self,result,operationName,operationId):
        self.result = result
        self.operationName = operationName
        self.operationId = operationId
       
        
    def getResult(self):
        return self.result
    
    def __str__(self):
     return '[' + str(self.result) + "," + str(self.operationName) + "," + str(self.operationId) + "]"
        
    
    
        
    