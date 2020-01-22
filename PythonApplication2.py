import numpy as np
import re#正则表达式的包
import pandas as pd
'''
文件是多组字典   而df的对象为一组字典  想办法合并多组字典
print(date.isnull())#是缺失值  返回值为true
plt.hist(date['price'], bins=20, normed=True)
print(date)    
'''
#导入文件
f=open('result.txt',encoding = "utf-8")
#导入文件的编码不是utf-8所以有报错  需要在后面加上 encoding = "utf-8"
filelist=f.readlines()
#定义储存的空列表
price=[]
deal=[]
shop=[]
location=[]


 #检查数据是否有缺失值 要写在循环里
"""
 如何判断多组字典key所对应的value为空
 并 删除或 填充
 思路一：
 如果key(deal)对应的value="",则删除字典
 line类型为字符串，可用eval()函数将其转化为字典
"""

for line in filelist:
    line=line
print(type(line))
print(line)



for line in filelist: #依次读取每行  
    #字符切割处理
    #(line)
    
    line=re.sub(r"[\:\"\¥]+",'',line)

    '''
    顺序不能放在循环最后  要不然会出错 
    '''

    line=line.strip().strip('{}')   #去掉每行头尾空白符  和 {}
    listline=line.split(',')    #按“，”切割

    '''
    如果按换行符分割数据 
    就 也把title切碎了  ，，，，，
    '''

    listline.pop(2)   #移除title与它所对应的元素
    listline=''.join(listline)
    listline=listline.split()
   # print(listline)
    '''
    price.append(str(listline[1]))
    deal.append(str(listline[3]))
    shop.append(str(listline[5]))
    location.append(str(listline[7]))
    '''
print(deal)
f.close()

