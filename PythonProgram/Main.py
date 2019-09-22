#print("Hello World!")
#name = "nihfjkds"
age = 454
num1 = 1
num2 = 2
#print(name)
#print(age)
#print("%d",age)

#Numbers（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Dictionary（字典）
#int（有符号整型）
#long（长整型[也可以代表八进制和十六进制]）
#float（浮点型）
#complex（复数

##Python 注重缩进  漂亮
if True :
   print("你好")
   print("fds")

if (age == 454 and num1 == 1 or num2 == 2):
    print("false")
if not(False):
    print("notfalse")


var1 = 1
var = 10
print(var1)
del var1
del var

string = "Hello Wrold"
#print(string)
#print(string[2:5])
#print(string[0])
#输出字符串两次
#print(string * 2)
#print(string + "test")

Str = string + " fjsdkjfl";
print(Str)
str1 = "0123456789"
print(str1[1:6:4])

List = ["1","2","3","4"]
print(List,List[2])

student = [19,18,"name"]
print(student)
student[1] = 100
print(student)


Tuple = ("fsd","2",54)
print(Tuple[0])
print(Tuple[0] + "44564")

Dict = { }
Dict["age"] = 18
Dict["name"] = "你好"
Dict[3] = 1000
Dict[0] = 10086

print(Dict)
print(Dict["age"])
print(Dict[0])

print(int(Dict["age"]))

print(3141//121)
print(2**10)

var2 = 100
var2 += 10086
print(var2)

print(var2 << 1)

#in
#not in
a = 10
b = 100
List = [1,2,3,10,100]
print(a in List)

#is 
#not is
#身份运算符用于比较两个对象的存储单元

print(a is b)#False
b = 10
print(a is b)#True

a = 1
b = 2
c = 3

if a == 2:
    print("a == 2")
else:
    print("a != 2")

a = 1
while a <= 100:
    if a % 2 == 0:
        print(a)
    a += 1

Lists = { }
i = 0
while i < 10:
    Lists[str(i)] = i;
    i += 1

while i < 10:
    print(Lists[str(i)])

a = 6
if a == 1:
    print("a == 1")
elif a == 2:
    print("a == 2")
elif a == 3:
    print("a == 3")
else:
    print("a != 1 and a != 2 and a != 3")

print("=========================")

i = 0
while i < 50:
    i += 1
    if i == 30:
        #continue
        break
print(i)

i = 0
if i == 0:
     print(i)
else:
   pass #不做任何事情，一般用做占位语句。

List = [5,9,6,7,5,6,3,5]
print(List)
i = 0

print(len(List))
lenght = len(List)

while i < lenght - 1:
    j = i + 1
    while j < lenght:
        I = List[i]
        J = List[j]
        if I > J:
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
        j += 1
    i += 1
print(List)

for value in List:
    print(value)

for value in "abcdefj":
    print(value)

for index in range(lenght):
    print("List ",List[index])

List = [5,9,6,7,1,6,3,2]

#int(x [,base ])         将x转换为一个整数  
#long(x [,base ])        将x转换为一个长整数  
#float(x )               将x转换到一个浮点数  
#complex(real [,imag ])  创建一个复数  
#str(x )                 将对象 x 转换为字符串  
#repr(x )                将对象 x 转换为表达式字符串  
#eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
#tuple(s )               将序列 s 转换为一个元组  
#list(s )                将序列 s 转换为一个列表  
#chr(x )                 将一个整数转换为一个字符  
#unichr(x )              将一个整数转换为Unicode字符  
#ord(x )                 将一个字符转换为它的整数值  
#hex(x )                 将一个整数转换为一个十六进制字符串  
#oct(x )                 将一个整数转换为一个八进制字符串  

import math
import cmath
import random



print(random.random())
print(random.randint(1,100) )
print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]               
random.shuffle(a) # 将序列a中的元素顺序打乱
print(a)

var1 = 'Hello World'
var2 = 'Python Runoob'

print(var1,var1[0])
print(var2,var2[0])
#从0开始截取6个字符再连接字符
print(var1[:6] + ' 123456')
str1 = "0123456789"
#从第1开始截取6个 在从这六个中截取第4个字符
print(str1[1:6:4])
#字符串
#print("\a") sound
print("字符串"+"连接")
print("%d 和附近的" % (454))
print ("My name is %s and weight is %d kg!" % ('Zara', 21))

 #%c	 格式化字符及其ASCII码
#%s	 格式化字符串
#%d	 格式化整数
#%u	 格式化无符号整型
#%o	 格式化无符号八进制数
#%x	 格式化无符号十六进制数
#%X	 格式化无符号十六进制数（大写）
#%f	 格式化浮点数字，可指定小数点后的精度
#%e	 用科学计数法格式化浮点数
#%E	 作用同%e，用科学计数法格式化浮点数
#%g	 %f和%e的简写
#%G	 %F 和 %E 的简写
#%p	 用十六进制数格式化变量的地址

#三引号
hi = ' '' ''fds'
print(hi)
hi = ' ''\n''fds'
print(hi)
#unicode字符串
print(u"fsdkjflkjdsl")

k = "fjksdj{d}".format(d = 76788)
print(k)
k = "fjksdj{str}".format(str = 123324)
print(k)
if('f' in k):
    pass
    print("yes")
else:
    pass
    print("no")

Str = "123456789"
print(Str)
len = len(Str)
print(len)
for value in Str:
    print(value)

#字符串逆序
m = list(Str)
m.reverse()
for letter in m:
    print(letter)

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print("list1[0]: ", list1[0])
#从list2中截取从1到4下标的值
print("list2[1:5]: ", list2[1:4])
del list2[0]
print(list2)
#len([1, 2, 3])	3	长度
#[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
#['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
#3 in [1, 2, 3]	True	元素是否存在于列表中
#for x in [1, 2, 3]: print x,	1 2 3	迭代
#1	cmp(list1, list2)
#比较两个列表的元素
#2	len(list)
#列表元素个数
#3	max(list)
#返回列表元素最大值
#4	min(list)
#返回列表元素最小值
#5	list(seq)
#将元组转换为列表

#序号	方法
#1	list.append(obj)
#在列表末尾添加新的对象
#2	list.count(obj)
#统计某个元素在列表中出现的次数
#3	list.extend(seq)
#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#4	list.index(obj)
#从列表中找出某个值第一个匹配项的索引位置
#5	list.insert(index, obj)
#将对象插入列表
#6	list.pop([index=-1])
#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#7	list.remove(obj)
#移除列表中某个值的第一个匹配项
#8	list.reverse()
#反向列表中元素
#9	list.sort(cmp=None, key=None, reverse=False)
#对原列表进行排序

random.shuffle(list2) # 将序列a中的元素顺序打乱
print(list2)
list2.sort()
print(list2)

#输入
#print(input())

list2 = []
i = 0
while i < 10:
    list2.append(i * 10)
    i += 1
print(list2)


############################元组

##Dict = { }
##Dict["age"] = 18
##Dict["name"] = "你好"
##Dict[3] = 1000
##Dict[0] = 10086
##print(Dict)

#Dict = { }
#i = 0
#while i < 10:
#    Dict[i] = i
#    i += 1
#print(Dict[8])

#1	cmp(tuple1, tuple2)
#比较两个元组元素。
#2	len(tuple)
#计算元组元素个数。
#3	max(tuple)
#返回元组中元素最大值。
#4	min(tuple)
#返回元组中元素最小值。
#5	tuple(seq)
#将列表转换为元组


i = 1
j = 1
while i < 10:
    while j < 10:
        print(i," * ",j," = ",i * j)
        j += 1
    j = i + 1
    i += 1


import time;
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) )
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
#python中时间日期格式化符号：

#%y 两位数的年份表示（00-99）
#%Y 四位数的年份表示（000-9999）
#%m 月份（01-12）
#%d 月内中的一天（0-31）
#%H 24小时制小时数（0-23）
#%I 12小时制小时数（01-12）
#%M 分钟数（00=59）
#%S 秒（00-59）
#%a 本地简化星期名称
#%A 本地完整星期名称
#%b 本地简化的月份名称
#%B 本地完整的月份名称
#%c 本地相应的日期表示和时间表示
#%j 年内的一天（001-366）
#%p 本地A.M.或P.M.的等价符
#%U 一年中的星期数（00-53）星期天为星期的开始
#%w 星期（0-6），星期天为星期的开始
#%W 一年中的星期数（00-53）星期一为星期的开始
#%x 本地相应的日期表示
#%X 本地相应的时间表示
#%Z 当前时区的名称
#%% %号本身

import calendar
 
cal = calendar.month(2019, 9)
print ("以下输出2016年1月份的日历:")
print (cal)
print("cls")
import os
#os.system("cls")

#while True:
#    os.system("cls")
#    print(time.time())
#while True:
#    os.system("cls")
#    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

def temp():
    return 10086;

def Timer():
    while(True):
        os.system("cls");
        print(temp())
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    return;
#Timer()
def change(var):
    var = 100
    return var
var = 5
change(var)
print(var)
print(change(var))





def F(var):
    if(var == 0):
        return;
    print(var)
    F(var - 1)



import Header
import os


def fopen(fileName,Mode):
    try:
        file = open(fileName,Mode)
    except IOError:
        print("Error: 没有找到文件或读取文件失败")
    else:
        return file
def fclose(file):
    file.close()

class Student:
    age = 0
    name = "name"
    #构造函数
    def __init__(self):
        print("Student 无参构造函数调用")
    def __init__(self,age,name):
        self.age = age
        self.name = name
        print("有参构造函数调用")
    def __init__(self,age = 0,name = "默认"):
         self.age = age
         self.name = name
         print("有参构造函数调用")
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def __del__(self):
        print("析构函数调用")
    #obj = Student(18,"浩曼")
    #print(obj.getName())
    #obj.setName("希特勒")
    #print(obj.getName())
    #obj = Student()
    #print(obj.getName())
    #obj = C()
    #print(obj.getName())
    #print(C.__name__)
    #print(C.__module__)
class C:
    name = "12345"
    def __init__(self):
        print("C 无参构造函数调用")
    def getName(self):
        print(self.name)

class Parent:
    def __init__(self):
        print("Parent 构造")
    def __del__(self):
        print("Parent 析构")
    name = "Parent"
    def SetName(self,name):
        self.name = name
    def GetName(self):
        return self.name
class Child(Parent):
    m_age = 0
    ID = 10086
    #加连根下划线为私有成员
    __m_ID = 144564
    def __init__(self):
        print("Child 构造" + " 私有成员 " + str(self.__m_ID))
    def __del__(self):
        print("Child 析构")
    def GetClassName(self):
        return self.__name__
    def SetName(self,name = "默认 Parent"):
        self.name = name
    def SetName(self,name = "默认 重载",age = 0):
        self.name = name
        self.m_age = age;
    def __add__(self,than):
        self.name += than.name
        self.age += than.age


import threading

list = [0,0,0,0,0,0,0,0,0,0,0,0]
class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程:",self.name)
        # 获得锁，成功获得锁定后返回 True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回 False
        threadLock.acquire()
        print_time(self.name,self.counter,list.__len__())
        # 释放锁
        threadLock.release()
    def __del__(self):
        print (self.name,"线程结束！")
def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        list[counter-1] += 1
        print("[%s] %s 修改第 %d 个值，修改后值为:%d" % (time.ctime(time.time()),threadName,counter,list[counter-1]))
        counter -= 1
#threadLock = threading.Lock()
#threads = []
## 创建新线程
#thread1 = myThread(1,"Thread-1",1)
#thread2 = myThread(2,"Thread-2",2)
## 开启新线程
#thread1.start()
#thread2.start()
## 添加线程到线程列表
#threads.append(thread1)
#threads.append(thread2)
## 等待所有线程完成
#for t in threads:
#    t.join()
#print ("主进程结束！")

def PT(tName,delay):
    count = 0
    #while count < 5:
    while True:
        print(count)
        print("%s: %s" % ( tName, time.ctime(time.time()) ))
        count += 1;
        os.system("cls")


import sys
sys.path.append("h")
import te

def Main():

    obj = Child()
    obj.SetName()
    print(obj.GetName())
    obj.SetName("fuck",17)
    print(obj.GetName())
    print(obj.ID)
    #访问私有属性并更改
    obj._Child__m_ID = 100
    print(obj._Child__m_ID)
    
    thread = threading.Thread(target = PT,args = ("fds",0))
    thread.start()

    te.tes()


    #Header.recursion(10)
    #print(Header.GetNum())

    #if "nih" == 'nih':
    #    print("nih")

    #while True:
    #    str = input("请输入：")
    #    print(str)
    #    if str == "exit":
    #        exit(0)
    #    elif str == "cls":
    #        os.system("cls")
    #    elif str == "clear":
    #        os.system("cls")
    #    elif str == "ipconfig":
    #        os.system("ipconfig")
    #    elif str == "ls" or str == "ll" or str == "dir":
    #        os.system("dir")
    #    else:
    #        os.system(str)




    #############################文件

    #file = open("py.txt","w+")
    #print("文件名: ", file.name)
    #print("是否已关闭 : ", file.closed)
    #print("访问模式 : ", file.mode)
    ##print("末尾是否强制加空格 : ",file.softspace)
    #file.writelines("你好,python 文件")
    #file.write("你好,python 文件")
    #print("当前文件位置为:"+str(file.tell()))
    #file.seek(0,0)
    #print(file.read(100))

    #file.close()

    #os.remove(file_name)
    #os.rename(current_file_name, new_file_name)
    #os.mkdir("newdir")
    #os.rmdir('dirname')
    #可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
    #os.chdir("newdir")
    #print("当前的工作目录 "+os.getcwd())

    # 将当前目录改为"/home/newdir"
    #os.chdir("/home/newdir")


    #############################################异常捕获
    #try:
    #    fh = open("testfile", "w")
    #    fh.write("这是一个测试文件，用于测试异常!!")
    #except IOError:
    #    print("Error: 没有找到文件或读取文件失败")
    #else:
    #    print("内容写入文件成功")
    #    fh.close()


    return;
###########################################################

Main();

######################################################文件
#t	文本模式 (默认)。
#x	写模式，新建一个文件，如果该文件已存在则会报错。
#b	二进制模式。
#+	打开一个文件进行更新(可读可写)。
#U	通用换行模式（不推荐）。
#r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
#r+	打开一个文件用于读写。文件指针将会放在文件的开头。
#rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
#w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
#w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
#wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
#a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
#ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写


#序号	方法及描述
#1	
#file.close()
#关闭文件。关闭后文件不能再进行读写操作。
#2	
#file.flush()
#刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
#3	
#file.fileno()
#返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
#4	
#file.isatty()
#如果文件连接到一个终端设备返回 True，否则返回 False。
#5	
#file.next()
#返回文件下一行。
#6	
#file.read([size])
#从文件读取指定的字节数，如果未给定或为负则读取所有。
#7	
#file.readline([size])
#读取整行，包括 "\n" 字符。
#8	
#file.readlines([sizeint])
#读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。
#9	
#file.seek(offset[, whence])
#设置文件当前位置
#10	
#file.tell()
#返回文件当前位置。
#11	
#file.truncate([size])
#截取文件，截取的字节通过size指定，默认为当前文件位置。
#12	
#file.write(str)
#将字符串写入文件，返回的是写入的字符长度。
#13	
#file.writelines(sequence)
#向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符



#异常名称	描述
#BaseException	所有异常的基类
#SystemExit	解释器请求退出
#KeyboardInterrupt	用户中断执行(通常是输入^C)
#Exception	常规错误的基类
#StopIteration	迭代器没有更多的值
#GeneratorExit	生成器(generator)发生异常来通知退出
#StandardError	所有的内建标准异常的基类
#ArithmeticError	所有数值计算错误的基类
#FloatingPointError	浮点计算错误
#OverflowError	数值运算超出最大限制
#ZeroDivisionError	除(或取模)零 (所有数据类型)
#AssertionError	断言语句失败
#AttributeError	对象没有这个属性
#EOFError	没有内建输入,到达EOF 标记
#EnvironmentError	操作系统错误的基类
#IOError	输入/输出操作失败
#OSError	操作系统错误
#WindowsError	系统调用失败
#ImportError	导入模块/对象失败
#LookupError	无效数据查询的基类
#IndexError	序列中没有此索引(index)
#KeyError	映射中没有这个键
#MemoryError	内存溢出错误(对于Python 解释器不是致命的)
#NameError	未声明/初始化对象 (没有属性)
#UnboundLocalError	访问未初始化的本地变量
#ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
#RuntimeError	一般的运行时错误
#NotImplementedError	尚未实现的方法
#SyntaxError	Python 语法错误
#IndentationError	缩进错误
#TabError	Tab 和空格混用
#SystemError	一般的解释器系统错误
#TypeError	对类型无效的操作
#ValueError	传入无效的参数
#UnicodeError	Unicode 相关的错误
#UnicodeDecodeError	Unicode 解码时的错误
#UnicodeEncodeError	Unicode 编码时错误
#UnicodeTranslateError	Unicode 转换时错误
#Warning	警告的基类
#DeprecationWarning	关于被弃用的特征的警告
#FutureWarning	关于构造将来语义会有改变的警告
#OverflowWarning	旧的关于自动提升为长整型(long)的警告
#PendingDeprecationWarning	关于特性将会被废弃的警告
#RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
#SyntaxWarning	可疑的语法的警告
#UserWarning	用户代码生成的警告