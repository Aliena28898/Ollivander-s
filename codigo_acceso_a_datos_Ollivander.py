"""Estos dos primeros métiodos van a permitir abrir un fichero de texto y extraer de él los casos test en forma de
matriz de 3 dimensiones [Primera dimensión: lista de los atributos del ítem. Segunda dimensión: lista de ítems de un día.
Tercera dimensión: lista de listas de cada día. Los casos test están escritos en la siguiente forma:

-------- día X --------
atributo1, atributo2, atributo3 (Nombre del. Ejemplo: Nombre, Caducidad, Calidad)
atributo1, atributo2, atributo3 (del primer ítem)
atributo1, atributo2, atributo3 (del segundo ítem y sucesivamente)
[*SALTO DE LÍNEA*]
---------día X+1--------
[...]

"""

def abrirFichero(rutaAccesoFichero):
    try:
        if not isinstance(rutaAccesoFichero, str):
            raise ValueError
        return open(rutaAccesoFichero, 'r')
    except FileNotFoundError:
        print("Fichero no encontrado")
        return []
    except ValueError:
        print("El nombre del fichero ha de ser un string")
        return []

def accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero):
    fichero = abrirFichero(rutaAccesoFichero)

    if fichero != []:
        matrizCasosTest = []
        numeroPropiedadesItem = 0
        for linea in fichero:
            if "day" in linea:
                casosTestDia = []
            elif linea == "\n":
                matrizCasosTest.append(casosTestDia)
            elif "name" in linea:
                numeroPropiedadesItem = len(linea.split(','))
            else:
                item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem - 1)
                casosTestDia.append(item)
        fichero.close()
        return matrizCasosTest


def crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest):

    try:
        if not isinstance(ficheroVolcadoCasosTest, str):
            raise ValueError
        stdout = open(ficheroVolcadoCasosTest, 'w')
    except ValueError:
            print("La ruta de acceso al fichero ha de ser un string")
    else:
        for (offset, casosTestDia) in enumerate(matrizCasosTest):
            stdout.write('-' * 5 + " Dia %d: " % offset + '-' * 5 + '\n')
            for item in casosTestDia:
                stdout.write(','.join(item) + '\n')
        stdout.close()


def mostrarCasosTest(matrizCasosTest):

    for (offset, casosTestDia) in enumerate(matrizCasosTest):
        print('-' * 5 + " Dia %d: " % offset + '-' * 5)
        for item in casosTestDia:
            print(item)


if __name__ == "__main__":

    rutaAccesoFichero = "./stdout.gr"
    # rutaAccesoFichero = "stdout_bug_conjured.gr"

    matrizCasosTest = []

    matrizCasosTest = accesoCasosTexttest(matrizCasosTest, rutaAccesoFichero)

    mostrarCasosTest(matrizCasosTest)

    ficheroVolcadoCasosTest = "./stdout.txt"

    crearFicheroCasosTest(ficheroVolcadoCasosTest, matrizCasosTest)
