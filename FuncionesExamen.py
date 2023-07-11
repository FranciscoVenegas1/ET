import os
import numpy as np 
def llenar(piso,Opcion):
    p=1
    for i in range(10):
        for j in range(4):
            piso[i,j]=p 
            Opcion[i,j]=p 
            p+=1 
def opciones():
    pp=0
    while(True):
        try:
            pp=int(input("   Elija opción: "))
            if(pp>=1 and pp<=5):
                break
            else:
                print("Debe ingresar una opción entre 1 y 5")
        except ValueError:
            print("Debe ingresar un número entero")
    return pp 
def mostrarDisponibles(aa):
    os.system("cls")
    for i in range(10):
        print("\n")
        for j in range(4):
            if(j==1 or j==4):
                print("\t",aa[i,j], end="        ")
            else:
                print("\t",aa[i,j], end="   ")
    print("\n\n")
def DeptosDispo():
    os.system("cls")
    dispo=""
    while(len(dispo)<=0):
        print("Tipo A")
        print("Tipo B")
        print("Tipo C")
        print("Tipo D")
        print()
        dispo=input("   Elija el tpo de departamento").lower()
        if(dispo!="Tipo A" and dispo!="Tipo B" and dispo!="Tipo C" and dispo!="Tipo D"):
            print("Debe ingresar una opcion correcta")
            dispo=""
    return dispo 
def validaDepto():
    depto=0
    while(True):
        try:
            depto=int(input(" Ingrese el piso y tipo de depto que desea: "))
            if(depto>=1 and depto<=40):
                break
            else:
                print("Error debe ingresar un departamento de los mostrados")
        except ValueError:
            print("Debe ser un número entero")
    return depto 
def disponible(piso,Opcion):
    for i in range(10):
        for j in range(4):
            if(piso==Opcion[i,j]):
                return True
    return False
def comprarDepto(aa,departamento,dd, Opcion,ListCompradores):
    if(dd=="departamento tipo A"):
        pago=137163432
    if(dd=="departamento tipo B"):
        pago=108286920
    if(dd=="departamento tipo C"):
        pago=101067792
    if(dd=="departamento tipo D"):
        pago==126334740    
    for i in range(10):
        for j in range(4):
            if(departamento==aa[i,j]):
                while(True):
                    while(True):
                        try:
                            rut=int(input("Ingrese su rut, debe tener minimo 8 numero y sin DV"))
                            if(rut<9999999):
                                print("Error, debe tener 8 dígitos mínimo")
                            else:
                                break
                        except ValueError:
                            print("Debe ser número entero")
                    if(len(ListCompradores)>0): 
                        sw=0
                        for y in range(len(ListCompradores)):
                            if(rut==ListCompradores[y]):
                                sw=1
                        if(sw==1):
                            print("Este rut ya esta registrado")
                        else:
                            ListCompradores.append(rut)
                            break
                    else:
                        ListCompradores.append(rut)
                        break
                aa[i,j]="x"
                if(i>=0 and i<=2):
                    pago+=50000
                elif(i>=3 and i<=7):
                    pago+=20000
                elif(i>=11 and i<=12):
                    pago-=10000
                Opcion[i,j]=pago
            
    return pago
def totalVentaDeptos(aa):
    suma=0
    for i in range(10):
        for j in range(4):
            if(aa[i,j]!=0 and aa[i,j]>40):
                suma+=aa[i,j]
    return suma
def Listado(r):
    r.sort()
    print("Listado de compradores ")
    print("\t",r)













