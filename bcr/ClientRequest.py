class ClientRequest:
    
    def __init__(self,operationName, key, value, client, operationId, logicalClock , clientNumber):
        self.operationName =  operationName
        self.key = key
        self.value =  value
        self.client = client
        self.operationId = operationId
        self.logicalClock = logicalClock
        self.clientNumber = clientNumber
    
    def __str__(self):
        return '[operation : ' + ' ID:' + str(self.operationId) + ' Name:' + str(self.operationName) + ' Key:' + str(self.key) + ' Value:' + str(self.value) + ' Client ID: ' + str(self.client) + ' Logical Clock' + str(self.logicalClock)  + ' ClientNum ' + str(self.clientNumber) + ']'