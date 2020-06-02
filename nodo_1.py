import sys
import time
sys.path.insert(0, '..') #Importando archivos donde se encuentran los modulos

from main_nodo import nodo

node_1 = nodo("142.44.246.92", 8001)#Creación de nodo

time.sleep(1)#Retrazando ejecución

node_1.start()#Iniciando hilo

time.sleep(2)#Retrazando ejecución

node_1.connect_with_node('142.44.246.23', 8002)#Conectando con nodo 2

time.sleep(1)#Retrazando ejecución

while True:
    try: 
        #Menu
        print("\n_____________BIENVENIDO___________\n"
        +"\n Ingrese el numero de la acción que desea realizar:"
        +"\n1. Agregar numero \n2. Sumar numero \n3. Salir")
        
        op = int(input(" \n : "))#Opción elegida por el usuario 

        if op == 1:
            num = input("\nEscriba el numero que desea agregar  ")#Numero a agregar 
            archivo = open("numeros.txt","a")#Guardando numero en un txt
            archivo.write("{},0".format(num))
            archivo.close() 
            print("Numero guardado")
            node_1.send_to_nodes(num)#Enviando numero a los otros nodos 
        elif op == 2:
            numbers = []
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")#Recorriendo archivo txt
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)#Separando numeros
                numbers.extend(subnumbers)
                suma = sum(numbers)#Sumando numeros
            print("\nLa suma es: "+str(suma))#Respuesta
        elif op == 3:
            #Deteniendo nodo
            node_1.stop()
            print('end')
            break#Rompiendo ciclo
    except ValueError:
        #Control de errores
        print("Porfavor, ingresa solo numeros")
    
