#Scan the IP Addres range and collect alive IP list
from ipscan import scanStatus
from sshRouter import sendCommand
import json

command = "ls -lrt"
liveNodes = scanStatus()
#SSH to alive IP and run a command
with open('data.json') as json_file:
        data = json.load(json_file)
        usr = (data["username"])
        pwd = (data["password"])

for x in range (len(liveNodes)):
    print("Running command " + command + " on " + liveNodes[x] + " with username password as " + usr + " " + pwd)
    output,error = sendCommand(liveNodes[x],usr,pwd,command)
    print (output)
    
