import requests
from datetime import date  

URL = "https://api.argentinadatos.com/v1/feriados/2026"

respuesta = requests.get(URL, timeout=10) #Realiza la solicitud GET a la API con un tiempo de espera maximo de 10 segundos 
feriados = respuesta.json() #Convierte la respuesta en formato JSON a una lista de diccionarios de Python

hoy = date.today() #Obtiene la fecha actual
restantes = [] #todavia no hay ninguno en la lista 

for feriado in feriados: #Itera sobre cada feriado en la lista de feriados
    fecha = date.fromisoformat(feriado["fecha"]) #para convertir la fecha (string) a date 
    if fecha >= hoy:
        restantes.append(feriado) #Agrega el feriado a la lista de feriados restantes si es mayor o igual a la fecha actual

print(f"Quedan: {len(restantes)} feriados hasta fin de año.") #Imprime la cantidad de feriados restantes hasta fin de año