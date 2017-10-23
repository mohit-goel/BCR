class FailureChecks:
    def __init__(self):
        self.change_operation = False
        self.change_result = False
        self.drop_result_stmt = False
        self.change_privatekey = False
    
    def __str__(self):
        return " change_oper=" + str(self.change_operation) + " change_result="+ str(self.change_result) + " drop_result="+str(self.drop_result_stmt) + " change_privatekey="+str(self.change_privatekey)
