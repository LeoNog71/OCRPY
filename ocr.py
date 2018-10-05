import os
import shutil 
import textract
import time
import datetime
import bd

queue = os.listdir(str(os.getcwd())+'/queue/')
    
if len(queue) == 0:
    testes = os.listdir('/home/leonardo/Documentos/testes/')
    for x in testes:
        shutil.copy2('/home/leonardo/Documentos/testes/'+str(x), str(os.getcwd())+'/queue/')
        queue = os.listdir(str(os.getcwd())+'/queue/')

cron = None
for item in queue:
    
    try:
        cron = datetime.datetime.now()
    
        print("Ocerizando o arquivo: "+ item+" às "+cron.strftime("%y-%m-%d-%H:%M:%S"))
    
        text = textract.process((str(os.getcwd())+'/queue/'+str(item)), encoding='ascii')
        files = open(str(os.getcwd())+"/result/"+str(item)+".txt","w+",encoding='utf-8')
        files.write(str(text))
        files.close()
        os.remove(str(os.getcwd())+'/queue/'+str(item))
    
        print("Terminou o arquivo: "+ item+" às "+ datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S")+ " demorou = "+str(datetime.datetime.now() - cron))
        print("----------------")
        
    except Exception as identifier:
        print(identifier)
