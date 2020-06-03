import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from main_nodo import nodo

node_2 = nodo("127.0.0.1", 8002)

time.sleep(1)

node_2.start()

time.sleep(1)

node_2.connect_with_node('127.0.0.1', 8003)
node_2.connect_with_node('127.0.0.1', 8004)

time.sleep(1)

while True:
    try: 
        print("\n_____________BIENVENIDO___________\n"
        +"\n Ingrese el numero de la acción que desea realizar:"
        +"\n1. Agregar numero \n2.Sumar numero \n3. Salir")
        
        op = int(input(" \n : "))

        if op == 1:
            num = input("\nEscriba el numero que desea agregar  ")
            archivo = open("numeros_1.txt","a")#Creando txt con la información del cliente
            archivo.write("{},0".format(num))
            archivo.close() 
            print("Numero guardado")
        elif op == 2:
            node_2.send_to_nodes("true")
            time.sleep(2)
            ''' numbers = []
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
                suma = sum(numbers)
            print("\nLa suma es: "+str(suma)) '''
        elif op == 3:
            node_2.stop()
            print('end')
            break
    except ValueError:
        print("Porfavor, ingresa solo numeros")
    
    
