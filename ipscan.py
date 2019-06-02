#Scans the IP address range sockets
import socket
import json
from datetime import datetime


def info(message):
    print("\n" + message + "\n")

def scan(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip,135))
    if result == 0:
      return 1
    else :
      return 0

def readData ():
    with open('data.json') as json_file:
        data = json.load(json_file)
        net = (data["ipAddress"])
        st1 = (data["startAddress"])
        en1 = (data["endAddress"])
        #net = input("Enter the IP address: ")
        net1 = net.split('.')
        a = '.'
        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        #st1 = int(input("Enter the Starting Number: "))
        #en1 = int(input("Enter the Last Number: "))
        return net2,net,st1,en1;

def scanStatus():
    ipAlive = []
    subnet,ip,startNum,endNum = readData()
    t1 = datetime.now()
    while startNum <= endNum:
        ip = subnet + str(startNum)
        up = scan(ip)
        if(up):
            info("Node " + ip + " is up!")
            ipAlive.append(ip)
        else:
            info("Node " + ip + " is dead!")
        startNum+=1
    t2 = datetime.now()
    total = t2 - t1
    info("Scanning completed in: " + str(total))
    return ipAlive
scanStatus()
