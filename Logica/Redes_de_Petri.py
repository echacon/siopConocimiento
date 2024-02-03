# Red de Petri. La marcacion inicial esta dada por la cantidad de marcas en los lugares
class RedPetri:
    nombre = ''
    lugares = []
    transiciones = []
    arcosEntrada = []
    arcosSalida = []
class Lugar:
    nombre = ''
    marcas = 0
class Transicion:
    nombre = ''
class ArcoEntrada:
    lugar = ''
    transicion = ''
    peso = 1
    inhibidor = False
class ArcoSalida:
    transicion = ''
    lugar = ''
    peso = 1
nombrelugar = []
nombretransicion = []

def leerRedNDR(nombrearchivo):
    archivo = open(nombrearchivo)
    red = RedPetri()
    lineas = archivo.readlines()
    for linea in lineas:
        campos = linea.split()
        if len(campos) > 0:
            match campos[0]:
                case 'p':
                    lugar = Lugar()
                    lugar.nombre=campos[3]
                    lugar.marcas=campos[4]
                    red.lugares.append(lugar)
                    nombrelugar.append(campos[3])
                case 't':
                    trans=Transicion()
                    trans.nombre = campos[3]
                    red.transiciones.append(trans)
                    nombretransicion.append(campos[3])
                case 'e':
                    if campos[1].startswith('p'):
                        arco = ArcoEntrada()
                        arco.lugar= campos[1]
                        arco.transicion=campos[2]
                        red.arcosEntrada.append(arco)
                    else:
                        arco = ArcoSalida()
                        arco.lugar= campos[2]
                        arco.transicion=campos[1]
                        red.arcosSalida.append(arco)
                case 'h':
                    red.nombre = campos[1]
    return red



    
