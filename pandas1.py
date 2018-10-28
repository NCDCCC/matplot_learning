import pandas as pd
import numpy as np

#Series
a = pd.Series(np.arange(4,10))
b = pd.Series([11,12,14],index = ['qqq','eee','eee'])#allowed
c = pd.Series({"qqq":11,'eee':12,"eee":14})#not allowed
print(a)
print(b)
print(c)

#DataFrame(important)
data_3_4 = pd.DataFrame(np.arange(10,22).reshape(3,4),dtype = 'float64')
print(data_3_4,data_3_4.shape)
print(data_3_4.index)#index
print(data_3_4[1:2])#row slice
print(data_3_4[:][1])#column

#open csv file
file = pd.read_csv("./SunSign.csv")
print(file,file.shape)
print(file.head(2))#top 2
print(file.tail(2))#foot 2
print(file.describe())#etc.
print(file["星座"][1:6])#special column
print(file[file["结束月日"]>601])#bool index

print(file.sort_values(by = '开始月日',
	ascending = False))#sort
file1 = file.dropna()#delete Samples including missing value
print(file1)
file2 = file.fillna('?')#fill missing value
print(file2)