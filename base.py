# -*- coding: utf-8 -*-
preCount = 72.000
nowCount = 85.000
r = ((nowCount - preCount) / preCount) * 100.00
print('%.1f%%' %r)

print('******元组练习*****')
L = [
	['Apple','Google','microsoft'],
	['java','Python','ruby','php'],
	['adam','bb','Lisa']
	]
FF = L[0][0]
print('打印：%s'%FF)
PP = L[1][1]
print('打印：%s'%PP)
LL = L[2][2]
print('打印：%s'%LL)

print('******条件练习*****')
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
	print('过轻')
elif 18.5 < bmi <= 25:
	print('正常')
elif 25 < bmi <= 28:
	print('过重')
elif 28 < bmi <= 32:
	print('肥胖')
elif 32 < bmi:
	print('严重肥胖')

print('******循环*****')	
WL = ['Bart','Lisa','Adam']
for x in WL:
	print('Hello,%s'%x)


print('******函数调用*****')
n1 = 255
n2 = 1000
hn1 = hex(255)
hn2 = hex(1000)
print('%s %s'%(hn1,hn2))	
print('******自定义函数*****')
# from Fountion import myHelloWorld
# myHelloWorld('hi world')
print('******求解一元二次方程*****')
from Fountion import quadratic,helloworld
print(quadratic(2, 3, 1))
helloworld()

print('*******切片******')
arr = ['a','b','c','d','e']
print('%s'%(arr[0:3]))
r = []
n = 3
for i in range(n):
	r.append(arr[i])
print('%s'%(r))

print('*******迭代******')
from collections import Iterable
v = isinstance('abc', Iterable)
print('%s'%v)

v = isinstance(['1','3','5','6'], Iterable)
print('%s'%v)

v = isinstance(123, Iterable)
print('%s'%v)

for x, y in [(1, 1), (2, 4), (3, 9)]:
 	print(x,y)

print('*******列表生成器******')
myList = []
for x in range(1,11):
	myList.append(x)
print(myList)
myList =  [x * x for x in range(1, 11)]
print(myList)

import os
docment = [d for d in os.listdir('.')]
print(docment)

L2 = []
L1 = ['Hello', 'World', 666, 'Python', None]
for x in L1:
	flag = isinstance(x, str)
	if flag:
		x = x.lower()
		L2.append(x)
print(L2)

