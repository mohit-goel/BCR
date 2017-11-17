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
        return 'operationID:' + str(self.operationId) + ' operationName:' + str(self.operationName) + " operation key:" + str(self.key) + ' operation value:' + str(self.value) + " Client ID:" + str(self.client) + + " Logical Clock" + str(self.logicalClock) + + " Client Num" + str(self.clientNumber)