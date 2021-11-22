import socket
import pickle
import threading

# Function
def calcularIMC(peso, altura):
      imc = (float(peso))/(float(altura))**2
      return imc
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = '127.0.0.1'
port = 8888
# bind to the port
serversocket.bind((host, port))
# starts listening requests
serversocket.listen()
def handle_client(clientsocket, addr):
  dados = clientsocket.recv(1024)
  dados = pickle.loads(dados)
  print(dados)
  resultado = calcularIMC(dados[0],dados[1])
  if (resultado<18.5):
        mensagem = ("Você está abaixo do peso ideal. Busque ajuda com o nutricionista.")
  elif ((resultado>=18.5) and (resultado<=24.9)):
        mensagem = ("Parabéns! O seu peso está normal.")
  elif((resultado>=25) and (resultado<=29,9)):
        mensagem = ("Você está com sobrepeso. Consulte um nutricionista.")
  elif((resultado>=30) and (resultado<=34,9)):
        mensagem = ("Cuidado! Você pode estar com obesidade grau 1. Consulte um nutricionista para avaliar a situação.")
  elif((resultado>=35) and (resultado<=39,9)):
        mensagem = ("Cuidado! Você pode estar com obesidade grau 2. Consulte um nutricionista para avaliar a situação.")
  elif(resultado>40):
        mensagem = ("Cuidado! Você pode estar com obesidade grau 3. Consulte um nutricionista para avaliar a situação.")
    #List
  enviacliente = []
  enviacliente.append(resultado)
  enviacliente.append(mensagem)
  clientsocket.send(pickle.dumps(enviacliente))

  clientsocket.close()

while True:
  clientsocket,addr = serversocket.accept()
  t = threading.Thread(target=handle_client, args=(clientsocket, addr))
  t.start()
  print("Got a connection from %s" % str(addr))