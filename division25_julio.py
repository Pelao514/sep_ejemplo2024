 a=4
 b=0
 try:
   print(a/b) # error division por cero / ZeroDivisionError
   
   
 except ZeroDivisionError:
   print("no se puede dividir")
    print(2+"2") # error typeError
    
 try: # sin conocer el tipo de error utilizamos exception( clase generica de python)
     print(2+"2") # Error TypeError
 except Exception:
     print("tiene un error")    