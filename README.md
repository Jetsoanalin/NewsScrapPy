# Inshorts News Scrapping Python Script


## What will the script Fetch ?

- Headline
- Description
- Date
- Author
- Source (If any)

## How to run it ?

Open CMD / Terminal after going to the folder and type the following command
```console
python3 scrape.py
```
Simple ? Thats it , now let the script do its work for you 

## Want more data ?
```python
for i in range(1000): #Increase the range to your desired result
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
    if i%100==0: #When 100 result in reached in one file it will create a new .csv file and start saving data there 
        df = pd.DataFrame(dict)
        df.to_csv("data"+str(i/100)+".csv", index=False)
        dict = {"headlines": [], "text": [], "date": [], "author": [], "read_more": []}
```


# Enjoy ! Chears 🍻
