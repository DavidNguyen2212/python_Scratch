# Cài đặt thư viện requests và win10toast
import requests as req
from win10toast import ToastNotifier
import json
import time
from datetime import datetime
from json import *
def update():
    r = req.get('https://api.covidtracking.com/v1/status.json')
    data = r.json()     # chuyển response về dạng json  
    print("JSON: \n", r)
    print("Python data: \n", data)
    build_time = datetime.fromisoformat(data["buildTime"][:-1])
    formatted_time = build_time.strftime("%d-%m-%Y %H:%M:%S")   #Y để hiện đủ 4 số
    text = f"BuildTime: {formatted_time} \nProduction: {data["production"]} \nrunNumber: {data["runNumber"]}"

    while True:
        t = ToastNotifier()
        t.show_toast("Covid-19 Update", text, duration=20)  # ở dạng text, thời lượng 20s
        time.sleep(60)
update()