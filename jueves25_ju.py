Ejemplo de diccionario realizado en clase virtual
#Hacer un código para manejar una base de datos para una empresa. Habrá un diccionario principal en el
# que la clave de cada cliente sera DNI y el valor sera otro diccionario con los datos del cliente
# (Nombre,Apellido y Correo).El programa debe preguntar al usuario por una opción del siguiente
# menú (1) Añadir cliente (2) eliminar, (3) Mostrar cliente,(4) Terminar

#a) Pedir los datos necesarios, agregar un cliente nuevo y mostrar el diccionario
#b) pedir un DNI y eliminar cliente. en caso de que NO exista, avisarlo por mensaje
#c) Pedir DNI y mostrar los datos en un mensaje

Clientes = {}

def MenuPrincipal():
    print("-----SISTEMA DE EMPRESA-----")
    print("1.Añadir Cliente")
    print("2.Eliminar Cliente")
    print("3.Mostrar Datos De Un Cliente")
    print("4.Finalizar Programa")
    opcion = input("Seleccione una opcion: ")
   
    if opcion == '1':
        AgregarCliente()
    elif opcion == '2':
        EliminarCliente()
    elif opcion == '3':
        MostrarCliente()
    elif opcion == '4':
        Clientes = {}
        print("Adios, vuelva pronto")
        return
    else:
        print("Opcion invalida, intentelo nuevamente: ")
        MenuPrincipal()

def AgregarCliente():
    Nombre = input("Ingrese el Nombre del cliente: ")
    Apellido = input("Ingrese el Apellido del cliente: ")
    DNI = int(input("Ingrese el DNI del cliente: "))
    Correo = input("Ingrese el correo del cliente: ")
   
    Datos = {
        "Nombre" : Nombre,
        "Apellido" : Apellido,
        "Correo" : Correo
    }
   
    Clientes[DNI] = Datos
    print(f"\nCliente Agregado correctamente")
    print(Clientes)
    MenuPrincipal()

def MostrarCliente():
    dni = int(input("Ingrese el DNI del cliente que desea mostrar los datos: "))
    if dni in Clientes:
        print("\nDatos del cliente: ")
        print(f"DNI: {dni}")
        print(f"Nombres: {Clientes[dni]['Nombre']}")
        print(f"Apellido: {Clientes[dni]['Apellido']}")
        print(f"Correo: {Clientes[dni]['Correo']}")
        MenuPrincipal()
    else:
        print("\nCliente no encontrado")
        MostrarCliente()

def EliminarCliente():
    dni = int(input("Ingrese el dni del cliente: "))
    if dni in Clientes:
        del Clientes[dni]
        print("\nCliente eliminado correctamente")
        MenuPrincipal()
    else:
        print('\nCliente No encontrado')
        EliminarCliente()
       
MenuPrincipal()