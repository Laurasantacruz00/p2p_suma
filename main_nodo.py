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
        
