class ReconfigurationRequestObject:

    def __init__(self, process):
        self.process = process

    def __str__(self):
        return '[' + str(self.process) + ']'
