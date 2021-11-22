# client.py
import socket
import pickle

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = '127.0.0.1'
port = 8888
# connection to hostname on the port.
s.connect((host, port))
# Collect user data
peso = (input('Peso(kg):'))
altura = (input('Altura(m):'))
# List
dados = []
dados.append(peso)
dados.append(altura)
# Send data to server
s.send(pickle.dumps(dados))
# Result
resultado = s.recv(1024)
dados = pickle.loads(resultado)


# Receive no more than 1024 bytes

s.close()
print('O seu IMC é: '+ str(dados[0])+'. '+str(dados[1]))
