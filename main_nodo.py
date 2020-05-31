from p2pnetwork.node import Node

class nodo(Node):
    archivo = open("numeros.txt","w")#Creando txt con la información del cliente
    archivo.close()
    #Constructor
    def __init__(self, host, port):
        super(nodo, self).__init__(host, port, None)
        print("Nodo: Iniciado")

    def outbound_node_connected(self, node):
        print("Nodo saliente conectado: " + node.id)
        
    def inbound_node_connected(self, node):
        print("Nodo entrante conectado: " + node.id)

    def inbound_node_disconnected(self, node):
        print("Nodo entrante desconectado: " + node.id)

    def outbound_node_disconnected(self, node):
        print("Nodo saliente desconectado: " + node.id)

    def node_message(self, node, data):
        archivo = open("numeros.txt","a")#Creando txt con la información del cliente
        archivo.write("{},0".format(str(data)))
        archivo.close() 
        #print("Numero guardado")
        
    def node_disconnect_with_outbound_node(self, node):
        print("El nodo desea desconectarse de otro nodo saliente:" + node.id)
        
    def node_request_to_stop(self):
        print("Deteniendo nodo...")
        
