
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