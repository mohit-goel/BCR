class Operation:
    def __init__(self, operationName,key, value):
        self.operationName = operationName
        self.key = key
        self.value = value
        
    def __str__(self):
        return "{ " + str(self.operationName) + " , " + str(self.key) + " , " + str(self.value) + " }"
    
    def performOperation(self,runningState):
        result = None
        if(self.operationName == 'put'):
            runningState[self.key] = self.value
            result = 'OK'
            
        elif(self.operationName == 'get'):
            result = ""
            if self.key in runningState:
                result = runningState[self.key]
            
        elif(self.operationName == 'append'):
            result = 'fail'
            if self.key in runningState:
                result = 'OK'
                runningState[self.key] = runningState[self.key] + self.value
            
        elif(self.operationName == 'slice'):
            result = 'fail'
            if self.key in runningState:
                rangeArr = re.split(":",self.value)
                x = int(rangeArr[0])
                range = int(rangeArr[1])
                klength = len(runningState[self.key])
                if (x>=0 and x<=range and x < klength) and (range>=0 and range <= klength):
                    runningState[self.key] = runningState[self.key][x:range]
                    result = 'OK'
        
        return result
    
    def __eq__(self, other):
        return self.operationName == other.operationName  and  self.key == other.key  and  self.value == other.value
        