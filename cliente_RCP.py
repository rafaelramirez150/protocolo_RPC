# Descripción: Cliente que se conecta al servidor RPC y utiliza las funciones de la calculadora
import xmlrpc.client

# Conexión con el servidor RPC
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Ejemplo de uso de las funciones de la calculadora
resultado_suma = proxy.sumar(5, 3) # suma
print("Suma: ", resultado_suma)

resultado_resta = proxy.restar(10, 3) # resta
print("Resta: ", resultado_resta)

resultado_multiplicacion = proxy.multiplicar(4, 5) # multiplicación
print("Multiplicación: ", resultado_multiplicacion)

resultado_division = proxy.dividir(10, 2) # división
print("División: ", resultado_division)
