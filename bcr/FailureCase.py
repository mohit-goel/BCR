import sys
from MessageTypes import MessageTypes
class FailureCase:
    def __init__(self,failcase,configuration,index,operationName,shuttle,clientNumber,messageType,messageNumber,head):
        self.failcase = failcase
        self.configuration = configuration
        self.index = index
        self.operationName = operationName
        self.shuttle = shuttle
        self.clientNumber = clientNumber
        self.messageType = messageType
        self.messageNumber = messageNumber
        self.action = ""
        self.failure = None
        self.head = head

        for fail in failcase:
            print(self.messageType)
            if (fail.condition == "client_request") & (self.messageType == MessageTypes.DIRECT):
                if (fail.client == self.clientNumber) & (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    self.failure = fail.condition + "(" +str(fail.client)+ "," + str(fail.requestnum) + ")" + fail.action + "()"
                    doFailure(fail.action)
            elif (fail.condition == "forwarded_request") & (self.messageType == MessageTypes.FORWARDED):
                if (fail.client == self.clientNumber) & (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    doFailure(fail.action)
            elif (fail.condition == "shuttle") & (self.messageType == MessageTypes.SHUTTLE):
                if (fail.client == self.clientNumber) & (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    self.doFailure(fail.action)
            elif (fail.condition == "result_shuttle") & (self.messageType == MessageTypes.RESULT_SHUTTLE):
                if (fail.client == self.clientNumber) & (fail.requestnum == messageNumber.clientMessageTypeCountDict[self.clientNumber][self.messageType]):
                    doFailure(fail.action) 
                        
    def doFailure(self,action):
        self.action = action
        orderstmts = self.shuttle.orderProof.getlistOfOrderSt()
        resultstmts = self.shuttle.resultProof.getlistOfResultSt()
        print('Encountered Failure Scenario')
        if action == "change_operation":
            for x in orderstmts:
                if (x.replicaId == self.index) :
                    x.operationName = 'get'
                    #x.key = 'x'
                    #x.value = None 
            for x in resultstmts:
                if (x.replicaId == self.index) :
                    x.operationName = 'get'
            print('operation is modified to %s' % x.operationName)   
        elif action == "change_result":
            for x in resultstmts:
                if (x.replicaId == self.index):
                    x.result = 'OK'
                    print('result is modified to %s' % x.result)
        elif action == "drop_result_stmt":    
            resultstmts = [x for x in resultstmts if x.replicaId != 0]
            self.shuttle.resultProof.setlistOfOrderSt(resultstmts)
            print('Head result statement is dropped in shuttle %s' % self.shuttle)
        
 
    def __str__(self):
     #return '[' + ",".join(self.failcase) +";" +  str(self.operationName) + ";" + str(self.key) + ";" + str(self.value)
     return  str(self.failure) + " for messagetype:" + str(self.messageType) + " and operation:" + str(self.operationName)
 