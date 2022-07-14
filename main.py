import os

filename = 'texto1.txt'

print("Tamanho = ",os.path.getsize(filename))
print("Data da ultima modificação = ",os.path.getmtime(filename))
print("Data da ultima criação = ",os.path.getctime(filename))

stats = os.stat(filename)
print("ID do autor =",stats.st_uid)