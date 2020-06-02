from p2pnetwork.node import Node

class nodo(Node):
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
        archivo = open("numeros.txt","a")#Guardando numeros de nodos conectados
        archivo.write("{},0".format(str(data)))
        archivo.close() 
        #print("Numero guardado")
    
    def node_disconnect_with_outbound_node(self, node):
        print("El nodo desea desconectarse de otro nodo saliente:" + node.id)
    
    def node_request_to_stop(self):#Detener el nodo
        print("Deteniendo nodo...")
