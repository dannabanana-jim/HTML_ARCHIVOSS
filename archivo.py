print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("3ro-W")
print (" ")

#1.-Abre el archivo indicado, devuelve
archivo = open("ALUMNO.txt", "r")# abro mi archivo de texto para solo lectura
print (archivo.read())
archivo.close() 

print(" ")

#2.-Para abrir el archivo, utilice la función incorporada open().
#La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:

archivo = open("ALUMNO.txt", "r")
print(archivo.read(1))

print(" ")

#3.-Si el archivo se encuentra en una ubicación diferente, deberá especificar la ruta del archivo, de esta manera:
#Abrir un archivo en una ubicación diferente:
archivo = open("e:\documento_demostracion.txt", "r")
print(archivo.read())

print(" ")

#4.-Leer solo partes del archivo
#De forma predeterminada, el read()método devuelve el texto completo,
# pero también puedes especificar cuántos caracteres quieres devolver:

archivo = open("ALUMNO.txt", "r")
print(archivo.read(8))

print(" ")

#5.-Escritura de archivos en Python❮ AnteriorPróximo ❯Escribir en un archivo existente
#Para escribir en un archivo existente, debe agregar un parámetro a la open()función:
#"a"- Anexar - se agregará al final del archivo
#"w"- Escribir: sobrescribirá cualquier contenido existente

archivo = open("ALUMNO.txt", "a")
archivo.write("¡Ahora el archivo tiene más contenido!")
archivo.close()

#Abra y lea el archivo después de agregar:
archivo = open("ALUMNO.txt", "r")
print(archivo.read())

print(" ")

#6.-Abra el archivo "ALUMNO.txt" y sobrescriba el contenido:
archivo = open("ALUMNO.txt", "w")
archivo.write("¡Ups! he eliminado el contenido!")
archivo.close()

print(" ")

# Abra y lea el archivo después de sobrescribirlo:
archivo = open("ALUMNO.txt", "r")
print(archivo.read())


print(" ")

#7.-liminar archivo de Python❮ AnteriorPróximo ❯Eliminar un archivo
#Para eliminar un archivo, debes importar el módulo del sistema operativo y ejecutar su os.remove()función:
#Eliminar el archivo "ALUMNO.txt":

import os
os.remove("ALUMNOss.txt")

print(" ")

#8.-Comprobar si el archivo existe:
#Para evitar obtener un error, es posible que desees verificar si el archivo existe antes de intentar eliminarlo
#Comprueba si el archivo existe  elimínalo:
import os
if os.path.exists("ALUMNO .txt"):
    os.remove("ALUMNO.txt")
else:
    print(" El archivo si existe")

print(" ")

#9.-Eliminar carpeta
#Para eliminar una carpeta entera, utilice el os.rmdir()método:
#Ejemplo
#Eliminar la carpeta "pollito":
import os
os.rmdir("pollito.txt")


print(" ")

