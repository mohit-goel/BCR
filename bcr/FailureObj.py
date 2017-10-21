import sys
import re
class FailureObj:
    def __init__(self,cond,cl,req,act):
        self.condition = cond
        self.client = cl
        self.requestnum = req
        self.action = act
        
    def __str__(self):
     return '[' +"Failure object is " +  str(self.condition) + "," + str(self.client) + "," + str(self.requestnum) + "," + str(self.action) + "]"
