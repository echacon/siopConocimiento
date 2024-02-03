from Logica import Redes_de_Petri
from Logica.Redes_de_Petri import leerRedNDR, RedPetri
import os

ruta = os.getcwd()
entradas = os.path.join(ruta,"DatosIniciales")
nomarchivo = os.path.join(entradas,"procesoCompra.ndr")
red = leerRedNDR(nomarchivo)
print(red.nombre)
for lugar in red.lugares:
    print (lugar.nombre, ' ', lugar.marcas)
for trans in red.transiciones:
    print( trans.nombre, ' ')
print("Arcos de entrada")
for arco in red.arcosEntrada:
    print(arco.lugar ,' ', arco.transicion)
print("Arcos de salida")
for arco in red.arcosSalida:
    print(arco.lugar ,' ', arco.transicion)
