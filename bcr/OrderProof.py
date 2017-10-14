from OrderStatement import OrderStatement
class OrderProof:
    def __init__(self,listOfOrderSt,slot,operationName,operationId):
        self.listOfOrderSt = listOfOrderSt
        self.slot = slot
        self.operationName = operationName
        self.operationId = operationId
        
    def getlistOfOrderSt(self):
        return self.listOfOrderSt
    
    def setlistOfOrderSt(self,listOfOrderSt):
        self.listOfOrderSt = listOfOrderSt
        
    def __str__(self):
     return listOfOrderSt + "," + str(slot) + "," + str(operationName) + "," + str(operationId)
        
        
     