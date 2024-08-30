""" Escribir un programa que cree un diccionario vacío y lo vaya llenado con
 información sobre una persona. Esta información se le va a ir pidiendo al
#usuario el cual deberá completar los campos de “nombre”, “apodo” y “teléfono”.  
 Cada vez que se añada un nuevo dato debe imprimirse el contenido del
 diccionario completo """
 
 # difinir dccionario vacio 
persona={}
 
 # funcion añadir personas
def agregar_persona ():
     dni=int(input("ingrese el numero de dni"))
     nombre=str(input("ingrese nombre:")) 
     apodo=str(input("ingrese apodo:"))
     telefono=int(input("ingrese telefono:"))
     
# creamos el diccionario con los datos de la persona 
     datos_personal ={
        "nombre":nombre,
        "apodo" :apodo,
        "telefono": telefono
        
    } 
   
# agregamos los datos personal al dicionario principal
     persona[dni]=datos_personal  
    
# mostramos el dicionario con los datos cargados
     print("datos personales cargados correctamente")
     print (persona)  
  
# Llamamos lafuncion agragar personas
cantidad_registro = int(input("ingrese la cantidad de personas a registarar"))
for numero in range (cantidad_registro):
    agregar_persona()   
 
 
 # opcion 2 while cargar hasta tener una repuesta de cargar
continuar =True
while continuar: 
    agregar_persona()
    repuesta =input ("desea agreagr otra persona? (S/n)")
    if repuesta == "n":
        continuar = False
        
