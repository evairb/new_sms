from datetime import datetime as dt
import csv


def msg_log(msg):
    file = r'C:\Users\x329470\Documents\new_sms\env\logs.csv'
    with open(file,'a+',newline='') as f:
        writer = csv.writer(f,delimiter=';')
        agora = dt.now()
        agora = dt.now().strftime('%d%m%Y %H:%M:%s')
        data = [agora, msg]
        writer.writerow(data)



