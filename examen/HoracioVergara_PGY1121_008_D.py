import funciones as fn

while True: 
    fn.menu()
    opcion = fn.validar_opcion()
    if opcion == 1:
        fn.comprar_entradas()
    elif opcion == 2:
        fn.mostrar_estadio()
    elif opcion == 3:
        fn.ver_listadoAsistentes()
    elif opcion == 4:
        fn.ver_ganancias()
    else:
        fn.salir()
        break