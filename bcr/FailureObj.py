import sys
import re
class FailureObj:
    def __init__(self,cond,cl,req,act):
        self.condition = cond
        self.client = cl
        self.requestnum = req
        self.action = act
