from numpy import*
from pandas import*
dict1={'Success':[]}
#Data colected 
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, nan, 9, 20, 14.5, nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=DataFrame(exam_data,
            columns=['name','score','attempts','qualify'])
#setting a label
df['Labels']=labels
df.set_index('Labels', inplace=True)
#dropping rows containing nan values
df2=df.dropna(subset=["score"])
#extracting name and score column
df3=df[["name","score"]]
#appending k
k={'name' : ["Suresh"], 'score': [15.5], 'attempts': [1], 'qualify': ["yes"]}
dg=DataFrame(k,
            columns=['name','score','attempts','qualify'])
df4=concat([df,dg])
#droping "attempt"
df5=df4.drop("attempts",axis=1)
#adding sucess
for i in df5.itertuples():
    if i[2]>=10:
        dict1['Success'].append(1)
    else:
         dict1['Success'].append(0)


df5['success']=dict1['Success']




print(df)
print(df.head(3))
print(df2)
print(df3)
print(df4)
print(df5)
#saving file
print(df5.set_index('Labels'))
df5.to_csv('raw_di.csv', index=True)
import csv
with open('raw_di.csv') as file:
    c=csv.reader(file,delimiter=',')
    for i in c:
        print(type(c))

