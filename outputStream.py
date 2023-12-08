#outputStream

import threading
import random
import datetime
import time

dinero=2000
gasto=10 #de reposicion de stock

salida = 0
entrada = 0 

ingreso = 1000 #costo=1000 #del producto al cliente
stock = 100

#saber si el ingreso corresponde al mismo dia o contar los dias
dias_actividad = 0#dias de actividad de la empresa


faltante = 0
#si consume cliente, se termina-resta stock, / si coincide horario de trabajo existe venta y reposicion

horaria = datetime.timedelta(hours=0, minutes=0 , seconds=0)




def hora(tiempo_empresa):
    HORAS = int(tiempo_empresa)
    minutos_decimales = (tiempo_empresa - HORAS) * 60
    MINUTOS = int(minutos_decimales)
    segundos_decimales = (minutos_decimales - MINUTOS) * 60
    SEGUNDOS = int(segundos_decimales)

    # Convierte el número decimal en un objeto timedelta        
    tiempo_delta = datetime.timedelta(hours=HORAS, minutes=MINUTOS , seconds=SEGUNDOS)
    #print(type(tiempo_delta))
    return tiempo_delta

    

while True:
    time.sleep(0.1)
    bandera = False

    salida = 0

    vende = random.random()
    vende = vende < 0.5

    #bloque empresa
    tiempo_empresa = random.uniform(8,20)#trabaja entre 8 y 20 hs
    

    #bloque cliente
    consumo_cliente = random.uniform(0,24)#consume en cualquier momento

    #bloque proveedor
    consumo_proverdor = random.uniform(8,20)#consume cuando se termina stock





    if int(tiempo_empresa) == int(consumo_cliente):
        bandera = True
        
        if vende == True:
            entrada = ingreso
            salida = 0
            dinero = dinero + ingreso
            stock = stock - 1
            faltante = faltante + 1

    #generar hora de ingreso
    horario = hora(tiempo_empresa)
    if horario > horaria:
        horaria = horario
        dias_actividad += 1
    else:
        horaria = horario

    if stock < 100 and int(consumo_proverdor) == int(tiempo_empresa):
        bandera = True
        entrada = 0
        stock = stock + faltante
        salida = gasto*faltante
        dinero = dinero - salida
        faltante = 0
        #generar hora de egreso
        horario = hora(tiempo_empresa)
        if horario > horaria:
            horaria = horario
            dias_actividad += 1 #aumenta un dia
        else:
            horaria = horario



    if bandera == False:
        continue

    elif bandera == True:
        #organiza datos en variable
        datos = [dias_actividad, horario, entrada, salida, dinero]
        print(f'{datos[0]},{datos[1]},{datos[2]},{datos[3]},{datos[4]}')




'''

f'{t[0]}, {t[1]}, {t[2]}'

'''
