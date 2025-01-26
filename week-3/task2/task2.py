import urllib.request as req
import bs4

def getTitleInfo(titleURL):
    request = req.Request(titleURL, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")

    like = root.find_all("span", string="推 ")
    dislike = root.find_all("span", string="噓 ")
    LikeSubtractDislike = len(like)-len(dislike)

    articleTime = root.find_all("span", class_="article-meta-value")
    articleTime = list(articleTime)
    if len(articleTime) > 3:
        time = articleTime[3].string
    else:
        time = "無法取得文章時間"
    return {"LikeSubtractDislike": LikeSubtractDislike, "time": time }


def getData(url):      
    #建立一個Request物件，附加 Request Headers 的資訊
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") #列表型態
    with open("article.csv", "a", encoding="utf-8") as file:
        for title in titles:
            if title.a != None:
                titleText = title.a.string
                eachTitlePageURL = "https://www.ptt.cc" + title.a["href"]
                # print(eachTitlePageURL)
                result = getTitleInfo(eachTitlePageURL)
                
                final = f"{titleText},{result["LikeSubtractDislike"]},{result["time"]}"+"\n"
                file.write(final)
            

    nextLink = root.find("a", string="‹ 上頁") #尋找內文是‹ 上頁的a標籤
    return nextLink["href"]

pageURL ="https://www.ptt.cc/bbs/Lottery/index.html"
count = 0
while count <3:
    pageURL ="https://www.ptt.cc" + getData(pageURL)
    count+=1