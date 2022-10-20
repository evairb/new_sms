import csv
import requests
from envio import enviar_sms
import smtplib
from email.mime.text import MIMEText


#Erros na descompatação
def email_erro():
    server = smtplib.SMTP('SMTPCORP.PRODAM', 25)
    msg = MIMEText(f'tetsteeeeee')
    sender = 'smsdtic@prefeitura.sp.gov.br'
    #recipients = ['evairbd@prefeitura.sp.gov.br']
    recipients = ['giovanifranco@prefeitura.sp.gov.br','evairbd@prefeitura.sp.gov.br']
    msg['Subject'] = "Teste de SMTP PYTHON"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    server.sendmail(sender, recipients, msg.as_string())

    server.quit()

class Mensageiro(object):
    arq_csv = ''
    def __init__(self, nome_arquivo):
        self.arq_csv = nome_arquivo
      

    def enviar_sms(self):
        with open(self.arq_csv,'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f, delimiter=';')
        
            for linha in reader:                    
                    cod_agendamento=linha[0]
                    cns_paciente=linha[1]
                    nome_paciente=linha[2]
                    nome_abrevia=nome_paciente.split(' ')
                    nome_abrevia=nome_abrevia[0:3]
                    nome_abrevia=' '.join(nome_abrevia)
                    celular=linha[3]
                    data_da_vaga=linha[4]
                    nome_eas_executante=linha[5]                    
                    #campos do csv
                    if nome_paciente != 'NOME_PACIENTE':
                        sms_text = rf'A Pref de SP COMUNICA O AGENDAMENTO Do(a) SR(a) {nome_abrevia} dia {data_da_vaga} .. {nome_eas_executante}'                    
                        sms_text=sms_text[0:160]
                        try:                                                      
                            print(sms_text + ', enviado para o fone: ' + celular)                            
                            enviar_sms(celular, sms_text)
                        except Exception as erro:
                             print("erro")
 
      
                        

