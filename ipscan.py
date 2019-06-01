import socket
import json
from datetime import datetime

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

def main():
    ipAlive = []
    subnet,ip,startNum,endNum = readData()
    addr = ip + str(startNum)
    print ("Scanning address:" + ip)
    for x in range (startNum,endNum):
        ipa = subnet + str(startNum)
        if (scan(ipa)):
            print(ip, "is alive!")
            ipAlive.append(ipa)
        else:
            print ("Node " + ipa + " is dead!")
        startNum = startNum + 1
    #t1 = datetime.now()
    #t2 = datetime.now()
    #total = t2 - t1
    #print ("Scanning completed in: " , total)

main()
