import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from main_nodo import nodo

node_4 = nodo("142.44.246.12", 8004)

time.sleep(1)

node_4.start()

time.sleep(1)

node_4.connect_with_node('142.44.246.92', 8001)

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
            node_4.send_to_nodes(num)
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
            node_4.stop()
            print('end')
            break
    except ValueError:
        print("Porfavor, ingresa solo numeros")
