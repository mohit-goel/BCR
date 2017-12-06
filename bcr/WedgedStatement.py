import copy


class WedgedStatement:

    def __init__(self, checkpoint, slotOperationHist1):
        self.checkpoint = checkpoint
        self.slotOperationHist = {
            key: slotOperationHist1[key] for key in slotOperationHist1.keys()}

    def __str__(self):
        hist = ",".join((str(k) + '=' + str(v))
                        for (k, v) in self.slotOperationHist.items())
        return '[checkpoint: ' + str(self.checkpoint) + ';history: ' + hist + ']'
