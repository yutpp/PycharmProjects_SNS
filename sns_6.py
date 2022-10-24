import os
import numpy as np
import pandas as pd
row = 137
col = 137
Matrix = np.zeros((row,col))
with open('spot3.txt', encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
    string=data.strip("\'")#把字符串头尾的单引号删除
    print(string)
    print(len(string))
    spot=[x.strip().split('/')for x in string.split(',')]#生成景点的二维数组，因为有的景点有多种名称，
    print(spot)

#如果某个景点的列表中，有一个景点名称在文章里出现，则返回TRUE
def isInArticle(article,list):
    for lst in list:
        if lst in article:
            return True
    return False

def read_path(file_pathname):
    # 遍历该目录下的所有文件
    for filename in os.listdir(file_pathname):
        path1 = os.path.join(r'D:\PycharmProjects\SNS\articles', filename)
        path2=os.path.join(r'D:\PycharmProjects\SNS\articles_3', filename)
        f1 = open(path1, 'r',encoding='utf-8')
        f2 = open(path2, 'w', encoding='utf-8')
        for line in f1.readlines():
            if line == '\n':
                line = line.strip('\n')#删除文章中的空白行
            f2.write(line)
        f2.close()
        f2 = open(path2, 'r', encoding='utf-8')
        data1 = f2.read()
        for i in range(len(spot)):
            for j in range(len(spot)) :
                if i != j and isInArticle(data1,spot[i]) and isInArticle(data1,spot[j]):
                    Matrix[i][j] +=1


read_path(r'D:\PycharmProjects\SNS\articles')
print(Matrix)
data2 = pd.DataFrame(Matrix)
data2.to_csv('matrix5.csv', index=0, columns=None, encoding='utf-8')