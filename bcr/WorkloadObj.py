import sys

class WorkloadObj:
    def __init__(self,object):
        if(len(object)==3):
            self.value = object[2].strip()
        else:
            self.value = None
        self.action = object[0].strip()
        self.key = object[1].strip()
