# Descripción: Servidor que implementa una calculadora con funciones de suma, resta, multiplicación y división
import xmlrpc.server

# Se define la clase que contiene las funciones que se van a llamar desde el cliente
class Calculadora:

    # Funciones de suma
    def sumar(self, x, y):
        return x + y

    # Funciones de resta
    def restar(self, x, y):
        return x - y

    # Funciones de multiplicación
    def multiplicar(self, x, y):
        return x * y

    # Funciones de división
    def dividir(self, x, y):
        if y == 0:
            return "Error: No se puede dividir por cero"
        else:
            return x / y

# Creamos el servidor RPC
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(Calculadora())

# Iniciamos el servidor
print("Servidor calculadora en marcha en el puerto 8000...")
server.serve_forever()
