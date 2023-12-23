### loops  o tambien se denomina ciclos o bucles ###

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Solo en python existe el false en while    ADEMAS ES OPCIONAL
    print("Mi condicion es mayor o igual a 10")  
print("La ejecution continua")

while my_condition < 20:
    my_condition += 1

    if my_condition == 15: 
        print("Se detienen la ejecucion")
      #  break
    print("Mi condicion es menor que 20")



# for
    my_list = [35, 24, 20, 54, 34,1]

    for element in my_list:
        print (element)

    my_tuple = (35, 1.77, "Roro", "Perez", "Ramon")

    for element in my_tuple:
        print (element)

    my_set = {"Roro", "Chavo", 45}
    for element in my_set:
        print (element)

    my_dict = {"Nombre":"Florinda", "Apellido":"Mesa", "Edad":35, 1:"Peso"}
    for element in my_dict:
        print (element)

    for element in list(my_dict.values()):
        print(element)
    else:
        print("El bucle for ha terminado")

    for element in my_dict:
        print(element)
        if element == "Edad":
            break
        print("Se ejecuta")

    else:
        print("El bucle for ha terminado")
    
for element in my_dict:
    print(element)
    if element == "Edad":
       continue # Los lenguajes modernos no se utiliza ya no es aconcejable
    print("Se ejecuta")
        
else:
    print("El bucle for ha terminado")
    