# Import libs

import requests
import datetime as dt
import pandas as pd
import os
import shutil

# Download dataset
today = dt.date.today()
url = "https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt"
dataset = requests.get(url,allow_redirects=True)
open(("/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2.txt"),'wb').write(dataset.content)
os.chmod('/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2.txt',0o777)
os.replace("/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2.txt",("/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2 "+str(today)+".txt"))

# Edit the dataset
today = dt.date.today()
# open file
with open(("/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2 "+str(today)+".txt"),"r") as file:
    data = file.readlines()

for i in range(0,9,1): # replacing data
    # print(data[i])
    data[i] = ""
data[0]= "Name\n"
# Slicing index 
# print(data[-1:])
data[-1:] = ""

with open(("/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2 "+str(today)+".txt"), 'w') as file:
    file.writelines( data )

# Reading the dataset

df = pd.read_csv(("/home/sunat/FortiSIEM/Botnet_C2_dataset/Dataset_C2 "+str(today)+".txt"),error_bad_lines=False)
df["Low IP"] = df["Name"] 
df["High IP"] = df["Name"] 
df["Malware Type"] = ["Botnet C2"] * df.shape[0]
df["Confidence"] = [" "] * df.shape[0]
df["Severity"] = [" "] * df.shape[0]
df["ASN"] = [" "] * df.shape[0]
df["Org"] = [" "] * df.shape[0]
df["Country"] = [" "] * df.shape[0]
df["Description"] = ["abuse.ch Feodo Tracker Botnet C2 IP Blocklist (recommended)"] * df.shape[0]
df["Last Seen"] = [today] * df.shape[0]
# df

# Export File to CSV format with header

today = dt.date.today()
df.to_csv ('/home/sunat/FortiSIEM/Botnet_C2_dataset/Botnet_IP_C2 '+str(today)+".csv", index = False, header=True, encoding="utf-8-sig")
print("OK at",today)

