class FailureChecks:
    def __init__(self):
        self.change_operation = False
        self.change_result = False
        self.drop_result_stmt = False
        self.change_privatekey = False
        self.remove_operationhistory = False
        self.crash = False
        self.truncate_history = False
        self.sleep = False
        self.sleeptime = 0
        self.drop = False
        self.increment_slot = False
        self.extra_op = False
        self.invalid_order_sig = False
        self.invalid_result_sig = False
        self.drop_checkpt_stmts = False

    def __str__(self):
        return " change_oper=" + str(self.change_operation) + " change_result=" + str(self.change_result) + " drop_result=" + str(self.drop_result_stmt) + " change_privatekey=" + str(self.change_privatekey) + " remove_operationhistory="+str(self.remove_operationhistory) + " crash=" + str(self.crash) + " truncate_history=" + str(self.truncate_history) + " sleep=" + str(self.sleep) + " drop=" + str(self.drop) + " increment_slot="+str(self.increment_slot) + " extra_op=" + str(self.extra_op) + " invalid_order_sig=" + str(self.invalid_order_sig) + " invalid_result_sig=" + str(self.invalid_result_sig) + " drop_checkpt_stmts=" + str(self.drop_checkpt_stmts)
