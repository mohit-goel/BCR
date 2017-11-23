from State import State
from Crypto import Crypto

import logging


class Validations:

    def __init__(self):
        self.crypto = Crypto()

    def shouldReplicaAcceptRequest(self, state):

        if state.value != State.ACTIVE.value:
            return False
        else:
            return True

    def validationOfResultProof(self, result, resultProof, replicaPublicList, proc):
        if len(resultProof.getlistOfResultSt()) < (len(replicaPublicList)):
            return (False, "Result Proof validation fail: Result Statement of some replica missing")

        resultStList = resultProof.getlistOfResultSt()
        for i in range(len(resultStList)):
            currentEncodedSt = resultStList[i]
            currentKey = replicaPublicList[i]
            decodeSt = self.crypto.isSignatureVerified(
                currentKey, currentEncodedSt)
            if (decodeSt is None):
                return (False, "Result proof validation fail: Signature not verified")

            if(not self.crypto.verifyHashes(result, decodeSt.result)):
                return (False, "Result proof validation fail: Result doesn't match Result Stmt of some replica")

        return (True, "Result Proof is valid")

    def clientValidationOfResultProof(self, result, resultProof, replicaPublicList, proc, t):
        if len(resultProof.getlistOfResultSt()) < (len(replicaPublicList)):
            return (False, "Result Proof validation fail: Result Statement of some replica missing")

        resultStList = resultProof.getlistOfResultSt()
        numberOfResultStMatched = 0
        for i in range(len(resultStList)):
            currentEncodedSt = resultStList[i]
            currentKey = replicaPublicList[i]
            decodeSt = self.crypto.isSignatureVerified(
                currentKey, currentEncodedSt)
            if (not ((decodeSt is None) or (not self.crypto.verifyHashes(result, decodeSt.result)))):
                numberOfResultStMatched += 1

        if numberOfResultStMatched >= t + 1:
            return (True, "Result Proof is valid")
        else:
            return (True, "Result Proof is notvalid: quoram not found")

    def clientValidationOfResultProofOlympus(self, result, resultProof, replicaPublicList, proc, t):

        resultStList = resultProof.getlistOfResultSt()
        numberOfResultStMatched = 0
        for i in range(len(resultStList)):
            decodeSt = resultStList[i]
            if (not self.crypto.verifyHashes(result, decodeSt.result)):
                numberOfResultStMatched += 1

        if numberOfResultStMatched >= t + 1:
            return (True, "Result Proof is valid")
        else:
            return (True, "Result Proof is Valid")

    def responseReceivedWithCorrectOperation(self, operationName, operationId, receivedOperationName, receivedOperationId):
        return (operationName == receivedOperationName) and (operationId == receivedOperationId)
