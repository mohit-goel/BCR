import sys
import re
from WorkloadObj import WorkloadObj
from FailureObj import FailureObj
from PseudoRandom import PseudoRandom


class configread:
    def __init__(self, inp):
        self.pseudoRandom = PseudoRandom()
        input_file = inp
        self.workload = dict()
        self.host = dict()
        self.client_host = dict()
        self.replica_host = dict()
        self.failure = dict()
        self.pseudorandom_workload = dict()
        self.checkpt_interval = 1

        with open(input_file) as f:
            for line in f:
                line = line.strip()
                if line[0] != '#':
                    (key, sep, val) = line.partition('=')
                    key = key.strip()
                    # if the line does not contain '=',
                    # it is invalid and hence ignored
                    if len(sep) != 0:
                        val = val.strip()
                        if line.startswith('test_case_name'):
                            self.test_case_name = val
                        elif line.startswith('t'):
                            self.failure_num = int(val)
                        elif line.startswith('num_client'):
                            self.num_client = int(val)
                        elif line.startswith('client_timeout'):
                            self.client_timeout = int(val) / 1000
                        elif line.startswith('head_timeout'):
                            self.head_timeout = int(val) / 1000
                        elif line.startswith('nonhead_timeout'):
                            self.nonhead_timeout = int(val) / 1000
                        elif line.startswith('checkpt_interval'):
                            self.checkpt_interval = int(val)
                        elif line.startswith('hosts'):
                            pattern = re.split(';', val)
                            pattern = [int(x.strip()) for x in pattern]
                            i = 0
                            for x in pattern:
                                self.host[i] = x
                                i = i + 1
                        elif line.startswith('client_hosts'):
                            pattern = re.split(';', val)
                            pattern = [int(x.strip()) for x in pattern]
                            i = 0
                            for x in pattern:
                                self.client_host[i] = x
                                i = i + 1
                        elif line.startswith('replica_hosts'):
                            pattern = re.split(';', val)
                            pattern = [int(x.strip()) for x in pattern]
                            i = 0
                            for x in pattern:
                                self.replica_host[i] = x
                                i = i + 1
                        elif line.startswith('pseudorandom_workload'):
                            i = int(re.search(r'\d+', key).group())
                            self.pseudorandom_workload[i] = []
                            pattern = re.split(';', val)
                            pattern = [x.strip() for x in pattern]
                            for x in pattern:
                                x = x.replace(")", "")
                                x = x.replace("'", "")
                                x = x.replace("(", ",")
                                object = re.split(',', x)
                                y = WorkloadObj(object)
                                self.pseudorandom_workload[i].append(y)

                        elif line.startswith('workload'):
                            i = int(re.search(r'\d+', key).group())
                            self.workload[i] = []
                            pattern = re.split(';', val)
                            pattern = [x.strip() for x in pattern]
                            for x in pattern:
                                x = x.replace(")", "")
                                x = x.replace("'", "")
                                x = x.replace("(", ",")
                                object = re.split(',', x)
                                y = WorkloadObj(object)
                                if y.action == 'pseudorandom':
                                    list = self.pseudoRandom.select_random_elements_of_list(
                                        self.pseudorandom_workload[i], int(y.value), int(y.key))
                                    for x in list:
                                        self.workload[i].append(x)

                                else:
                                    self.workload[i].append(y)
                        elif line.startswith('failures'):
                            number = re.findall(r'\d+', key)
                            i = int(number[0])
                            j = int(number[1])
                            pattern = re.split(';', val)
                            pattern = [x.strip() for x in pattern]
                            self.failure[(i, j)] = []
                            for x in pattern:
                                spattern = re.split(',', x)
                                spattern = [temp.strip() for temp in spattern]
                                if len(spattern) > 2:
                                    number = re.findall(r'\d+', x)
                                    client = int(number[0])
                                    req = int(number[1])
                                    x = x.replace(")", "")
                                    x = x.replace("(", ",")
                                    y = re.split(',', x)
                                    cond = y[0].strip()
                                    action = y[3].strip()
                                    if len(number) >2:
                                        sleeptime = int(number[2])
                                        action = action + str(sleeptime)                                
                                        
                                else:
                                    number = re.findall(r'\d+', x)
                                    client = -1
                                    req = int(number[0])
                                    x = x.replace(")", "")
                                    x = x.replace("(", ",")
                                    y = re.split(',', x)
                                    cond = y[0].strip()
                                    action = y[2].strip()
                                    if len(number) >1:
                                        sleeptime = int(number[1])
                                        action = action + str(sleeptime)
                                
                                f = FailureObj(cond, client, req, action)
                                self.failure[(i, j)].append(f)
                                    
                                    
                                #number = re.findall(r'\d+', x)
                                #client = int(number[0])
                                #req = int(number[1])
                                #x = x.replace(")", "")
                                #x = x.replace("(", ",")
                                #y = re.split(',', x)
                                #cond = y[0].strip()
                                #action = y[3].strip()
                                #print("cond is %s, client is %i, req is %i, action is %s" % (cond,client,req,action))
