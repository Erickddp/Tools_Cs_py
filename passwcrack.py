import hashlib

# Primeras dos instrucciones en que se solicita el HASH y el diccionario.
encontrada = 0
input_hash = input("Inserte la contraseña hasheada:  ")
pass_doc = input("Inserte el diccionario: ")


# Operacion de busqueda.
try:
    pass_file = open(pass_doc, 'r')
except:
    print("Error: " + pass_doc + " no ha sido encontrada") 

for palabra in pass_file:
    palabra_cifrada = palabra.encode("utf-8")
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()


# En caso de ser encontrada la contraseña
    if digest == input_hash:
        print("Contraseña encontrada!!! \n \tLa contraseña es: " + palabra)
        break
# En caso de no ser encontrada.
if not encontrada:
    print("Contraseña no encontrada en el archivo " + pass_doc)

input()