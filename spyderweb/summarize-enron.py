# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:06:15 2019

@author: pichappan
"""
import pandas as pd
import csv
import math
import sys
import os

file_name = sys.argv[1]

OUTDIR = "../output/"
OUTFILE1 = OUTDIR+"output1_sent_received.csv"
OUTFILE2 = OUTDIR+"output2_prolific_senders.png"
OUTFILE3 = OUTDIR+"output3_percentage_people_count.png"

if  os.path.isdir(OUTDIR)==False:
    os.mkdir(OUTDIR)

#0 Read required columns into DataFrame 
#with open('enron-event-history-all.csv') as csvFile:
with open(file_name) as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    times = []
    months = []
    senders = []
    recipients = []
    i=0
    for row in readCSV:
        recipient = row[3]
        toList = recipient.split('|')
        for each in toList:
            time = row[0]
            month = math.floor(int(time)/(1000*3600*24*30))
            sender = row[2]
            times.append(time)
            months.append(month)
            senders.append(sender.title())
            recipients.append(each.title())
            
    dictData = {
        'time': times,
        'month': months,
        'sender':senders,
        'recipient':recipients
    }
    dfData = pd.DataFrame(dictData)

#1 Perform Dataframe group by to get the count by Sender & Recipient. Then concat the DataFrame and sort it
dfSender = dfData.groupby('sender').count()[['time']]
dfSender.rename(columns={"time":"cntSender"}, inplace=True)

dfRecipient = dfData.groupby('recipient').count()[['time']]
dfRecipient.rename(columns={"time":"cntRecipient"}, inplace=True)

dfMerged = pd.concat([dfSender, dfRecipient], axis=1, sort=True)
dfMerged.fillna(value={'cntSender': 0, 'cntRecipient': 0}, inplace=True)
dfMerged.sort_values(by=['cntSender','cntRecipient'], ascending=False, inplace=True, na_position='last')
dfMerged.to_csv(OUTFILE1)

top = 5
dfHead = dfMerged.head(top)
dfHead.rename(columns={"cntSender":"hSender","cntRecipient":"hRecipient"}, inplace=True)
lHead=dfHead.index.to_list()

#2 Performed DataFrame group by Sender & Month for top 5 Prolific Senders
import matplotlib.pyplot as plt
#import matplotlib
import datetime


def get_year_month(unix_time):
    return datetime.datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m')

plt.figure()
mList = []
for sender in lHead:
    df1Sender = dfData[(dfData.sender == sender)]
    df1MonthSender = df1Sender.groupby(['sender','month']).count()[['recipient']]
    tmp = df1MonthSender.index.tolist()
    month_ids = []
    for m in range(len(tmp)):
        month_ids.append(tmp[m][1])
        #month_ids.append(get_year_month(tmp[m][1]))
      
    #print(month_ids)
    x = month_ids
    y = df1MonthSender['recipient'].values.tolist()
    plt.plot(x,y,label = sender)
    mList.append([sender, month_ids])

# Legend
plt.title('Email count for Prolific Senders across every month')
plt.grid(True)
plt.xlabel("Month in Unix Time")
plt.ylabel("Email Count")
plt.legend(loc=2, borderaxespad=0.,frameon=False)
plt.savefig(OUTFILE2, format='png',dpi=200)


#3 Performed DataFrame group by Recipient & Month for top 5 Prolific Senders, Then preparied data for plot
plt.figure()
for sender in mList:
    df1Sender2 = dfData[(dfData.sender == sender[0])]
    df1MonthSender2 = df1Sender2.groupby(['sender','recipient','month']).count()[['time']]
    df1MonthSender2.to_csv('monthly_count.csv')
    df3MonthRecipient = pd.read_csv('monthly_count.csv')
    df3Groupby = df3MonthRecipient.groupby(['sender','month']).count()[['recipient']]
    df3Groupby.rename(columns={"recipient":"cnt"}, inplace=True)
    tmp = df3Groupby.index.tolist()
    month_ids = []
    month_cnt = []
    for m in range(len(tmp)):
        month_ids.append(tmp[m][1])
    x = month_ids
    y = (df3Groupby['cnt'].values*100)/(df3Groupby.sum(axis=0)).tolist()
    plt.plot(x,y,label = sender[0])
    
# Legend
os.remove('monthly_count.csv')
plt.title('Count of unique people contacted by prolific senders')
plt.grid(True)
plt.xlabel("Month in Unix Time")
plt.ylabel("Percentage People Count")
plt.legend(loc=2, borderaxespad=0.,frameon=False)
plt.savefig(OUTFILE3, format='png',dpi=200)
