# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:12:09 2020

@author: user
"""

import pandas
df = pandas.read_csv("collaborative-data/User1data.csv")
r = df["Recommended"]
ans_r = []
for i in range(len(r)):
    if "(" in r[i]:
        start_ind = r[i].index('(')
        end_ind = r[i].index(')')
    if "-" in r[i]:
        j = r[i].index('-')
        start_ind = j+2
        for k in range(j+2,len(r[i])):
            if ord(r[i][k]) >=65 and ord(r[i][k])<=90:
                start_ind = k
                break
        end_ind=len(r[i])-1
    ans_r.append(r[i][start_ind+1:end_ind])    

s = df["Selected"]
ans_s = []
for i in range(len(s)):
    if pandas.isnull(s[i]) or pandas.isna(s[i]):
        ans_s.append('')
        continue
    if "-" in s[i]:
        j = s[i].index('-')
        start_ind = j+2
        for k in range(j+2,len(s[i])):
            if ord(s[i][k]) >=65 and ord(s[i][k])<=90:
                start_ind = k
                break
        end_ind=len(s[i])-1
    else:
        for k in range(1,len(s[i])):
            if ord(s[i][k]) >=65 and ord(s[i][k])<=90:
                start_ind = k
                break
        end_ind=len(s[i])-1 
    ans_s.append(s[i][start_ind+1:end_ind])
ans_df = [list(ans_r)]
ans_df.append(list(ans_s))
an = pandas.DataFrame(ans_df)
an.to_csv("ans.csv")