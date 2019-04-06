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

########TODO: UPDATE TO V3 Recaptcha 2Captcha API.

def CheckLoop():
    #go on recaptcha, fill balance and put api key down here
    rekey = ""
    while 1:
        userid = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
        driver.find_element_by_xpath("//button[@id='generate_button']").click()
        time.sleep(2)
        useridnew = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
        if userid == useridnew:
            driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
            time.sleep(1)
            #gangnam = driver.find_element_by_xpath("//input[@id='recaptcha-token']")
            getcodeurl = "http://2captcha.com/in.php?key=" + str(rekey) + "&method=userrecaptcha&googlekey=6Leuh5EUAAAAALediEIgey5dKbm1_P97zvzxjgvC&pageurl=https://accgen.cathook.club&invisible=1"
            testcode = urllib2.urlopen(getcodeurl).read()
            gc_IDex = testcode.split("|")
            gc_ID = gc_IDex[1]
            time.sleep(15)
            resurl = "http://2captcha.com/res.php?key="+ str(rekey) +"&action=get&id=" + str(gc_ID)
            contents = urllib2.urlopen(resurl).read()
            while "CAPCHA_NOT_READY" in contents:
                time.sleep(2)
                contents = urllib2.urlopen(resurl).read()
            #print "contents: " + str(contents)
            link = contents.split("|")
            #print "link: " + str(link)
            googleresolved = link[1]
            driver.switch_to_window(mainWin)
            #gre = driver.find_element_by_xpath("//textarea[@name='g-recaptcha-response']")
            #gre.send_keys(googleresolved)
            #print(googleresolved)
            driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='"+ str(googleresolved) + "'")
            driver.execute_script("on_captcha_valid('{}')".format(googleresolved))
            #delay = 3
            #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'acc_login')))
            time.sleep(25)
            source_code = driver.page_source
            while "Login:" not in source_code:
                time.sleep(1)
                source_code = driver.page_source


            source_code = driver.page_source
            useridnew = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
            if useridnew is not userid:
                userpwnew = driver.find_element_by_xpath("//h6[@id='acc_pass']/strong").text
                f= open("accs.txt","a+")
                f.write(str(useridnew) + ":" + str(userpwnew) + "\n")
                f.close()
                print str(useridnew) + ":" + str(userpwnew)
        else:
            useridnew = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
            userpwnew = driver.find_element_by_xpath("//h6[@id='acc_pass']/strong").text
            print str(useridnew) + ":" + str(userpwnew)
                
            
def Choperro():
    rekey = ""
    while 1:
        try:
            socket.setdefaulttimeout(120)
            #PROXY = proxy
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument('--proxy-server=%s' % PROXY)
            #chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(chrome_options=chrome_options)
            #driver.set_window_position(0, 0)
            #driver.set_window_size(0, 0)
            url="https://accgen.cathook.club/"
            driver.get(url)
            time.sleep(2)
            #email = data.split(":")[0]
            #password = data.split(":")[1]
            #email_f = driver.find_element_by_id('email')
            #email_f.send_keys(email)
            #pw_f = driver.find_element_by_id('password')
            #pw_f.send_keys(password)
            mainWin = driver.current_window_handle
            driver.find_element_by_xpath("//button[@id='generate_button']").click()
            driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
            time.sleep(1)
            #gangnam = driver.find_element_by_xpath("//input[@id='recaptcha-token']")
            getcodeurl = "http://2captcha.com/in.php?key="+ str(rekey) +"&method=userrecaptcha&googlekey=6Leuh5EUAAAAALediEIgey5dKbm1_P97zvzxjgvC&pageurl=https://accgen.cathook.club&invisible=1"
            testcode = urllib2.urlopen(getcodeurl).read()
            gc_IDex = testcode.split("|")
            gc_ID = gc_IDex[1]
            time.sleep(5)
            resurl = "http://2captcha.com/res.php?key="+ str(rekey) +"&action=get&id=" + str(gc_ID)
            contents = urllib2.urlopen(resurl).read()
            while "CAPCHA_NOT_READY" in contents:
                time.sleep(2)
                contents = urllib2.urlopen(resurl).read()
            #print "contents: " + str(contents)
            link = contents.split("|")
            #print "link: " + str(link)
            googleresolved = link[1]
            driver.switch_to_window(mainWin)
            #gre = driver.find_element_by_xpath("//textarea[@name='g-recaptcha-response']")
            #gre.send_keys(googleresolved)
            #print(googleresolved)
            driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='"+ str(googleresolved) + "'")
            driver.execute_script("on_captcha_valid('{}')".format(googleresolved))
            delay = 4
            time.sleep(15)
            #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'acc_login')))
            source_code = driver.page_source
            while "acc_login" not in driver.page_source:
                time.sleep(1)
                
            
            if "Login: " in source_code:
                userid = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
                #userid = driver.get_element_by_xpath("//h6[@id='acc_login']/strong")
                userpw = driver.find_element_by_xpath("//h6[@id='acc_pass']/strong").text
                if len(userid) > 3:
                    f= open("accs.txt","a+")
                    f.write(str(userid) + ":" + str(userpw) + "\n")
                    f.close()
                #print str(useridnew) + ":" + str(userpwnew)
                print str(userid) + ":" + str(userpw)
                ##########################
                while 1:
                    userid = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
                    driver.find_element_by_xpath("//button[@id='generate_button']").click()
                    time.sleep(2)
                    useridnew = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
                    if userid == useridnew:
                        driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
                        time.sleep(1)
                        #gangnam = driver.find_element_by_xpath("//input[@id='recaptcha-token']")
                        getcodeurl = "http://2captcha.com/in.php?key="+ str(rekey) +"&method=userrecaptcha&googlekey=6Leuh5EUAAAAALediEIgey5dKbm1_P97zvzxjgvC&pageurl=https://accgen.cathook.club&invisible=1"
                        testcode = urllib2.urlopen(getcodeurl).read()
                        gc_IDex = testcode.split("|")
                        gc_ID = gc_IDex[1]
                        time.sleep(15)
                        resurl = "http://2captcha.com/res.php?key="+ str(rekey) +"&action=get&id=" + str(gc_ID)
                        contents = urllib2.urlopen(resurl).read()
                        while "CAPCHA_NOT_READY" in contents:
                            time.sleep(2)
                            contents = urllib2.urlopen(resurl).read()
                        #print "contents: " + str(contents)
                        link = contents.split("|")
                        #print "link: " + str(link)
                        googleresolved = link[1]
                        driver.switch_to_window(mainWin)
                        #gre = driver.find_element_by_xpath("//textarea[@name='g-recaptcha-response']")
                        #gre.send_keys(googleresolved)
                        #print(googleresolved)
                        driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='"+ str(googleresolved) + "'")
                        driver.execute_script("on_captcha_valid('{}')".format(googleresolved))
                        delay = 3
                        #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'acc_login')))
                        time.sleep(10)
                        source_code = driver.page_source
                        while "acc_login" not in driver.page_source:
                            time.sleep(1)


                        source_code = driver.page_source
                        useridnew = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
                        if useridnew is not userid:
                            if len(useridnew) > 3:
                                userpwnew = driver.find_element_by_xpath("//h6[@id='acc_pass']/strong").text
                                f= open("accs.txt","a+")
                                f.write(str(useridnew) + ":" + str(userpwnew) + "\n")
                                f.close()
                                print str(useridnew) + ":" + str(userpwnew)
                    else:
                        useridnew = driver.find_element_by_xpath("//h6[@id='acc_login']/strong").text
                        userpwnew = driver.find_element_by_xpath("//h6[@id='acc_pass']/strong").text
                        print str(useridnew) + ":" + str(userpwnew)
                        if len(useridnew) > 3:
                            #userpwnew = driver.find_element_by_xpath("//h6[@id='acc_pass']/strong").text
                            f= open("accs.txt","a+")
                            f.write(str(useridnew) + ":" + str(userpwnew) + "\n")
                            f.close()
                #zf = threading.current_thread()
                
                #StoppableThread.stop()
            else:
                #print "acc not working" + data
                zf = threading.current_thread()
                #StoppableThread.stop()
            #print gangnam.get_attribute('value')
        except Exception as e:
            driver.quit()
            exc_type, exc_obj, exc_tb = sys.exc_info()
            #print("excepted, retrying" + str(e) + " line number: " + str(exc_tb.tb_lineno))
            #driver.quit()
            #checkacc(data,proxy)
            print(e)
z=0
thr = []
pagg = ["111.11.111.11:8085","100.90.100.100:8085"]
while True:
    atn = threading.active_count()
    #acctocheck = main_accs[z]
    if atn<15:
        #manpag = pagg[z]
        thr.append(threading.Thread(target=Choperro))
        thr[z].start()
        
    
        #print atn
        #print(acctocheck)
    #    thr.append(threading.Thread(target=checkaccs, args=(acctocheck,)))
    #    thr[z].start()
     #   z = z+1
    else:
        atn = threading.active_count()
        continue
    z = z+1


#checkacc("testtest:sdjbasj","127.0.0.1:9191")
