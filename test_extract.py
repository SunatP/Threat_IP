# Import Lib
import requests
import datetime as dt
import pandas as pd
import shutil
import zipfile
import os
# Download zip file and extract to the destination path 

today = dt.date.today()
url = "https://threatfox.abuse.ch/export/csv/ip-port/full/"
dataset = requests.get(url,allow_redirects=True)
open((r"/home/sunat/FortiSIEM/ThreatFox_Dataset/Dataset_Malware_"+ str(today) + ".zip"),'wb').write(dataset.content)
os.chmod("/home/sunat/FortiSIEM/ThreatFox_Dataset/Dataset_Malware_"+ str(today) + ".zip",0o777)
os.replace(("/home/sunat/FortiSIEM/ThreatFox_Dataset/Dataset_Malware_"+ str(today) + ".zip"),("/home/sunat/FortiSIEM/ThreatFox_Dataset/Dataset_Malware_"+str(today)+".zip"))

# Extract File
with zipfile.ZipFile(("/home/sunat/FortiSIEM/ThreatFox_Dataset/Dataset_Malware_"+str(today)+".zip"),'r') as zipfile_ref:
    zipfile_ref.extractall("/home/sunat/FortiSIEM/ThreatFox_Dataset/")

# os.replace(("/home/sunat/FortiSIEM/full_ip-port.csv"),("/home/sunat/FortiSIEM/ThreatFox_Dataset/full_ip-port.csv"))
