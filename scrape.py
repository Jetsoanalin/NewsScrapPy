import requests
from bs4 import BeautifulSoup
import pandas as pd

def storedata(soup):
    for data in soup.findAll("div",{"class":"news-card z-depth-1"}):
        #print(dict["headlines"],data.find(itemprop="headline").getText())
        if data.find(itemprop="headline").getText() not in dict["headlines"]:
            #print(data.find(itemprop="headline").getText(),dict["headlines"].index(data.find(itemprop="headline").getText()))
            dict["headlines"].append(data.find(itemprop="headline").getText())
            dict["text"].append(data.find(itemprop="articleBody").getText())
            dict["date"].append(data.find("span",{"clas":"date"}).getText())
            dict["author"].append(data.find("span",{"class":"author"}).getText())
            if data.find("a",{"class":"source"}):
                dict["read_more"].append(data.find("a",{"class":"source"}).get("href"))
            else:
                dict["read_more"].append("None")
    #print(len(dict["headlines"]))
url="https://www.inshorts.com/en/read"
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'referer': 'https://inshorts.com/en/read',
        'origin': 'https://inshorts.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
    }
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.content,"lxml")
dict={"headlines":[],"text":[],"date":[],"author":[],"read_more":[]}
storedata(soup)
#Start Ajaxing
start_id=soup.findAll("script",{"type":"text/javascript"})[-1].getText().split()[3].strip(";").strip('"')
for i in range(1000):
    print(i,len(dict["headlines"]),start_id)
    ajax_url="https://inshorts.com/en/ajax/more_news"
    payload={"news_offset":start_id,"categopry":""}
    #print(payload)
    try:
        r=requests.post(ajax_url,payload,headers=headers)
        start_id=r.content.decode("utf-8")[16:26]
        soup=BeautifulSoup(r.text.replace('\\',""),"lxml")
        storedata(soup)
    except:
        pass
    if i%100==0:
        df = pd.DataFrame(dict)
        df.to_csv("data"+str(i/1000)+".csv", index=False)
        dict = {"headlines": [], "text": [], "date": [], "author": [], "read_more": []}