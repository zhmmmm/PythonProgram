import requests
import os
os.system("color 2")
from lxml import etree
import re
import time
import urllib3
import urllib
import urllib.parse


def p():
    print("function")
        #url = "https://www.cnblogs.com/YZFHKMS-X/gallery/1575130.html"
    url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CE%A8%C3%C0%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CE%A8%C3%C0%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111',
        'Cookie': 'HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaMMzY0i9qXJ9ATcu3rvxFIc-a7KI9byBcYk%7EjBVmPGIbL3LTKKJ2D17mh5VfJ5yjlCncAb2yhPI5sZM51Qo7tpCemygM0VNUzuTBJwYF8OYmi3nsCCzbpo5U9tLSzkZfcQ1rxUcJSzaipThg__; HISTORY=fec845b215cd8e8be424cf320de232722d0050; PTOKEN=ff58b208cc3c16596889e0a20833991d; STOKEN=1b1f4b028b5a4415aa1dd9794ff061d312ad2a822d52418f3f1ffabbc0ac6142; SAVEUSERID=0868a2b4c9d166dc85e605f0dfd153; USERNAMETYPE=3; PSTM=1454309602; BAIDUID=E5493FD55CFE5424BA25B1996943B3B6:FG=1; BIDUPSID=B7D6D9EFA208B7B8C7CB6EF8F827BD4E; BDUSS=VSeFB6UXBmRWc3UEdFeXhKOFRvQm4ySmVmTkVEN2N0bldnM2o5RHdyaE54ZDlXQVFBQUFBJCQAAAAAAAAAAAEAAABzhCtU3Mbj5cfl0e8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE04uFZNOLhWZW; H_PS_PSSID=1447_18282_17946_18205_18559_17001_17073_15479_12166_18086_10634; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm',
    }


    res = requests.get(url, headers=headers)
    #res = requests.get(url)
    print(res.request.headers)
    print(res)
    html = res.text
    print("###############################################################")
    urls = re.findall('<img src=.*? alt=""/>',html)
    print(urls)

    i = 0
    for web in urls:
        pass
        #1秒
        #time.sleep(1)
        #print("###############################################################")
        #filename = web.split(' ')
        #print(filename[1].split('src="')[1].rstrip('"'))
        #filename = filename[1].split('src="')[1].rstrip('"')

        #resp = requests.get(filename)
        #with open("image"+str(i)+".jpg","wb") as file:
        #    file.write(resp.content)
        #i = i + 1

#url 编码
def parse_decode(url):
    ret = urllib.parse.quote(url)
    return ret
#url 解码
def parse_encode(url):
    ret = urllib.parse.unquote(url)
    return ret

def getImgUrl(url):
    urls = ""
    index = 0
    Is = False
    j = 0
    types = ""
    for i in url:
        if i == 'h':
            if url[index + 1] == 't' and url[index + 2] == 't' and url[index + 3] == 'p':
                Is = True
        if Is == True:
            if url[index] == '"':
                break
            urls = urls + url[index]
        index = index + 1
    types = types + urls[len(urls) - 3]
    types = types + urls[len(urls) - 2]
    types = types + urls[len(urls) - 1]

    return urls,types
def saveImgUrl(filename,url):
    header = {
        #qq游览器请求头
            #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400'
        #谷歌游览器请求头
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
    ret = requests.get(url,headers = header)
    file = open(filename,"wb")
    file.write(ret.content)
    file.close()
    print("ok")

if __name__ == "__main__":

    url = "https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CE%A8%C3%C0%CD%BC%C6%AC&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111"
    url = "https://www.mzitu.com/211558"#https://www.mzitu.com/211558/1 ~ 49

    url = "http://2019eee.xyz/?m=pic_list*25*3"
    headers = {
        #qq游览器请求头
            #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400'
        #谷歌游览器请求头
            #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
            'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        }
    response = requests.get(url,headers = headers)

    #解决乱码
    #response.encoding = response.apparent_encoding
    #imgurl = re.findall('<img .*?/>',html)

    url = "http://2019eee.xyz/?m=pic_list*25*"
    j = 3
    count = 0
    #下载页gif
    while j < 100:
        url = url + str(j)
        response = requests.get(url,headers = headers)
        imgurl = re.findall('<a class="stui-vodlist__thumb lazyload" .*?>',response.text)
        image = "image/image_0"
        for i in imgurl:
            time.sleep(1)
            img,types = getImgUrl(i)
            saveImgUrl(image + str(count) + "."+ types,img)
            count = count + 1
        j = j + 1

    #imgurl = re.findall('<a class="stui-vodlist__thumb lazyload" .*?>',response.text)
    #image = "image/image"
    #count = 0
    #for i in imgurl:
    #    time.sleep(1)
    #    img,types = getImgUrl(i)
    #    saveImgUrl(image + str(count) + "."+ types,img)
    #    count = count + 1






