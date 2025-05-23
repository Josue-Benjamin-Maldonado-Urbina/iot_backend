import requests
import random
import time
from datetime import datetime

URL = 'http://127.0.0.1:8000/api/sensores/'  # Cambia esto si usas otro puerto o dominio

def simular_lectura():
    humedad = round(random.uniform(20, 80), 1)
    riego = humedad < 40  # Si la humedad es baja, se simula que se activa el riego
    return {
        "humedad": humedad,
        "riego_activado": riego
    }

while True:
    datos = simular_lectura()
    response = requests.post(URL, json=datos)

    if response.status_code == 201:
        print(f"[{datetime.now()}] ✅ Registro enviado: {datos}")
    else:
        print(f"[{datetime.now()}] ❌ Error al enviar: {response.status_code} - {response.text}")

    time.sleep(10)  # Espera 10 segundos antes de volver a enviar datos
