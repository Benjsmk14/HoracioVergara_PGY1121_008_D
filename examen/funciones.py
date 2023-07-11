import datetime
import time
import msvcrt
import os
import numpy
lista_asiento  = []
lista_rut      = []
lista_Platinum = []
lista_Gold     = []
lista_Silver   = []
Platinum = 0
Gold = 0
Silver = 0
cant_Platinum = 0
cant_Gold = 0
cant_Silver = 0
contador = 0
estadio = numpy.zeros((10,10),int)
hora_actual = datetime.datetime.now
def menu ():
    os.system('cls')
    print("""\t MENU
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir """)

def validar_opcion ():
    while True: 
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion in (1,2,3,4,5):
                return opcion
        except:
            print("ERROR! Debe ingresar números enteros")

def mostrar_estadio ():
    contador = 0
    print("\t\t\t\t ________________________")
    print("\t\t\t\t|                        |")
    print("\t\t\t\t|          show          |")
    print("\t\t\t\t|                        |")
    print("\t\t\t\t|________________________|")
    print("\t\t\t\t    1 2 3 4 5 6 7 8 9 10 - COLUMNAS")
    for x in range (10):
        contador += 1
        print("\t\t\t\t ", contador, end=" ")
        for y in range(10):
            print(estadio[x][y], end=" ")
        print(" ")
    print("\t\t\t\t |")
    print("\t\t\t\tFILAS")
    print("""LOS PRECIOS DE LAS ENTRADAS SON: 
         Platinum, $120.000. (FILAS del 1 al 2).
         Gold, $80.000. (FILAS del 3 al 5).
         Silver, $50.000. (FILAS del 6 al 10.).""")
    print("\nPRESIONE UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()
    

def comprar_entradas():
    if 0 not in estadio:
        print("LO SENTIMOS, NO QUEDAN ENTRADAS! :(")
        return
    mostrar_estadio()
    cant_entradas = validar_cantENT()
    for x in range(cant_entradas):
        rut = validar_rut()
        while True:
            fila = validar_filas()
            columna = validar_columnas()
            if estadio[fila-1][columna-1] == 0:
                precio_asientos(fila)
                estadio[fila-1][columna-1] = 1
                lista_asiento.append(estadio[fila-1][columna-1])
                print("HA COMPRADO EL ASIENTO CON EXITO!")
                print("ESPERE MIENTRAS LO REDIRIGIMOS...")
                time.sleep(3)
                break
            else:
                print("EL ASIENTO NO ESTA DISPONIBLE! :(")
        
    

def validar_filas ():
    while True:
        try:
            fila = int(input("Ingrese fila: "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("ERROR! Debe ingresar una fila entre 1-10!")
        except:
            print("ERROR! Debe ingresar número entero!")
def validar_columnas ():
    while True:
        try:
            columna = int(input("Ingrese columna: "))
            if columna in (1,2,3,4,5,6,7,8,9,10):
                return columna
            else:
                print("ERROR! Debe ingresar una columna entre 1-10!")
        except:
            print("ERROR! Debe ingresar número entero!")
def validar_rut():
    while True: 
        try:
            rut = int(input("Ingrese su rut (sin puntos ni digito verificador ): "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                if rut not in lista_rut:
                    print("Su rut se ha registrado con EXITO!")
                    print("ESPERE MIENTRAS LO REDIRIGMOS...")
                    time.sleep(2)
                    lista_rut.append(rut)
                    return rut
                else:
                    print("ERROR! EL RUT INGRESADO YA SE HA REGISTRADO!")
        except:
            print("ERROR! Debe ingresar solo números enteros ")

def validar_cantENT():
    while True: 
        try:
            entradas = int(input("Ingrese cantidad de entradas que desea comprar MAX. 3: "))
            if entradas <= 3:
                return entradas
        except:
            print("ERROR! Debe ingresar solo números enteros ")

def ver_listadoAsistentes():
    lista_rut.sort()
    print("Los asistentes de este evento son: ")
    print(lista_rut)
    print("\nPRESIONE UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()

def precio_asientos (fila):
    global Platinum 
    global Gold 
    global Silver 
    global cant_Platinum 
    global cant_Gold 
    global cant_Silver
    if fila >= 1 and fila<=2:
        Platinum += 120000
        cant_Platinum += 1
        return Platinum
    elif fila >= 3 and fila <=5:
        Gold += 80000
        cant_Gold += 1
        return Gold
    else:
        Silver += 50000
        cant_Silver += 1
        return Silver

def ver_ganancias ():
    os.system('cls')
    print("\t\t\t __________________________________________")
    print(f"""\t\t\t|  TIPO ENTRADA  |   CANTIDAD   |  TOTAL   |
\t\t\t--------------------------------------------
\t\t\t|   Platinum     |   {cant_Platinum}          | {Platinum} |
\t\t\t|   Gold         |   {cant_Gold}          | {Gold} |
\t\t\t|   Silver       |   {cant_Silver}          | {Silver} |  
\t\t\t|   Total        |   {cant_Platinum+cant_Silver+cant_Gold}           | {Platinum+Gold+Silver}|
\t\t\t--------------------------------------------""")
    
    print("\n PRESIONE UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()
def salir ():
    global hora_actual
    print("Horacio","Vergara", hora_actual)
