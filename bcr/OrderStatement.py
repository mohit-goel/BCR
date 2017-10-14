
class OrderStatement:
    
    def __init__(self,slot,operationName,operationId):
        self.slot = slot
        self.operationName = operationName
        self.operationId = operationId
       
        
    def getSlot(self):
        return self.slot
    
    def __str__(self):
     return str(self.slot) + "," + str(self.operationName) + "," + str(self.operationId)
        
    
    
        
    
    