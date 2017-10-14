class Shuttle:
    
    def __init__(self,resultProof,orderProof):
        self.resultProof = resultProof
        self.orderProof = orderProof
        
    def getResultProof(self):
        return self.resultProof
    
    def getOrderProof(self):
        return self.orderProof
    
    def addOrderStatement(self,orderStatement):
        self.orderProof.addStatement(orderStatement)        
        
        
    def addResultStatement(self,resultStatement):
        self.resultProof.addStatement(resultStatement)
        
    def __str__(self):
     return str(self.resultProof) + "," + str(self.orderProof)
        
        
        