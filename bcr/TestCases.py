class TestCases:
    
    def __init__(self,testCaseName,masterDict):
        self.clientToResultDictionary = dict()
        self.testCaseName =testCaseName
        self.masterDict = masterDict
        
    def verify(self,clientNumber,clientResultDict):
        print('Verifying Test case:%s client:%i',self.testCaseName,clientNumber)
        return True


        
        
    
            