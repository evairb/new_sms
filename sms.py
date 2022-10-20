from zipfile import ZipFile
from datetime import datetime as dt
import os
import shutil
from time import sleep
from log import msg_log
from mensageiro import Mensageiro, email_erro
import pandas as pd


#copiar arquivo pasta raiz
dataref = dt.today().strftime('%d%m%Y')
origin_path = r'\\Smssis05a173\relatorios$\REL_127_MAILINGS_TORPEDOS_SMS\\'
base_name_zip = f'Mailing_torpedos_SMS_{dataref}.zip'
full_name_zip = origin_path + base_name_zip
base_name_csv = full_name_zip.replace('zip','csv').replace(origin_path,'')
work_path = r'C:\Users\x329470\Documents\new_sms\env\arq_csv\\'
fake_file = r"C:\Users\x329470\Documents\new_sms\env\fake_csv.csv" #excluir em produção
work_path_abre = r'C:\Users\x329470\Documents\new_sms\env\arq_abrev\\'


if not os.path.isdir(origin_path):
    email_erro()
    print('diretorio não encontrado')
    exit()

if not os.path.isfile(full_name_zip):
    email_erro()
    print('arquivo não encontrado')
    exit()

try:
    shutil.copy(full_name_zip, work_path)
except Exception as erro:
    email_erro()
    msg_log('Codigo da res ' + str(erro))
    exit()


arqZip = work_path + base_name_zip

with ZipFile(arqZip,'r') as f:
    if len(f.namelist()) != 1:
        print('Inconsistência na abertura do arquivo')
        exit()
    try:
        ZipFile.extractall(f, path = work_path)
    except Exception as erro:
        print('Erro na extração: ' + str(erro))


df = pd.read_csv(work_path + base_name_csv, delimiter=";", low_memory=False, encoding='ISO-8859-1')

#altera a nomeclatura da coluna nome executante

def substituir(texto):
    arr = [('AMA ESPECIALIDADES','AE'),('UBS JARDIM','UBS JD'),('INTEGRADA',''),('AMA/ UBS','UBS'),
    ('AMBULATORIO ESPECIALIDADES','AE'),('CENTRO DE PRATICAS','C.PRAT'),('HOSPITAL DIA ','HD '),('INFANTIL','INF'),
    ('HOSPITAL INTEGRADO','HI'),('HOSPITAL MUNICIPAL ','HM '),('SANTO','ST'),('ASSOC AACD','AACD'),('HOSPITALAR','HOSP'),('HOSP DIA','HD'),
    ('UNIDADE', 'UNID.'), ('IMAGEM', 'IMA'),('TOMOGRAFIA DA FOR - REGIAO SUDESTE', 'FUNDACAO OSWALDO RAMOS'), ('TOMOGRAFIA DA FOR - REGIAO SUL', 'FUNDACAO OSWALDO RAMOS'),
    ('TOMOGRAFIA DA FOR - REGIAO CENTRO OESTE','FUNDACAO OSWALDO RAMOS') ]

    for er,subs in arr:
        texto = texto.replace(er,subs)
    return texto
    
df['NOME_EAS_EXECUTANTE'] = df['NOME_EAS_EXECUTANTE'].apply(lambda x:substituir(str(x)))
df.to_csv(work_path_abre + base_name_csv,encoding = 'iso-8859-1',sep=';',index= None)


#mensageiro = Mensageiro(work_path_abre + base_name_csv)   #descomentar em produção
mensageiro = Mensageiro(fake_file) #excluir em produção



mensageiro.enviar_sms()

     

