from playsound import playsound
from bs4 import BeautifulSoup
import requests as rq
from time import sleep

r = rq.get('http://oidb.ankara.edu.tr/')
source = BeautifulSoup(r.content, "html.parser")
titles = source.find("div",{"class":"fusion-recent-posts fusion-recent-posts-1 avada-container layout-date-on-side layout-columns-1"})

titlesList = titles.find_all("a")

while True:
    
    for each in titlesList:
        # print(each.text+"\n")
        if ("ek madde" in each.text.lower()) or ("merkez" in each.text.lower()):
            playsound("sound/alarm.wav")
            break

    sleep(300)
    
# div class="fusion-recent-posts fusion-recent-posts-1 avada-container layout-date-on-side layout-columns-1"

