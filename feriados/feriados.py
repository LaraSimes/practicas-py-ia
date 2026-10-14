import requests
from datetime import date  
import csv

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

if restantes: 
    proximo = restantes[0] #Obtiene el primer feriado de la lista de feriados restantes
    fecha_proximo = date.fromisoformat(proximo["fecha"]) #Convierte la fecha del proximo feriado a un objeto date
    dias_restantes = (fecha_proximo - hoy).days #Calcula la cantidad de dias restantes hasta el proximo feriado
    print(f"El proximo feriado es {proximo['nombre']} el {fecha_proximo.strftime('%d/%m/%Y')}, faltan {dias_restantes} días.") #Imprime el nombre del proximo feriado, su fecha y la cantidad de dias restantes

else:
    print("No hay feriados restatantes este año")

with open("feriados_restantes.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["fecha", "nombre", "tipo"])
    for feriado in restantes:
        escritor.writerow([feriado["fecha"], feriado["nombre"], feriado["tipo"]])

print("CSV guardado: feriados_restantes.csv")