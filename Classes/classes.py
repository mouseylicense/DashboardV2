from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime as dt
from google.oauth2 import service_account
import os
import requests
import time as t
# variable declaration
secret_file = os.path.join(os.getcwd(),"/home/hangar/DashboardV2/Classes/client_secret.json")
creds = service_account.Credentials.from_service_account_file("/home/hangar/DashboardV2/Classes/client_secret.json")
schedule_times = ["08:30","09:15","10:07","11:00","11:45","12:45"]
TIME_SPREAD_ID = "1J6V9rF9uAAl1JEXbdVummdC4e-Ray4HsuMlMXLBY_yg"
TIME_RANGE = "Times!A2:E"
times_service = build('sheets', 'v4', credentials=creds)
times_sheet = times_service.spreadsheets()
times = times_sheet.values().get(spreadsheetId=TIME_SPREAD_ID,range=TIME_RANGE).execute()

# converting numbers to days (letters)
day_to_weekday = {0: "ב", 1:"ג",2:"ד",3:"ה",4:"ו",5:"ש",6:"א"}

def reset_all():
    classes = requests.post("http://127.0.0.1:5000/data")
    for key in classes.json().keys():
        requests.post("http://127.0.0.1:5000/get_classes",data={"room":key,"class":"פנוי","key":"wajitalslkmLatkolkadws"})
while True:
    now = dt.datetime.now().strftime("%H:%M")
    if now=="14:00":
        print("resetting")
        reset_all()
    for time in schedule_times:
        if time == now:
            reset_all()
            for Class in times.get('values',[]):
                if day_to_weekday[dt.datetime.now().weekday()] == Class[0]:
                    if Class[1][:-3] == time:
                        room = Class[4]
                        isFree = f"{Class[2]} - {Class[3]}"
                        print({"room":room,"class":isFree,"key":"wajitalslkmLatkolkadws"})
                        requests.post("http://127.0.0.1:5000/get_classes",data={"room":room,"class":isFree,"key":"wajitalslkmLatkolkadws"})
    t.sleep(1)
