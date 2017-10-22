class Operation:
    def __init__(self, operationName,key, value):
        self.operationName = operationName
        self.key = key
        self.value = value
        
    def __str__(self):
        return "{ " + str(self.operationName) + " , " + str(self.key) + " , " + str(self.value) + " , "
    
    def __eq__(self, other):
        return self.operationName == other.operationName  and  self.key == other.key  and  self.value == other.value
        