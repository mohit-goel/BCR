
				
PLATFORM:  
DistAlgo version -- 1.0.9 
Python Implementation CPython 3.6.3
Operating System: macOS Sierra 10.12.6 (16G29)
PyNacl: 1.1.2
		   
		   
INSTRUCTIONS: 
Install Python3
Install Distalgo: "sudo pip3 install pyDistAlgo"
Install PyNacl: "sudo pip3 install pynacl"

MAIN FILES.  
			       
		1. src/bcr.da : This file contains code for master to read configuration file from command line and initiate Olympus and Clients.
		2. src/client.da :This file contains code for clients to send client requests and receive client responses, configuration request & response to Olympus
		3. src/olympus.da : This file contains code for olympus to initiate replicas and hsndling configuration requests from clients
		4. src/replica.da : This file contains code for replica to handle client requests and other replica messages.

SINGLE PROCESS SETUP
python3 -m da --logfile --logfilename testCaseName.txt --logfilelevel 'info' --message-buffer-size size_Bytes bcr.da configurationFileName.txt

Multi Node/Process Setup
python3 -m da -r  --message-buffer-size=1280000 --logfile --logfilename logdirect/replica0.log --logfilelevel info -n ReplicaNode0  -D replica.da
python3 -m da -r  --message-buffer-size=1280000 --logfile --logfilename logdirect/replica1.log --logfilelevel info -n ReplicaNode1  -D replica.da
python3 -m da -r  --message-buffer-size=1280000 --logfile --logfilename logdirect/replica2.log --logfilelevel info -n ReplicaNode2  -D replica.da
python3 -m da -r --message-buffer-size=1280000 --logfile --logfilename logdirect/client.log --logfilelevel info  -n ClientNode   -D client.da
python3 -m da -r  --message-buffer-size=1280000  --logfile --logfilename logdirect/olympus.log --logfilelevel info  -n OlympusNode  -D olympus.da
python3 -m da -r  --message-buffer-size=1280000  --logfile --logfilename logdirect/master.log --logfilelevel info  -n MasterNode  bcr.da perform900.txt

WORKLOAD GENERATION: 

class PseudoRandom:

   def select_random_elements_of_list(self, l, num_required_elements, seed):
       len_of_list = len(l)
       sample = []
       random.seed(seed)
       for i in range(num_required_elements):
           index = random.randint(0, len_of_list - 1)
           sample.append(l[index])

       return sample
       
num_required_elements : number of requests to be generated
l : specify the list present in configuration.csv from which request will be picked up randomly

We are using python in-built 'random' utiltiy to generate 'num_required_elements' numbers  corresponding to one of the indexes in the list.


CONFIGURATION FILES 
support configuration files specified in project.txt

LOGS 
detailed and readable logs 

DOCUMENTATION 
README and testing.txt contain all information specified in project.txt 


PERFORMANCE EVALUATION 
1. RAFT   :  8.78 seconds

2. single-host configuration : 61 seconds

3. Multi-Host setup with replicas on different host : 60 seconds  


Code Size: 
 
79 text files.
79 unique files.
50 files ignored.

github.com/AlDanial/cloc v 1.74  T=0.24 s (122.3 files/s, 10423.5 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
DAL                              4            212              1           1416
Python                          25            150             18            675
-------------------------------------------------------------------------------
SUM:                            29            362             19           2091
 

