from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from random import randrange
import codecs
import os
import time
import sys
import pickle
# import winsound

mincm = int(sys.argv[1])
maxcm = int(sys.argv[2])

class accd:
    def __init__(self, username, target, div):
        self.username = username
        self.target = target
        self.ban = 5
        self.max = randrange(mincm, maxcm)
        self.xpid = "/html/body/div["+str(div)+"]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a"
        self.xplike = "/html/body/div["+str(div)+"]/div[2]/div/article/div[3]/section[1]/span[1]/button"
        self.xpcomment = "/html/body/div["+str(div)+"]/div[2]/div/article/div[3]/section[3]/div/form"
        self.xpcommentext = "/html/body/div["+str(div)+"]/div[2]/div/article/div[3]/section[3]/div/form/textarea"
        self.xpcommentsend = "/html/body/div["+str(div)+"]/div[2]/div/article/div[3]/section[3]/div/form/button"
        self.xpcommentcheck = "/html/body/div["+str(div)+"]/div[2]/div/article/div[3]"

info = accd(0, 0, 5)

tfp = "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]"


# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference('permissions.default.image', 2)
# browser = webdriver.Firefox(firefox_profile=firefox_profile)

# firefox_profile = webdriver.FirefoxProfile()
# firefox_profile.set_preference('permissions.default.image', 2)
# options = Options()
# options.add_argument("--headless")
# browser = webdriver.Firefox(firefox_options=options, firefox_profile=firefox_profile)

opti = ""

if sys.argv[6] == "1":
    opti = "--headless"
    print(">>>>>>>>Headless<<<<<<<<  \n", opti)

options = Options()
options.add_argument(opti)
browser = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr", firefox_options=options)

browser.implicitly_wait(4)
count = randrange(0, 36)

accfl = sys.argv[3]
plus = int(sys.argv[4])
targ = sys.argv[5]
logf = "stats/log"
print("the plus is ",plus)
acccount = 0
to = 0
with open(accfl, 'r') as f:
    for line in f:
        to += 1
targetsnumber = 0
with open(targ, 'r') as f:
    for line in f:
        targetsnumber += 1

print(f"total targers are ",targetsnumber)
print(mincm)
print(maxcm)
print(accfl)
print("max acc is")
print(to)

def dataoff():
    os.system('adb shell sh /storage/EA5D-2D07/dataoff.sh')
    sleep(20)

def dataon():
    os.system('adb shell sh /storage/EA5D-2D07/dataon.sh')
    sleep(30)
    os.system('adb shell ip -4 addr show rmnet0')




def likeandcomment(cfile, count):
    a = count%25
    b = randrange(0, 2)
    try:
        browser.find_element_by_xpath(info.xplike).click()
        sleep(2 + b)
        browser.find_element_by_xpath(info.xpcomment).click()
        sleep(1)
        print("clicked")
        browser.find_element_by_xpath(info.xpcommentext).send_keys(cfile[a])
        sleep(1.5)
        browser.find_element_by_xpath(info.xpcommentsend).click()
        sleep(4 + b)
    except:
        print("likedchs")

def next(count):
    if count != 0:
        try:
            browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
            count = count+1
        except:
            print("next")
    else:
        try:
            browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
            count = count+1
        except:
            print("next")
    return(count)

def previous(count):
    if count != 0:
        try:
            browser.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[1]").click()
            count = count-1
        except:
            print("previous")
    return(count)

def cachefile(file):
    print(file," loaded")
    f= open(file,"r", encoding="UTF-8")
    return(f.readlines())

def cacheids(file):
    print("ids handler")
    f= open(file,"w")
    return(f)


def disconnect(info):
    usernamep = info.username.replace('\n','')
    cname = "botc/"+usernamep
    pickle.dump( browser.get_cookies() , open(cname,"wb"))
    # browser.get(info.profile)
    # sleep(1)
    # try:
    #     browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button").click()
    #     sleep(1)
    #     browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div/button[9]").click()
    #     sleep(7)
    # except:
    #     print("disconnected")
    sleep(0.1)

def signin(info):
    browser.get('https://www.instagram.com/')
    username = info.username.replace('\n','')
    cname = "botc/"+username
    cookies = pickle.load(open(cname, "rb"))
    sleep(2)
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get('https://www.instagram.com/')
    # uid = browser.find_element_by_css_selector("input[name='username']")
    # uid.click()
    # uid.send_keys(info.username)
    # sleep(1)
    # pswd = browser.find_element_by_css_selector("input[name='password']")
    # pswd.click()
    # sleep(1)
    # pswd.send_keys(info.password)
    # sleep(1)
    # btn = browser.find_element_by_xpath("//button[@type='submit']")
    # btn.click()
    # sleep(4)
    browser.get(info.target)
    sleep(3)
    try:
        browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()
    except:
        print("Its not a hashtag")
        # browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/a[3]").click()
        # sleep(5)
        browser.find_element_by_xpath(tfp).click()
  
def loadacc(afile, tfile):
    h = 1
    a = acccount
    while (1):
        if a == to:
            browser.close()
            exit()
        username = afile[a]
        filenamen = str(username)
        filenameb = filenamen.replace('\n', '')
        filenameb = "acc/"+filenameb+".txt"
        msgb = open(filenameb, "r+")
        a += 1
        targetn = int(afile[a]) + plus
        targetn = int(targetn) % int(targetsnumber)
        target = tfile[targetn - 1]
        info = accd(username, target, 5)
        h = msgb.read(5)
        msgb.close()
        a += 1
        print("H is ", h)
        print("at >>", username)
        if h == "0":
            break
    signin(info)
    return(info)

def fixdiv(info):
    sleep(3)
    info = accd(info.username, info.target, 5)
    try:
        browser.find_element_by_xpath(info.xpid).get_attribute("href")
    except:
        info = accd(info.username, info.target, 4)
        print("error id")
    finally:
        print("no error")
    print("Div fixed")
    return(info)

def reloadtn(info):
    sleep(3)
    try:
        postid = browser.find_element_by_xpath(info.xpid).get_attribute("href")
    except:
        print("error id")
        browser.find_element_by_xpath("/html").send_keys(u'\ue012')
        sleep(5)
        browser.find_element_by_xpath("/html").send_keys(u'\ue012')
        sleep(5)
        browser.find_element_by_xpath("/html").send_keys(u'\ue014')
        sleep(8)
        browser.find_element_by_xpath("/html").send_keys(u'\ue014')
        sleep(8)
        postid = browser.find_element_by_xpath(info.xpid).get_attribute("href")
    finally:
        print("got the id")
    print(info.username)
    print(info.target)
    print(postid)
    return(postid)

def reloadt(info):
    browser.get(info.target)
    sleep(6)
    try:
        browser.find_element_by_xpath(tfp).click()
        sleep(3)
    except:
        browser.find_element_by_xpath(tfp).click()
    sleep(5)
    try:
        postid = browser.find_element_by_xpath(info.xpid).get_attribute("href")
    except:
        print("error id")
        browser.get(info.target)
        sleep(5)
        browser.find_element_by_xpath(tfp).click()
        sleep(3)
        postid = browser.find_element_by_xpath(info.xpid).get_attribute("href")
    finally:
        print("got the id")
    print(info.username)
    print(info.target)
    print(postid)
    return(postid)

def getalt():
    print("im in !!!!")
    i = 0
    altv="test"
    try:
        altv = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/div[1]/img").get_attribute("alt")
    except:
        altv = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/div[1]/img").get_attribute("alt")
    finally:
        print(altv)
    if altv.find("personne"):
        print("ppl found")
        i = 1
    if altv.find("personnes"):
        print("ppls found")
        i = 2
    return(i)

def quitp(info):
    disconnect(info)
    browser.close()

def check():
    print("checking likes")
    classe = "NULL"
    try:
        classe = browser.find_element_by_xpath(info.xpid).get_attribute("title")
    except:
        print("notfound")
        return(1)
    finally:
        if classe != "NULL":
            print(" found")
            return(0)

def check2():
    print("search comments")
    cm = browser.find_element_by_xpath(info.xpcommentcheck).text
    # print(cm)
    if "vovim" in str(cm) or "hannahmartin*" in str(cm) or "vootty" in str(cm) or "Rabat" in str(cm) or "india" in str(cm) or "amartina" in str(cm) or "pitpethouse" in str(cm):
        print("found in comments")
        return(0)
    else:
        return(1)

def testban(x):
    ban = "NULL"
    ban = "NULL"
    try:
        ban = browser.find_element_by_xpath("/html/body/div[2]/div/div/button")
    except:
        try:
            ban = browser.find_element_by_xpath("/html/body/div[3]/div/div/button")
        except:
            try:
                ban = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/button[2]")
            except:
                print("not banned")
                return(x)
    finally:
        if ban != "NULL":
            print(info.username)
            print("BANNED !!!")
            filenamen = str(info.username)
            filename = filenamen.replace('\n', '')
            fileac = "acc/"+filename+".txt"
            msgb = open(fileac, "r+")
            msgb.truncate(0)
            msgb.write("1")
            msgb.close
            logfd = open(logf, "a+")
            t = time.localtime()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
            logfd.write(current_time)
            logfd.write(fileac)
            logfd.write(" is banned")
            logfd.write('\n')
            logfd.close
            # winsound.Beep(frequency, duration)
            sleep(0.5)
            # winsound.Beep(frequency, duration)
            sleep(0.5)
            # winsound.Beep(frequency, duration)
            return(2)

likecount = 0
maxretry = randrange(25, 55)
tfile = cachefile(targ)
cfilee = cachefile("cmt.txt")
cfile = [i.replace('\n','') for i in cfilee]
afile = cachefile(accfl)
ids = open("ids.txt","r+", encoding="UTF-8")
tem = ids.readlines()
ids.close()
temp = [i.replace('\n','') for i in tem]
# print("+*+*+*+*+*+*+*+*\n")
# print(temp)
# print("+*+*+*+*+*+*+*+*\n")
info = loadacc(afile, tfile)

filenamen = str(info.username)
filenameb = filenamen.replace('\n', '')
filenameb = "acc/"+filenameb+".txt"
print(filenameb)
msgb = open(filenameb, "r+")
msgbc = msgb.read(5)
print("*****************>>>>", msgbc)
info.ban = msgbc
print(";o;;o;o;o; this is the content")
print(info.ban)
msgb.close

info = fixdiv(info)
postid = reloadtn(info)
i = 0
j = 0
x = 1
x2 = 1
y = 0
switched = 0
while 1:

    print("y is : ", y)
    print(info.max)
    ids = open("ids.txt","a+")
    x = 1
    sleep(1)
    # print("-/-/-//-/-/-/-/-/-/-/  ")
    # print(filename)
    # print("-*-*-*-*-*-*-*-*-*-*-*")
    # stats = open(filename, "a+")
    # print(stats)
    # stats.close()
    if info.ban == "1":
        y = maxretry
        plus -= 1
    if i == info.max or y == maxretry:
        filenamen = str(info.target)
        filename = filenamen.split('/', 5)[3]
        if (filename == "explore"):
            filename = filenamen.split('/', 6)[5]+"-tag"
        filename = "stats/"+filename+".txt"
        stats = open(filename, "a+")
        t = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
        stats.write(current_time)
        stats.write(" : ")
        stats.write(info.username)
        stats.write(" : ")
        stats.write(str(i))
        stats.write("\n")
        stats.close()
        disconnect(info)
        sleep(300)
        acccount += 2
        if acccount == to:
            quitp(info)
            break
        # dataoff()
        # print("-----------------------changing ip----------------------")
        # dataon()
        echec = 0
        sleep(15)
        info = loadacc(afile, tfile)
        info = fixdiv(info)
        i = 0
        y = 0
        filenamen = str(info.username)
        filenameb = filenamen.replace('\n', '')
        filenameb = "acc/"+filenameb+".txt"
        print(filenameb)
        msgb = open(filenameb, "r+")
        msgbc = msgb.read(5)
        print("*****************>>>>", msgbc)
        info.ban = msgbc
        print(";o;;o;o;o; this is the content")
        print(info.ban)
        msgb.close
        switched = 1
        count = randrange(0, 28)
    # alt = getalt()
    print("///////////////////////////Switched is ", switched)
    if switched == 0:
        postnow = reloadtn(info)
        print("reloaded")
        # print("-*-*-*-*-*-*-*-*\n", temp,"\n-*-*-*-*-*-**")
        # x = check()
        x = 1
        x2 = check2()
        if postnow in temp:
            x = 0
            print("-------------------------------------------already liked")
            y += 1
            print("next")
            browser.find_element_by_xpath("/html").send_keys(u'\ue014')
        postid = postnow
        if postid not in temp:
            print("****Not FouNd*****")
            temp.append(postid)
            ids.write(postid)
            ids.write('\n')
            print("****Added to temp*****")
        if x == 1 and x2 == 1:
            # if alt != 0:
            print("****Not LiKed doing it now*****")
            likeandcomment(cfile, count)
            x = testban(x)
            if x == 2:
                likecount -= 1
                y = maxretry
                x = 0
            likecount = likecount+1
            sleep(1)
            print("total sesion likes is : ",likecount)
            postid = postnow
            i += 1
            print("next")
            browser.find_element_by_xpath("/html").send_keys(u'\ue014')
            # sleep(3)
            count = randrange(0, 28)
    switched = 0
    ids.close()
    sleep(0.5)
browser.quit()
exit()