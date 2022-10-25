import os
import numpy as np
import pandas as pd

with open('spot3.txt', encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    string=data.strip("\'")#把字符串头尾的单引号删除
    spot=[x.strip().split('/')for x in string.split(',')]#生成景点的二维数组，因为有的景点有多种名称，

#如果某个景点的列表中，有一个景点名称在文章里出现，则返回TRUE
def isInArticle(article,list):
    for lst in list:
        if lst in article:
            return True
    return False
#定义两个行列相同的矩阵相加
def add(x,y):
    result=np.ones((len(x),len(x[0])))
    for i in range(len(x)): # 迭代输出行，矩阵当中，是由三个列表所呈现的。
        for j in range(len(x[0])): # 迭代输出列，访问大列表当中 每个列表的第一个元素，即为列
            result[i][j] = x[i][j]+y[i][j] #X下标对应的数字，加上Y下标对应的数字 即为所求
    return result

def read_path(file_pathname):
    # 遍历该目录下的所有文件
    Matrix = np.zeros((137, 137))
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
        loc = []
        for x in spot:
            if isInArticle(data1,x):
                loc.append(spot.index(x))
        # print(loc)
        m=np.ones((137,137))
        m[loc, :] += 1  # 行+1
        m[:, loc] += 1  # 列+1
        row, col = np.diag_indices_from(m)
        m[row, col] = 2  # 对角线赋值
        m = m // 3  # 转化为0和1
        # print(m)
        Matrix=add(Matrix,m)
    return Matrix

a=read_path(r'D:\PycharmProjects\SNS\articles')
print(a)
data2 = pd.DataFrame(a)
data2.to_csv('matrix_xc.csv', index=0, columns=None, encoding='utf-8')