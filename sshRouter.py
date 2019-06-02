#!/usr/local/python
#Creats an SSH session to the router
import base64
import paramiko
import json

def sendCommand(ipAddress,usr,pwd,command):
    #Run command on the Mesh Device
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ipAddress, username= usr, password= pwd)
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read()
    error = stderr.read()
    stdin.flush()
    print (output)
    return output, error;
    client.close()

#sendCommand("127.0.0.1","akshay","akshay911","ls -lrt")
