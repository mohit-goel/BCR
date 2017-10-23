from OperationState import OperationState
import json


class ReplicaHistory:

    def __init__(self):
        self.operationStateDict = dict()
        self.slotOperationDict = dict()

    def insertOperation(self, operation, localResult, slot):
        self.operationStateDict[operation] = OperationState(localResult, slot)
        self.slotOperationDict[slot] = operation

    def doesSlotExistForDifferentOperation(self, slot, new_operation):
        if slot in self.slotOperationDict:
            operation = self.slotOperationDict.get(slot)

            if new_operation == operation:
                return True
            else:
                return False
        else:
            return False

    def isOperationExist(self, operation):
        return operation in self.operationStateDict

    def isResultShuttleArrivedForOperation(self, operation):
        if operation in self.operationStateDict:
            operationState = self.operationStateDict.get(operation)
            re = operationState.get_result_shuttle() is not None
            return re
        else:
            return False

    def getSlotForOperation(self, operation):
        if operation in self.operationStateDict:
            operationState = self.operationStateDict.get(operation)
            return (True, operationState.get_slot())
        else:
            return (False, -1)

    def getResultShuttleForOperation(self, operation):
        if operation in self.operationStateDict:
            operationState = self.operationStateDict.get(operation)
            return (True, operationState.get_result_shuttle())
        else:
            return (False, None)

    def setResultShuttleForOperation(self, operation, shuttle):
        operationState = self.operationStateDict.get(operation)
        operationState.set_result_shuttle(shuttle)

    def setSlotForOperation(self, operation, slot):
        operationState = self.operationStateDict.get(operation)
        operationState.set_slot(slot)

    def setLocalResultForOperation(self, operation, result):
        operationState = self.operationStateDict.get(operation)
        operationState.set_result_shuttle(result)

    def __str__(self):
        res = []
        res.append('\n')
        res.append("operationStateDict=")

        for k, v in self.operationStateDict.items():
            res.append(str(k) + "=" + str(v))
            res.append('\n')
        res.append('\n')
        res.append("slotOperationDict=")

        for k, v in self.slotOperationDict.items():
            res.append(str(k) + "=" + str(v))
            res.append('\n')

        return ",".join(res)
