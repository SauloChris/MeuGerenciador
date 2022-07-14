import os
import datetime

filename = 'texto1.txt'
stats = os.stat(filename)

def time(data):
    dt=datetime.datetime.fromtimestamp(data)
    return dt.strftime("%Y-%m-%d %H:%M-%S")

def get_file_attr(filename):
    dicatrib ={
    "Tamanho":os.path.getsize(filename),
    "Data da ultima modificação":time(os.path.getmtime(filename)),
    "Data da criação":time(os.path.getctime(filename)),
    "ID do Autor":os.stat(filename).st_uid
    }

    return dicatrib
print(get_file_attr(filename))