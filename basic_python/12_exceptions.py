## exceptions handling - manejo de errores ##


number_one = 5
#number_two = 1
number_two = "1"


# try except
try:   #para excepcionar errore
    print(number_one + number_two)
    print("No se ha producido un error")

except:
    print("Se ha producido un error")




# try except else finaly
try:   #para excepcionar errore
    print(number_one + number_two)
    print("No se ha producido un error")

except:
    # Se ejecuta si produce una excepcion 
    print("Se ha producido un error")
else: #opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally: #opcional
    # Se ejecuta siempre
    print("La ejecucion continua")


#Exceptiones por tipo 

try:   
    print(number_one + number_two)
    print("No se ha producido un error")

except ValueError:
    print("Se ha producido un ValuError")

except TypeError:
    print("Se ha producido un TypeError")


# Captura de la informacion de la excepcion
try:   
    print(number_one + number_two)
    print("No se ha producido un error")

except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)

