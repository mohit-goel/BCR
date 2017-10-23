import sys


class WorkloadObj:
    def __init__(self, object):
        self.action = object[0].strip()
        self.key = object[1].strip()
        if(len(object) == 3):
            self.value = object[2].strip()
        else:
            self.value = None

    def __str__(self):
        return '[' + str(self.action) + ":" + str(self.key) + ":" + str(self.value) + ']'
