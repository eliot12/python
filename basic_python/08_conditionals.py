## conditionals ##

my_condition = False

if my_condition: # es lo mismo que if my_condition == true
    print("Se ejectua la condicion del if")

print("La ejecucion continua")

my_condition = 5*5

if my_condition == 10:
     print("Se ejectua la condicion del segundo if")

if my_condition > 10 and my_condition < 20:
     print("Es mayor que 10 y menor que 20")

elif my_condition == 25:
    print("es igual a 25")
else:
     
    print("Es menor igual que 10 o mayor a 20 o distinto de 25")


my_string = ""

if not my_string:
    print("Mi cadena de testo es vacia")

if my_string == "Mi cadena de textooo":
    print("Estas cadenas de texto coinciden")
