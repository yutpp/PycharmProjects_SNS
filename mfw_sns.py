import os
import numpy as np
import pandas as pd
row = 137
col = 137
Matrix = np.zeros((row,col))

# 如果某个景点的列表中，有一个景点名称在文章里出现，则返回TRUE
def isInArticle(article,list):
    for lst in list:
        if lst in article:
            return True
    return False

with open('spot3.txt', encoding='UTF-8') as f:  # 打开文件
    data = f.read()  # 读取文件
    string=data.strip("\'")#把字符串头尾的单引号删除
    spot=[x.strip().split('/')for x in string.split(',')]#生成景点的二维数组，因为有的景点有多种名称，
with open('mafengwoQA/mafengwoQA/answer.txt', encoding='UTF-8') as f:  # 打开文件
    for string in f:
        start_index = string.index('"answerContent":')
        end_index = string.index('==========')
        string=(string[start_index:end_index]).strip('\"answerContent\": \"\\n')
        # print(string)
        for i in range(len(spot)):
            for j in range(len(spot)) :
                if i != j and isInArticle(string,spot[i]) and isInArticle(string,spot[j]):
                    Matrix[i][j] +=1
print(Matrix)
data2 = pd.DataFrame(Matrix)
data2.to_csv('matrix_mfw_1.csv', index=0, columns=None, encoding='utf-8')