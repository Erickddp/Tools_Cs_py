# Convierte numeros ordinarios a binarios. 
def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

# Imprime el resultado
numero = int(input("Introduce el numero que quieres convertir a binario: "))
print(binario(numero))

#Mantiene abierta la consola para verificar su respuesta.
input()