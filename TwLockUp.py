#!/usr/bin/python
# -*- coding: UTF-8 -*-
#> Twitter LookeUp Show Someone Profile Info In Twitter
#> By: Oseid Aldary

## IMPORT LIBRARIES ##

import socket,urllib,sys,datetime
from time import sleep
try:
   from bs4 import BeautifulSoup as soup
except:
	print("\n[!] Error The [ bs4 ] library Is Not Install In Your Python \n[#] Install It Using This Command: pip install bs4\n[#] And Try Again :)")
	exit(1)
## Import Libraries Done!

## SHOW TIME ##
now = datetime.datetime.now()
hour = now.hour
min = now.minute
sec = now.second
timenow = "{}:{}:{}".format(hour,min,sec)

## Check internet Connection...
server = "www.google.com"
def check():
  try:
     ip = socket.gethostbyname(server)
     conn = socket.create_connection((ip, 80), 2)
     return True
  except:
	pass
  return False
## Check Internet Done

## COLORS ###
wi = "\033[0m"
rd = "\033[31m"
gr = "\033[32m"
yl = "\033[33m"
bl = "\033[36m"
##############

#Usage msg ##
if len(sys.argv) !=2:
	print("""
________         ______                   ______ _____  __             
___  __/__      ____  / _____________________  /___  / / /_______      
__  /  __ | /| / /_  /  _  __ \  __ \  ___/_  //_/  / / /___  __ \     
_  /   __ |/ |/ /_  /___/ /_/ / /_/ / /__ _  ,<  / /_/ / __  /_/ /     
/_/    ____/|__/ /_____/\____/\____/\___/ /_/|_| \____/  _  .___/      
                                                         /_/                
____________________________________________________________
[#] Twitter LookeUp Show Somenoe ProFile Info In Twitter   [#]
[$] Coded By: Oseid Aldary :)				   [$]
[@] Thanks For Usage					   [@]

Usage:
	python TwitterPoint.py <UserName>
Ex:
	python TwitterPoint.py Twitter """)
	exit()

############# Done ######################

## Start :)

USER = sys.argv[1]
UU = sys.argv[1]
def twitter(USER,UU):
     try:
	print("\n"+rd+"="*10+">"+bl+" CONFIG "+rd+"<"+"="*10+"\n")
        sleep(0.30)
	print(gr+"[@] "+wi+"Start At   :"+bl+" [  "+str(timenow)+" ]")
        sleep(0.30)
	print(gr+"[>] "+wi+"Website    :"+bl+" [ www.twitter.com ]")
	sleep(0.30)
	print(gr+"[>] "+wi+"UserName   :"+bl+" [ "+UU+" ]")
	sleep(1)
	print(rd+"\n[#]"+gr+" Finding Info About USER [ "+bl+UU+gr+" ]......")

	openurl = urllib.urlopen(USER)
	DATA = openurl.read() # Page Source Code For Find Info From him :)
	s = soup(DATA, 'html.parser')
	INFO = s.find_all("span" ,{"data-is-compact":"false"})
	FOLLOWING = INFO[1].text.encode("utf-8") # User Following
	NAME = s.find("a" ,{"href":"/"+USER.split("/")[-1]}).text.encode("utf-8").replace("  ","").replace("\n","") ## USER NAME
	FOLLOWERS = INFO[2].text.encode("utf-8") ## USER FILLOWERS
	LIKES = INFO[3].text.encode("utf-8") ## USER LIKES
	PIC = s.find("a" ,{"class":"ProfileAvatar-container u-block js-tooltip profile-picture"})["href"].encode("utf-8") ## USER Profile-Picture
	DATE = s.find("span" ,{"class":"ProfileHeaderCard-joinDateText js-tooltip u-dir"})["title"].encode("utf-8") # USER Join To Twitter Date 

	# OUTPUT THE INFO TO USER
	print(gr+"\n[#] Found!\n"+yl+"------------------"+rd+" INFO"+yl+" ------------------")
	print(gr+"[U] "+wi+"UserName    : [ "+bl+NAME+wi+" ]")
        print(gr+"[F] "+wi+"Following   : [ "+bl+FOLLOWING+wi+" ]")
	print(gr+"[F] "+wi+"Followers   : [ "+bl+FOLLOWERS+wi+" ]")
	print(gr+"[L] "+wi+"Likes       : [ "+bl+LIKES+wi+" ]")
	print(gr+"[D] "+wi+"Date Join   : [ "+bl+DATE+wi+" ]")
	print(gr+"[P] "+wi+"ProFile PIC : [ "+bl+PIC+wi+" ]")
	print(gr+"\n[S] "+wi+"Shutdown At : [ "+str(timenow)+" ]")
	print(rd+"[#] "+bl+"Done! :)")

     except: # Her The Script Can't Find You input Name In Twitter May be removed from twitter!
	print(yl+"\n[!]"+wi+"I Can't Find This USER[ "+rd+UU+wi+" ] In Twitter Users! "+rd+":{")
	print(gr+"[#]"+bl+"Check Name OR Try Other UserName "+gr+":)")
	exit(1)

if check() == True:
  if "twitter.com" in USER:
        twitter(USER,UU)
  else:
      twitter("https://twitter.com/" + USER,UU)
else:
        print(yl+"\n[!] "+rd+"Error:"+wi+" Your Not Connected To["+rd+"Internet"+wi+"]\n"+gr+"[*]"+wi+"Please Connect To Internet And Try Again :)")
        exit(1)

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye
