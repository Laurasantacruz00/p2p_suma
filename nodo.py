import sys
import time
sys.path.insert(0, '..') #Importando archivos donde se encuentran los modulos

from main_nodo import nodo

node = nodo("127.0.0.1", 8001)#prueba

time.sleep(1)

node.start()

time.sleep(2)

node.connect_with_node('127.0.0.1', 8002)

time.sleep(1)

while True:
    try: 
        print("\n_____________BIENVENIDO___________\n"
        +"\n Ingrese el numero de la acción que desea realizar:"
        +"\n1. Agregar numero \n2.Sumar numero \n3. Salir")
        
        op = int(input(" \n : "))

        if op == 1:
            num = input("\nEscriba el numero que desea agregar  ")
            archivo = open("numeros.txt","a")#Creando txt con la información del cliente
            archivo.write("{},0".format(num))
            archivo.close() 
            print("Numero guardado")
            node.send_to_nodes(num)
        elif op == 2:
            numbers = []
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
                suma = sum(numbers)
            print("\nLa suma es: "+str(suma))
        elif op == 3:
            node.stop()
            print('end')
            break
    except ValueError:
        print("Porfavor, ingresa solo numeros")
    

