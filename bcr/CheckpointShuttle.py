class CheckpointShuttle:

    def __init__(self, slot, listOfCheckpointSt):
        self.checkpointSlot = slot
        self.listOfCheckpointSt = listOfCheckpointSt

    def getCheckpointSlot(self):
        return self.checkpointSlot

    def getListOfCheckpointSt(self):
        return self.listOfCheckpointSt


    def addCheckpointStatement(self, st):
        self.listOfCheckpointSt.append(st)

    def __str__(self):
        return 'checkpointSlot:' + str(self.checkpointSlot) + "\n checkpointStatement:" + ",".join(str(i) for i in self.listOfCheckpointSt)
