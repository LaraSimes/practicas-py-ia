import requests

URL = "https://api.argentinadatos.com/v1/feriados/2026"

respuesta = requests.get(URL, timeout=10) #Realiza la solicitud GET a la API con un tiempo de espera maximo de 10 segundos 
feriados = respuesta.json() #Convierte la respuesta en formato JSON a un diccionario de Python

print("Cantidad de feriados: ", len(feriados))
print("El primer feriado es: ", feriados[0])
print("Su nombre es: ", feriados[0]['nombre'])