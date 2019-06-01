#Creats an SSH session to the router
import base64
import paramiko
import json


def sendCommand(command):
    #key = paramiko.RSAKey(data=base64.b64decode(b'AAA...'))
    client = paramiko.SSHClient()
    #Read Data from JSON File
    with open('data.json') as json_file:
        data = json.load(json_file)
        ipAddress = (data["ipAddress"])
        user = (data["username"])
        pwd = (data["password"])

#client.get_host_keys().add('ipAddress', 'ssh-rsa', key)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ipAddress, username= user, password= pwd)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read()
        error = stderr.read()
        stdin.flush()
        print (output)
        return output, error;
        client.close()

def checkParam(param):
    print("The params are:" + param)


def main():
    #Run command on the Mesh Device
    command = "ls -lrt"
    sendCommand(command)
    checkParam("akshay")

main()

