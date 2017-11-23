import sys


class MessageNumber:
    def __init__(self):
        self.clientMessageTypeCountDict = dict()
        self.replicaMessageTypeCountDict = dict()

    def incrementMessageType(self, client, messagetype):
        if client not in self.clientMessageTypeCountDict:
            self.clientMessageTypeCountDict[client] = dict()
        if messagetype not in self.clientMessageTypeCountDict[client]:
            self.clientMessageTypeCountDict[client][messagetype] = -1
        self.clientMessageTypeCountDict[client][messagetype] = self.clientMessageTypeCountDict[client][messagetype] + 1

    def incrementReplicaMessageType(self, messagetype):
        if messagetype not in self.replicaMessageTypeCountDict:
            self.replicaMessageTypeCountDict[messagetype] = -1
        self.replicaMessageTypeCountDict[messagetype] = self.replicaMessageTypeCountDict[messagetype] + 1

    def getClientMessageTypeCount(self, client, messagetype):
        return self.clientMessageTypeCountDict[client][messagetype]

    def getReplicaMessageTypeCount(self, messagetype):
        return self.replicaMessageTypeCountDict[messagetype]

    def getDict(self):
        return self.clientMessageTypeCountDict

    def getReplicaDict(self):
        return self.replicaMessageTypeCountDict
