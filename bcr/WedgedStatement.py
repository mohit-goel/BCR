class WedgedStatement:
    
    def __init__(self, checkpoint,slotOperationHist):
        self.checkpoint = checkpoint
        self.slotOperationHist = slotOperationHist
        
    def __str__(self):
        return '[' + str(self.checkpoint) + ";" + str(self.slotOperationHist) + "]"
    