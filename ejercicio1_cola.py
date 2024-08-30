"""Escribir un codigo en el cual se comience con una lista vacia y se le pregunte
al usuario el tratamiento que se quiere dar. si el usuario ingresa pila 
se debera eliminar y mostrar uno a uno en el orden convencional de la pila.
hacer lo mismo pero en el orden de la cola para el caso que ingrese "cola" 
pensar para que estructura utilizaremos una pila o cola en un ejemplo cotidiano"""


lista=[]

def MenuPrincipal():
    print("agregar elemento ")
    print("1.Tratamiento Pila")
    print("2.Tratamiento cola")
    print("4.Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        elemento=input("ingresa un elemento:")
        lista.append (elemento)
    elif opcion =="2":
        print (" tramiento Pila")
        while lista:
            print (lista.pop())
    elif opcion== "3":
        print ( "tratamiento cola")  
        while lista:
            print (lista.pop())  
    elif opcion==            
   

