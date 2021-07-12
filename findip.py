import socket

#Revison rapida de dos datos escenciales; Nombre del ordenador e IP privada.
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

#Muestra la infromacion solicitada.
print("El nombre de tu ordenador es: " + hostname)
print("Tu direccion IP es: " + ip)

#Mantiene la consola abierta para poder verificar la informacion.
input()