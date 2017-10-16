from OrderStatement import OrderStatement
class OrderProof:
    def __init__(self,listOfOrderSt,slot,operationName,operationId):
        self.listOfOrderSt = listOfOrderSt
        self.slot = slot
        self.operationName = operationName
        self.operationId = operationId
        
    def getlistOfOrderSt(self):
        return self.listOfOrderSt
    
    def addStatement(self,st):
        self.listOfOrderSt.append(st)
    
    def setlistOfOrderSt(self,listOfOrderSt):
        self.listOfOrderSt = listOfOrderSt
        
    def __str__(self):
     return '{ ' + ",".join(str(i) for i in self.listOfOrderSt)  + ",slot: " + str(self.slot) + ",operation:(" + str(self.operationName) + "," + str(self.operationId) + ')}'
        
        
     