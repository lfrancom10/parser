def parser():
    #Abrir el archivo de las instrucciones
    print("entra")
    archivo = open("Robot.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    print("hola")
    for linea in lineas:
        linea = linea.strip()
        print(linea)

parser()