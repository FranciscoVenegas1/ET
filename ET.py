import os
import numpy as np 
import FuncionesExamen as fa 
piso=np.empty([10,4],type(int))
Opcion=np.empty([10,4],type(int))
ListCompradores=[]
fa.llenar(piso,Opcion)
op=0
tipo=0
suma=0
while(op!=5):
    os.system("cls")
    print("    Inmobliliaria Casa feliz    ")
    print("     **********************     ")
    print(" 1.  Comprar departamento ")
    print(" 2.  Mostrar departamentos disponibles ")
    print(" 3.  Ver listado de compradores ")
    print(" 4.  mostrar ganancias totales ")
    print(" 5.  Salir ")
    op=fa.opciones()
    if(op==1):
        fa.comprarDepto(piso)
        os.system("pause")
    if(op==2):
        dd=fa.comprarDepto()
        fa.mostrarDisponibles(piso)
        Departamento=fa.validaDepto()
        cc=fa.DeptosDispo(piso,tipo)
        if (cc):
            print("Departamento Disponible")
            pagar=fa.comprarDepto(piso,Opcion,dd, tipo,ListCompradores )
            print("\t Total a pagar: $", pagar)
            os.system("pause")
    if(op==3):
        fa.Listado(ListCompradores)
        os.system("pause")
    if(op==4):
        suma=0
        suma=fa.totalVentaDeptos(Opcion)
        if(suma==0):
            print("\t No se han vendido departamentos aún")
        else:
            print("\t El total vendido hasta ahora es de : $", suma)
        os.system("pause")
    if(op==5):
        print("Hasta luego :)")












