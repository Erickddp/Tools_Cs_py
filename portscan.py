import sys
import socket

# Intrucciones generales y recomendaciones.
print("Esto se puede comprobar en windows con ___netstat -an___ \n Tambien se recomienda usar herramientas como METASPLOIT FRAMEWORK")

# input para la direccion ip, solo soporta ip privada.
objetivo = socket.gethostbyname(input("Inserte la direccion IP: "))
print("Escaneando objetivo: " + objetivo)

#Operacion
try:
    for port in range(1,150):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} esta abierto".format(port))
            s.close()

# Finalizacion.
except: 
    print("\n Saliendo...")
    sys.exit(0)

# Para que se quede en la consola al escanear los puertos.
input()
