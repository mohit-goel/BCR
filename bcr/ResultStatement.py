
class ResultStatement:

    def __init__(self, result, operationName, operationId, replicaId):
        self.result = result
        self.operationName = operationName
        self.operationId = operationId
        self.replicaId = replicaId

    def getResult(self):
        return self.result

    def __str__(self):
        return '[' + str(self.result) + "," + str(self.operationName) + "," + str(self.operationId) + "," + str(self.replicaId) + "]"
