import sys
import re
from MessageTypes import MessageTypes


class FailureCase:
    def __init__(self, failcase, index, clientNumber, messageType, messageNumber, failureChecks):
        self.failcase = failcase
        self.index = index
        self.clientNumber = clientNumber
        self.messageType = messageType
        self.messageNumber = messageNumber
        self.failure = None
        self.failureChecks = failureChecks

        for fail in failcase:
            if (fail.condition == "client_request") and (self.messageType == MessageTypes.DIRECT):
                if (fail.client == self.clientNumber) and (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    self.failure = fail.condition + \
                        "(" + str(fail.client) + "," + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "forwarded_request") and (self.messageType == MessageTypes.FORWARDED):
                if (fail.client == self.clientNumber) and (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    self.failure = fail.condition + \
                        "(" + str(fail.client) + "," + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "shuttle") and (self.messageType == MessageTypes.SHUTTLE):
                if (fail.client == self.clientNumber) and (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    self.failure = fail.condition + \
                        "(" + str(fail.client) + "," + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "result_shuttle") and (self.messageType == MessageTypes.RESULT_SHUTTLE):
                if (fail.client == self.clientNumber) and (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    self.failure = fail.condition + \
                        "(" + str(fail.client) + "," + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "checkpoint") and (self.messageType == MessageTypes.CHECKPOINT):
                if (fail.requestnum == messageNumber.replicaMessageTypeCountDict[self.messageType]):
                    self.failure = fail.condition + \
                        "(" + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "completed_checkpoint") and (self.messageType == MessageTypes.COMPLETED_CHECKPOINT):
                if (fail.requestnum == messageNumber.replicaMessageTypeCountDict[self.messageType]):
                    self.failure = fail.condition + \
                        "(" + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "wedge_request") and (self.messageType == MessageTypes.WEDGE_REQUEST):
                if (fail.requestnum == messageNumber.replicaMessageTypeCountDict[self.messageType]):
                    self.failure = fail.condition + \
                        "(" + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "new_configuration") and (self.messageType == MessageTypes.NEW_CONFIGURATION):
                if (fail.requestnum == messageNumber.replicaMessageTypeCountDict[self.messageType]):
                    self.failure = fail.condition + \
                        "(" + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "get_running_state") and (self.messageType == MessageTypes.GET_RUNNUNG_STATE):
                if (fail.requestnum == messageNumber.replicaMessageTypeCountDict[self.messageType]):
                    self.failure = fail.condition + \
                        "(" + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)
            if (fail.condition == "catch_up") and (self.messageType == MessageTypes.CATCH_UP):
                if (fail.requestnum == messageNumber.replicaMessageTypeCountDict[self.messageType]):
                    self.failure = fail.condition + \
                        "(" + \
                        str(fail.requestnum) + ")," + fail.action + "()"
                    self.doFailure(fail.action)

    def doFailure(self, action):
        print('Encountered Failure Scenario')
        if action == "change_operation":
            self.failureChecks.change_operation = True
        elif action == "change_result":
            self.failureChecks.change_result = True
        elif action == "drop_result_stmt":
            self.failureChecks.drop_result_stmt = True
        elif action == "change_privatekey":
            self.failureChecks.change_privatekey = True
        elif action == "remove_operationhistory":
            self.failureChecks.remove_operationhistory = True
        elif action == "crash":
            self.failureChecks.crash = True
        elif action == "truncate_history":
            self.failureChecks.truncate_history = True
        elif action == "drop":
            self.failureChecks.drop = True
        elif action == "increment_slot":
            self.failureChecks.increment_slot = True
        elif action == "extra_op":
            self.failureChecks.extra_op = True
        elif action == "invalid_order_sig":
            self.failureChecks.invalid_order_sig = True
        elif action == "invalid_result_sig":
            self.failureChecks.invalid_result_sig = True
        elif action == "drop_checkpt_stmts":
            self.failureChecks.drop_checkpt_stmts = True
        elif action.startswith('sleep'):
            number = re.findall(r'\d+', action)
            self.failureChecks.sleep = int(number[0])
        

    def __str__(self):
        return str(self.failure)
