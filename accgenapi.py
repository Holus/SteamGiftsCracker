from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests; import re
from lxml.html import fromstring
from urlparse import urlparse
from urlparse import urljoin
import urllib2
import random
import time
import socket
from win32process import CREATE_NO_WINDOW
import threading
import sys, os
import json
print("This is a public api posted in github, with a limit of 30 accounts per minute.")
print("If You don't get accounts, or want to be faster go on https://accgen.cathook.club/ and request a private api key to put down here ") 
def Choperro():
    rekey = "FBVKP3E-2SX489H-NJBA5T2-TB0BMRE"
    while 1:
        time.sleep(2)
        try:
            resurl = "https://catbot.club:2053/api/v1/account/"+ str(rekey)
            contents = urllib2.urlopen(resurl).read()
            if "password" in contents:
                    f= open("accs.txt","a+")
                    y = json.loads(contents)
                    print(y["login"])
                    userid = y["login"]
                    print(y["password"])
                    userpw = y["password"]
                    #print contents
                    f.write(str(userid) + ":" + str(userpw) + "\n")

                    f.close()
            if "Error" in contents:
                print("Someone else is using this |Api Requests * Minute Exausted, get Your own private api key from accgen.cathook.club")
                    
        except Exception as e:
            print(e)
            Choperro()
Choperro()
