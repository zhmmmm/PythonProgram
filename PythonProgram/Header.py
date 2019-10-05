
list = []
num = 1000
def recursion(var):
    list.append(var)
    if(var ==0):
        num = 1
        print(list)
        return;
    recursion(var - 1)

def GetNum():
    return 10086

#import requests

url = "https://www.bilibili.com/video/av55350377?from=search&seid=13783158102611648125"

def Main():
    #text = requests.get(url).text
    pass
