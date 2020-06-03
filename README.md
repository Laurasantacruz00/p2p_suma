# Red peer to peer

Para la realización de este taller se uso un paquete de python el tiene el nombre de p2pnetwork, se descargo usando el administrador de paquetes de python(pip) con el siguiente comando 

    pip install p2pnetwork

El cual fue creado por un profesor el cual pretendía que sus estudiantes entendieran como funciona blockchain, así mismo este paquete puede usarse para la implementación de aplicaciones como Bitcoin o para compartir archivos. 

Para la creación de un nodo debe contar con un servidor tcp/ip en un puerto
    
    node = nodo("142.44.246.12", 8004)
    
El cual permitira conectarse otros estos seran llamados "nodos salientes" 

    node.connect_with_node('142.44.246.92', 8001)

Al tener esta serie de nodos conectados se podra hacer envio de información en este caso numeros a los nodos salientes y entrantes de la siguiente forma 

    node.send_to_nodes(num)

# Creación de clase para realizar eventos (main_nodo)

Con esto claro se realizan dos codigos uno que funcionara para realizar los eventos requeridos por el nodo y el otro como la vista del cliente, para los eventos requeridos se llama el paquete y se importa de este el objeto "Node" El cual permitira la creación, conección y envío de mensajes entre nodos.

    from p2pnetwork.node import Node

class nodo(Node):
    archivo = open("numeros_1.txt","w")#Creando txt para los numeros a guardar
    archivo.close()
    archivo = open("numeros.txt","w")#Creando txt para los numeros a guardar
    archivo.close()
    #Constructor
    def __init__(self, host, port):
        super(nodo, self).__init__(host, port, None)#Creando nodo
        print("Nodo: Iniciado")

    def outbound_node_connected(self, node):
        print("Nodo saliente conectado: " + node.id)#Nodo al que se conecto
        
    def inbound_node_connected(self, node):
        print("Nodo entrante conectado: " + node.id)#Nodo que se conecto a este

    def inbound_node_disconnected(self, node):#Nodo al que se desconecto
        print("Nodo entrante desconectado: " + node.id)

    def outbound_node_disconnected(self, node):#Nodo que se desconecto a este
        print("Nodo saliente desconectado: " + node.id)

    def node_message(self, node, data):#Mensajes provenientes de los otros nodos
        if str(data) == "true":
            with open("numeros_1.txt", "r") as file:
                for line in file:
                    #fields = line.split(",")
                    data = line.rstrip("n")
                    #print(data)
            self.send_to_node(node, data)
        else:
            #print(str(data))
            num = data
            archivo = open("numeros.txt","a")#Creando txt con la información del cliente
            archivo.write("{},0".format(num))
            archivo.close() 
            numbers = []
            with open("numeros_1.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
                suma = sum(numbers)
            print("\nLa suma es: "+str(suma)) 

        
    def node_disconnect_with_outbound_node(self, node):
        print("El nodo desea desconectarse de otro nodo saliente:" + node.id)
        
    def node_request_to_stop(self):#Detener el nodo
        print("Deteniendo nodo...")
        


Todos los datos enviados y recibidos se enviaran en formato json generado por este mismo paquete. Cada nodo contara también con un numero de identificación generado por una función hash.

# Creación de nodos

Como primera instancia se hace la importación de varios modulos los cuales permitiran la manipulación del nodo en cuestiones de inicio, tiempo de ejecución y cierre de este.

También se llama la clase nodo la cual permitira por medio de funciones realizar eventos con el nodo.

    import sys
    import time
    sys.path.insert(0, '..') #Importando archivos donde se encuentran los modulos

    from main_nodo import nodo
    
Luego de esto se hace la creación del objeto nodo el cual será de tipo node y se le asignara una ip y un puerto, luego de darle un tiempo de espera a la ejecución del programa se hara inicio del nodo y luego se conectara al nodo siguiente de este:

    node = nodo("142.44.246.12", 8004) #Creación de nodo

    time.sleep(1)#Retrazando ejecución

    node.start()#Iniciando hilo

    time.sleep(2)#Retrazando ejecución

    node.connect_with_node('142.44.246.92', 8001)#Conectando con nodo 2

    time.sleep(1)#Retrazando ejecución

# Menu para el usuario

Se realizo un ciclo repetitivo el cual solo se detendra cuando el usuario lo decida, dentro de este se encuentran 3 opciones las cuales les permitiran ciertas acciones al usuario.

      while True:
          try: 
              #Menu
              print("\n_____________BIENVENIDO___________\n"
              +"\n Ingrese el numero de la acción que desea realizar:"
              +"\n1. Agregar numero \n2.Sumar numero \n3. Salir")

              op = int(input(" \n : "))#Opción elegida por el usuario 

              if op == 1:
                  #Agregar numero
                  num = input("\nEscriba el numero que desea agregar  ")#Numero a agregar 
                  archivo = open("numeros.txt","a")#Guardando numero en un txt
                  archivo.write("{},0".format(num))
                  archivo.close() 
                  print("Numero guardado")
                  node.send_to_nodes(num)#Enviando numero a los otros nodos 
              elif op == 2:
                  #Suma de los numeros
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
                  node.stop()
                  print('end')
                  break #Rompiendo ciclo
          except ValueError:
              #Control de errores 
              print("Porfavor, ingresa solo numeros")


Cabe resaltar que _Todos los nodos son iguales a excepción de sus conecciones_ 

# Suma de numeros 
Para realizar la suma de todos los numero primero el usuario debe seleccionar la opcion de suma, al hacer esto se envía a los nodos conectados el dato "true"

        node_2.send_to_nodes("true")
        time.sleep(2)
        
Al hacer esto lo que cada nodo verificiara es si recibio este dato, para esto se utiliza una condición donde si este dato es un "true" envíe los datos guardados en este nodo

    if str(data) == "true":
            with open("numeros_1.txt", "r") as file:
                for line in file:
                    #fields = line.split(",")
                    data = line.rstrip("n")
                    #print(data)
            self.send_to_node(node, data)
           
Si este dato no contiene un 3 debe obtener los numeros entonces estos se guardan en txt aparte de donde se guardan para el propio nodo

    else:
            #print(str(data))
            num = data
            archivo = open("numeros.txt","a")#Creando txt con la información del cliente
            archivo.write("{},0".format(num))
            archivo.close() 
            numbers = []
            with open("numeros_1.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
            with open("numeros.txt", "r") as file:
                for line in file:
                    fields = line.split(",")
                    #print(line.rstrip("n"))
                subnumbers = (int(field) for field in fields)
                numbers.extend(subnumbers)
                suma = sum(numbers)
            print("\nLa suma es: "+str(suma)) 
