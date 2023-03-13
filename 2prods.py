import queue
import threading
import time
import random

cola = queue.Queue() # Creamos una cola
consumed_items = 0 # Inicializamos la variable que llevará la cuenta de los items consumidos
start_time = time.time() # Guardamos el tiempo de inicio del programa

# Definimos la función del productor
def productor():
    global consumed_items # Indicamos que vamos a usar la variable global
    while True:
        # Verificamos si ya se consumieron los 100 items
        if consumed_items == 30:
            end_time = time.time() # Guardamos el tiempo de finalización del programa
            elapsed_time = end_time - start_time # Calculamos el tiempo transcurrido
            print(f"Se han consumido los 30 items. El productor se detendrá. Tiempo transcurrido: {elapsed_time:.2f} segundos.")
            break
        item = random.randint(1, 10) # Generamos un número aleatorio
        cola.put(item) # Añadimos el número a la cola
        print(f"El productor ha producido el item {item}")
        time.sleep(0.1) # Esperamos un tiempo aleatorio antes de producir el siguiente item

# Definimos la función del consumidor
def consumidor():
    global consumed_items # Indicamos que vamos a usar la variable global
    while True:
        item = cola.get() # Obtenemos un item de la cola
        consumed_items += 1 # Incrementamos el contador de items consumidos
        print(f"El consumidor ha consumido el item {item}")
        cola.task_done() # Indicamos que hemos completado el procesamiento del item
        time.sleep(0.1) # Esperamos un tiempo aleatorio antes de procesar el siguiente item
        # Verificamos si ya se consumieron los 100 items
        if consumed_items == 30:
            end_time = time.time() # Guardamos el tiempo de finalización del programa
            elapsed_time = end_time - start_time # Calculamos el tiempo transcurrido
            print(f"Se han consumido los 30 items. El consumidor se detendrá. Tiempo transcurrido: {elapsed_time:.2f} segundos.")
            break

# Creamos los threads para el productor y el consumidor
productor_thread = threading.Thread(target=productor)
consumidor_thread = threading.Thread(target=consumidor)
#crear otro productor y otro consumidor
productor2_thread = threading.Thread(target=productor)
consumidor2_thread = threading.Thread(target=consumidor)

#iniciarlos
productor2_thread.start()
consumidor2_thread.start()

# Iniciamos los threads
productor_thread.start()
consumidor_thread.start()

# Esperamos a que la cola esté completamente vacía antes de continuar
cola.join()