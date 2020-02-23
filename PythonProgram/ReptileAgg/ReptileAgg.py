import os;
import requests;
import re;
import time;



#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#获取图片的URL
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
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#截取部分字符串 " 到 "
def getCustom(url):
    strs = ""
    types = ""
    index = 0
    state = 0
    for v in url:
        if(v == '"'):
            if(state == 1): break;
            state = 1
        if(state == 1 and url[index + 1] != '"'):
            strs = strs + url[index + 1]

        index = index + 1

    types = types + strs[len(strs) - 3]
    types = types + strs[len(strs) - 2]
    types = types + strs[len(strs) - 1]
    return strs,types;

#///////////////////////////////////////////////////////////////////////////////////////////////////////////
#文件名 图片的url 请求头
def saveImgUrl(filename,url, head):
    ret = requests.get(url,headers = head)
    if ret.status_code == 404:
        print("404")
        return 404;
    file = open(filename,"wb")
    file.write(ret.content)
    file.close()
    print("save image ok !!!")
#///////////////////////////////////////////////////////////////////////////////////////////////////////////
################http://www.mmonly.cc/mmtp/
def www_mmonly_com(url,page,head,isOpen,filedir):
    i = 0;
    count = 1;
    while i < page:
        if i == 0:
            URL  = url + ".html"
        else:
            URL  = url + "_" + str(i + 1) + ".html"
        print(URL)
        response = requests.get(URL,headers = head)
        if response.status_code == 404:
            print("存在反爬措施,请仔细检查！！！")
            return 404
        response.encoding = response.apparent_encoding
        #file = open("pars.xml","wb")
        #file.write(response.content)
        if isOpen == True:
            os.system("notepad pars.xml")
        ImgURL = re.findall('<img alt=".*?" .*?>', response.text)
        print(ImgURL[0])
        i = i + 1
        time.sleep(1);
        Break = 0
        for v in ImgURL:
            Break = Break + 1
            time.sleep(1);
            image,types = getImgUrl(v)
            ret = saveImgUrl(filedir + str(count) + "." + types,image,head)
            if ret == 404:
                print("存在反爬措施,请仔细检查！！！")
                return 404
            count = count + 1;
            if Break == 1:
                break;

    return 0;
################https://www.showmeizi.com/detail/2623
def www_showmeizi_com(filename,url,head):
    response = requests.get(url,headers = head)
    if response.status_code == 404:
        print("404")
        return 404;
    response.encoding = response.apparent_encoding
    ImgURL = re.findall('<img .*? class="swiper-lazy">', response.text)
    strs = ""
    types = ""
    count = 0
    for v in ImgURL:
        strs,types = getCustom(v)
        saveImgUrl(filename + str(count) + "." + types,"https://www.showmeizi.com" + strs,head)
        count = count + 1
        time.sleep(1)

    return 0;
def www_showmeizi_coms(filename,url,head,flag):
    response = requests.get(url,headers = head)
    if response.status_code == 404:
        print("404")
        return 404;
    response.encoding = response.apparent_encoding
    ImgURL = re.findall('<img .*? class="swiper-lazy">', response.text)
    strs = ""
    types = ""
    count = 0
    for v in ImgURL:
        strs,types = getCustom(v)
        saveImgUrl(filename + str(count) + flag + "." + types,"https://www.showmeizi.com" + strs,head)
        count = count + 1
        time.sleep(1)

    return 0;



if __name__ == "__main__":
    os.system("color 2");
    print("python main");

    header = {
        #qq游览器请求头
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2843.400'
        #谷歌游览器请求头
            #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }


    url = "http://www.mmonly.cc/mmtp/ctmn/295392";
    www_mmonly_com(url,14,header,False, "D:/Material/www_mmonly_com/12/")

    #url = "https://www.showmeizi.com/detail/2144"
    #www_showmeizi_com("D:/Material/SoftPorn/www_showmeizi_com/2/",url,header)

    #page = 2
    #url = { }
    ##url[0] = "https://www.showmeizi.com/detail/782"
    #url[0] = "https://www.showmeizi.com/detail/559"
    ##url[2] = "https://www.showmeizi.com/detail/541"
    ##url[3] = "https://www.showmeizi.com/detail/559"
    ##url[4] = "https://www.showmeizi.com/detail/577"
    ##url[5] = "https://www.showmeizi.com/detail/558"
    ##url[6] = "https://www.showmeizi.com/detail/578"
    ##url[7] = "https://www.showmeizi.com/detail/538"
    ##url[8] = "https://www.showmeizi.com/detail/725"
    ##url[9] = "https://www.showmeizi.com/detail/782"
    #i = 0
    #flag = 0
    #while i < 10:
    #    time.sleep(1)
    #    www_showmeizi_coms("D:/Material/SoftPorn/www_showmeizi_com/3/",url[i],header,str(flag))
    #    flag = flag + 1
    #    i = i + 1

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! GAME OVER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    #============================================================






