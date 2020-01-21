import numpy as np
import re#正则表达式的包
'''
文件是多组字典   而df的对象为一组字典  想办法合并多组字典
print(date.isnull())#是缺失值  返回值为true
plt.hist(date['price'], bins=20, normed=True)
print(date)    
'''
f=open('result.txt',encoding = "utf-8")
#导入文件的编码不是utf-8所以有报错  需要在后面加上 encoding = "utf-8"
filelist=f.readlines()

price=[]
deal=[]
title=[]
shop=[]
location=[]

for line in filelist: #依次读取每行    
    line=re.sub(r"[\:\"\¥]+",'',line)
    #顺序不能放在循环最后  要不然会出错 
    line=line.strip().strip('{}')   #去掉每行头尾空白符  和 {}
    listline=line.split()     #按换行符分割数据 
    #也把title切碎了  ，，，，，
    print(listline)

    price.append(str(listline[1]))
    deal.append(str(listline[3]))#不能用char  会显示char not defined
    title.append(str(listline[5]))
    shop.append(str(listline[7]))
    location.append(str(listline[9]))
    '''
    line[3]=re.sub(r"[\u4e00-\u9fff]+","",line[3])#去除字符串中的中文字  
    '''
print(title)
f.close()