class CheckpointStatement   :

    def __init__(self, slot, runningStateHash):
        self.checkpointSlot = slot
        self.runningStateHash = runningStateHash
        #self.replicaId = replicaId

    def getSlot(self):
        return self.slot

    def __str__(self):
        return '[' + 'checkpointSlot:' + str(self.checkpointSlot) + ","  + 'runningStateHash:' + str(self.runningStateHash) + "," + 'replicaID:' +  str(self.replicaId) + "]"
