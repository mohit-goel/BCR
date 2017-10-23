import sys
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
            print(self.messageType)
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

    def __str__(self):
        return str(self.failure)
