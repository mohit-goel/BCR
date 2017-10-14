class OperationState:
    
    def __init__(self,localResult,slot):
        self.localResult = localResult
        self.slot = slot
        self.resultShuttle = None

    def get_local_result(self):
        return self.localResult


    def get_slot(self):
        return self.slot


    def get_result_shuttle(self):
        return self.resultShuttle


    def set_local_result(self, value):
        self.localResult = value


    def set_slot(self, value):
        self.slot = value


    def set_result_shuttle(self, value):
        self.resultShuttle = value
        
        
    def __str__(self):
     return 'localResult: '  + str(self.localResult) + ",slot: " + str(self.slot) + ", resultShuttle: " + str(self.resultShuttle)
        
    
        