# -*- coding: utf-8 -*-
"""ch3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r5ACCH1g4sgSfmtUkm753RO-5NzTrk2V
"""

from os import EX_TEMPFAIL
#待辦事項=[]
#工作=input("請輸入工作?")
#待辦事項.append(工作)
#print(待辦事項.pop(0),待辦事項.pop(0),待辦事項)            #用pop會在同一行程式碼逐一刪除指定位置的元素
#print(待辦事項.pop(),待辦事項)

#Dict={'apple': '蘋果', 'bird':'鳥', 'cat':'貓'}
#print(Dict.keys())
#print(Dict)
#英文=input('請輸入一個英文單字?')
#print(Dict.get(英文,"找不到該單字"))

#詩="白日依山盡，黃河入海流。欲窮千里目，更上一層樓。"
#字=set(詩)
#字.remove("，")                #注意標點符號不能是(英文)半形，會被當作程式碼
#字.remove("。")
#print(字)

#星期=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
#月份=["January","February","March","April","May","June","July","August","September","October","November","December"]
#Dict={'week':星期,'month':月份}
#print(Dict['month'][9])         #字典[鍵值]讀取key對應的value

#s=input('請輸入一句英文直述句')
#s.split('.')
#words=s.split(" ")
#print(words[::-1])

#全班學生=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
#英文及格=set(['John','Mary','Fiona','Claire','Ben','Bill'])
#數學及格=set(['Mary','Fiona','Claire','Eva','Ben'])
#print("數學和英文都及格的人:", 英文及格&數學及格)
#print("數學不及格的人:", 全班學生-數學及格)
#print("英文及格且數學不及格的人:", 英文及格&(全班學生-數學及格))

#Poem1="床前明月光，疑是地上霜。舉頭望明月，低頭思故鄉。"
#Poem2="清明時節雨紛紛，路上行人欲斷魂。借問酒家何處有，牧童遙指杏花村。"
#Set1=set(Poem1)
#Set1.remove("，")
#Set1.remove('。')
#Set2=set(Poem2)
#Set2.remove('，')
#Set2.remove('。')
#print(Set1&Set2).

#Mail=dict()
#name=input("請輸入名字")
#email=input("請輸入email")
#Mail[name]=email
#name=input('請輸入要查詢email的名字')
#print(mail[name])