#!/urs/bin/envy python
import cgi
import cgitb

# python -m http.server 8080 --cgi

def cel_fahr(celsius):

    resultado = celsius * (9 / 5) + 32
    return resultado

def fahr_cel(fahrenheit):

    resultado = (fahrenheit - 32) * (5 / 9)
    return resultado
def cel_kel(celsius):

    resultado = celsius * 274.15
    return resultado
    
def fahr_kel(fahrenheit):
    resultado = (fahrenheit + 459.67) * (5/9)
    return resultado
    
def metro_cm(metro):
    resultado = metro * 100.0
    return resultado

    

def metro_km(metro):
    resultado = metro/1000.0
    return resultado

def metro_decimetro(metro):
    resultado = metro * 10.0
    return resultado


cgitb.enable()

form = cgi.FieldStorage()

temperatura = form.getvalue('temperatura')
temp_atual = form.getvalue('deTemperatura')
temp_conversao = form.getvalue('paraTemperatura')

distancia = form.getvalue('distancia')
dist_atual = form.getvalue('deDistancia')
dist_conversao = form.getvalue('paraDistancia')
result_temperatura = 0
result_dist = 0
if distancia == None:
    temperatura = float(temperatura)
    if temp_atual == temp_conversao:
        result_temperatura = temperatura
    
    if temp_atual == 'Celsius' and temp_conversao == 'Fahrenheit':
        result_temperatura = cel_fahr(temperatura)

    if temp_atual == 'Celsius' and temp_conversao == 'Kelvin':
        result_temperatura = cel_kel(temperatura)
        
    if temp_atual == 'Fahrenheit' and temp_conversao == 'Celsius':
        result_temperatura = fahr_cel(temperatura)

    if temp_atual == 'Fahrenheit' and temp_conversao == 'Kelvin':
        result_temperatura = fahr_kel(temperatura)

    print("Content-Type:text/html\r\n\r\n")
    print("<html> <body> ")
    print('%.2f %s equivalem a %.2f %s' %(temperatura, temp_atual, result_temperatura, temp_conversao))
    print("</body> </html>") 
    
if temperatura == None:
    distancia = float(distancia)
    if dist_atual == dist_conversao:
        result_dist = distancia
    
    if dist_atual == 'metros' and dist_conversao == 'centímetros':
        result_dist = metro_cm(distancia)

    if dist_atual == 'metros' and dist_conversao == 'quilômetros':
        result_dist = metro_km(distancia)
        
    if dist_atual == 'metros' and dist_conversao == 'decímetros':
        result_dist = metro_decimetro(distancia)

    print("Content-Type:text/html\r\n\r\n")
    print("<html> <body> ")
    print('%.2f %s equivalem a %.2f %s' %(distancia, dist_atual, result_dist, dist_conversao))
    print("</body> </html>")  
    

          







