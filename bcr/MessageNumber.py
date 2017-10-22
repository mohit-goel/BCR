import sys

class MessageNumber:
    def __init__(self):
        self.clientMessageTypeCountDict = dict()
            
    def incrementMessageType(self,client,messagetype):
        if client not in self.clientMessageTypeCountDict:
            self.clientMessageTypeCountDict[client] = dict()
        if messagetype not in  self.clientMessageTypeCountDict[client] :
            self.clientMessageTypeCountDict[client][messagetype]=-1
        self.clientMessageTypeCountDict[client][messagetype] = self.clientMessageTypeCountDict[client][messagetype] + 1
        
    def getClientMessageTypeCount(self,client,messagetype):
          return self.clientMessageTypeCountDict[client][messagetype]
      
    def getDict(self):
        return self.clientMessageTypeCountDict
           
    
