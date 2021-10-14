class Carro():
    def __init__(self, tanque):
        self.__tanque = tanque#Atributo privado

    def andar(self, km):
        self.__tanque -= (km * 0.5)

    def abastecer(self, gasolina):
        self.__tanque += float(gasolina)

    def getTanque(self):
        return self.__tanque
    
    def setTanque(self, novo):
        self.__tanque = novo

corsa = Carro(0)

valorAbastecimento = input("Frentista: Quanto você quer abastecer?\n ")
float(valorAbastecimento)
corsa.abastecer(valorAbastecimento)
tanqueAtual = valorAbastecimento 
float(tanqueAtual)

print("Frentista: Abastecemos {} litros do seu tanque. Agora você tem {} litros no seu tanque\n".format(valorAbastecimento,tanqueAtual))

distancia = input("Amigo: Que tal darmos uma voltinha na estrada? Quantos km você consegue correr?\n")
distancia = float(distancia)

corsa.andar(distancia)

tanqueAtual = float(valorAbastecimento) - float(distancia * 0.5)

print("Que irado! corremos {} km! Agora temos {}L no tanque!".format(distancia,tanqueAtual))