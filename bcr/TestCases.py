class TestCases:
    
    def __init__(self,testCaseName,masterDict):
        self.clientToResultDictionary = dict()
        self.testCaseName =testCaseName
        self.masterDict = masterDict
        
    def verify(self,clientNumber,clientResultDict):
        if(self.testCaseName == 'stresstest'):
            print('Verifying Test case:%s client:%i',self.testCaseName,clientNumber)
            print('Expected Dict' + str(self.masterDict))
            print('Actual Dict' + str(clientResultDict))
            assert self.masterDict == clientResultDict


        
        
    
            