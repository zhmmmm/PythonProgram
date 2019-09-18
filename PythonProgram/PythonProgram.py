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
