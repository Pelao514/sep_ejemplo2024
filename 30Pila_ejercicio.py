pila=[]
def mostrar_menu ():
    print ("CREADOR DE PILAS ¿ Que quiere hacer ?")
    print ("0.Salir")
    print ("1.Apilar")
    print ("2.Desapilar")
    print ("3.Numero de elementos")

def pedir_opcion():
    print("ingrese la opcion (0-1-2-3):")
    opcion = int(input())    
    while opcion <0 or opcion > 3:
        print ("opcion incorrecta. Ingrese una valida:")
        opcion= int(input())
    return opcion

def apilar_elemento ():
    print ("Ingrese el elmentoa apilar:")    
    elemento = input ()
    pila.append (elemento)
    
def desapilar_elemento():
    print ("Eleminado el siguiente elemento...") 
    print (pila.pop ())   

def mostrar_tamaño ():
    print("Mostrando tamaño...")
    print (pila.__len__ ())
    
def creador_pila ():
    mostrar_menu ()
    opcion = pedir_opcion ()
    hacer_accion(opcion)
    print ("Presione ENTERpara continuar...")
    input()
    
def hacer_accion(opcion):
    if opcion ==1:
        apilar_elemento()
    elif opcion ==2:
        desapilar_elemento()
    elif opcion ==3:
        mostrar_tamaño()


mostrar_menu ()
opcion =pedir_opcion()
hacer_accion (opcion)
print ("Presione ENTER para continuar ...") 
input () 
while opcion!=0:
    mostrar_menu()
    opcion= pedir_opcion()
    hacer_accion (opcion)
    print ("Presione ENTERpara continuar...")
    input()
                          
      
        