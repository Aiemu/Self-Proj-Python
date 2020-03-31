import csv 
import pandas as pd

rankPath = "./rank.csv"
listPath = "./list.csv"

with open(rankPath) as rf:
    rankReader = csv.reader(rf)
    rankList = list(rankReader)
    


with open(listPath) as lf:
    listReader = csv.reader(lf)
    listList = list(listReader)

count = 0
outList = []
for i in rankList:
    for j in listList:
        if i[1] == j[0]:
            tmpList = []
            tmpList.append(j[1])
            for k in range(1, 13):
                tmpList.append(i[k])
            tmpList.append(i[0])
            tmpList.append(j[2])
            outList.append(tmpList)

print(outList)
title = ["Name", "SID", "GPA-all", "Rank-all", "Credit-all", "GPA-limit", "Rank-all", "Credit-all", "Fail-Course", "Credit-minor", "SRT", "PE-Class-Passed", "Credit-failed", "Qualification", "Department"]
outCSV=pd.DataFrame(columns=title, data=outList)
outCSV.to_csv("./out.csv", encoding = "utf-8")