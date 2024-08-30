# cola criterio FIFO primero elemento en ingresar es primer elemento en salir 

cola= []
cola= ["juan","Pedro","Maria"]
print (cola)

#agregar elemnetos de cola

cola.append ("Gustavo")
cola.append ("Vanesa")
print (cola)

# sacar elementos de cola

salida= cola.pop(0)
print(f"Atendiendo a  {salida}")  # f str 

salida= cola.pop(0)
print(f"Atendiendo a {salida}")
print(cola)