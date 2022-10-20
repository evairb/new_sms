import base64
import code
from email import message
import json
import requests
from requests_toolbelt.utils import dump
import mysql.connector
from doctest import testfile
import mysql.connector
import envio as cod_resp



login = 'fundomunsaude'
password = 'YzcxOWE3ZTQ@'
credentials = login + ':' + password
# credentials = password
credentials_byte = credentials.encode('ascii')
auth = base64.b64encode(credentials_byte)
auth = 'Basic ' + auth.decode('ascii')
header = {'Content-Type':'application/json','Authorization' : auth}


#print(auth)


mydb = mysql.connector.connect(
  host="10.46.116.95",
  user="pontaltech",
  password="p23bd7slkrs92hww",
  database="pontaltech_sms"
)

mycursor = mydb.cursor()
def teste(item):
    number_res = item['to']
    status_res = item['status']
    sDesc_res = item['statusDescription']
    eCode_res = item['error']['code']
    eMessage = item['error']['message']
    print("##########")
       
    sql = "INSERT INTO log (to_number, status, statusDescription, error_code, error_message) VALUES (%s, %s, %s, %s, %s)"
    val = (number_res,status_res,sDesc_res,eCode_res,eMessage)

    mycursor.execute(sql, val)

    mydb.commit()
    return number_res
    

def enviar_sms(phone, text):
    global teste
    try:
        data_sms = {'to':phone,'message':text}
        r = requests.request(method = 'POST', url = 'https://sms-api-pointer.pontaltech.com.br/v1/single-sms', headers = header, json = data_sms)
    except Exception as erro:
        return
    
    print('header enviado:')
    print(header)
    print('Body enviado:')
    print(data_sms)
    print('Tipo de objeto do body:')
    print(type(data_sms))
    print('status da resposta:')    
    print('Codigo da resposta; ' + str(r.status_code))
    print('Corpo da resposta:')
    print("###################")
    print(r.content.decode('utf-8'))
    r_dict = json.loads (r.content.decode('utf-8'))
    teste(r_dict)
    print('Cabeçalho da resposta:')
    print(r.headers)

   
    
   
    







    

