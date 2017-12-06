
class OrderStatement:

    def __init__(self, slot, operationName, operationId, replicaId):
        self.slot = slot
        self.operationName = operationName
        self.operationId = operationId
        self.replicaId = replicaId

    def getSlot(self):
        return self.slot

    def __str__(self):
        return '[' + str(self.slot) + "," + str(self.operationName) + "," + str(self.operationId) + "," + str(self.replicaId) + "]"
