from OperationState import OperationState
import json


class ReplicaHistory:

    def __init__(self):
        self.operationStateDict = dict()
        self.slotOperationDict = dict()
        self.slotRunningStateHashDict = dict()
        self.lastCheckpointProof = None
        self.lastCheckpointSlot = -1
        self.clientResultStDict = dict()

    def insertOperation(self, operation,clientRequest, localResult, slot):
        self.operationStateDict[operation] = OperationState(localResult, slot)
        self.slotOperationDict[slot] = clientRequest

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
    
    def getResultStForClient(self, client):
        if client in self.clientResultStDict:
            (result,resultSt) = self.clientResultStDict(client)
            return resultSt
        else:
            return None

    def setResultStForClient(self, client,result, resultSt):
        self.clientResultStDict[client] = (result,resultSt)
        
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
        
        
    def removeOperation(self,operation):
        try:
            self.operationStateDict.pop(operation)
        except:
            print('error while removing operation')
    
    def addRunningStateHash(self,slot,runningStateHash):
        self.slotRunningStateHashDict[slot] = runningStateHash
    
    def getRunningStateHash(self,slot):
        if slot in self.slotRunningStateHashDict:
            return self.slotRunningStateHashDict[slot]
        else:
            return None

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
        
        res.append("slotRunnungStateHashDict=")

        for k, v in self.slotRunningStateHashDict.items():
            res.append(str(k) + "=" + str(v))
            res.append('\n')
        
        res.append("lastCheckpointProof=")
        res.append(str(lastCheckpointProof))
        res.append('\n')
        

        return ",".join(res)
