data_base={}
def add_customer():
    id_=int(input("\nIngrese el DNI del cliente: "))
    data_base.copy()
    name=str(input("Ingrese el nombre del cliente: "))
    surname=str(input("Ingrese el apellido del cliente: "))
    e_mail=str(input("Ingrese el correo electrónico del cliente: "))
    customer_data={"Nombre": name,
                   "Apellido":surname,
                   "Correo electrónico": e_mail}
    data_base[id_]=customer_data
    if id_ in data_base:
       print("\nCliente agredado con éxito.")
   
def delete_customer():
    id_=int(input("Ingrese el DNI del cliente a eliminar:  "))
    if id_ in data_base:
        data_base.pop(id_)
    else:
        print("Cliente inexistente.")
    print("Cliente eliminado con éxito")
       
def show_costumer():
    id_=int(input("Ingrese el DNI del cliente que desea visualizar: "))
    if id_ in data_base:
        print(data_base[id_])
       
def menu():
    print("\nBienvenido. Este es el menú de opciones:   ")
    while True:
        option=int(input("""\n
                         \t1-Añadir cliente.
                         \t2-Eliminar cliente.
                         \t3-Mostrar cliente.
                         \t4-Borrar datos y salir
                         \n\tIngrese el número de operación deseada:"""))
        if option==1:
         add_customer()
        elif option==2:
         delete_customer()
        elif option==3:
         show_costumer()
        elif option==4:
         print("\n¡Hasta luego!")
         data_base.clear()
         break
        else:
            print("\nOpcion incorrecta")