## Dicctionaries ##

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Roro","Apellido":"Valdez","Edad":39, 1:"Python"}

my_dict = {"Nombre":"Roro",
           "Apellido":"Valdez",
           "Edad":39, 
           "Lenguajes":{"Python", "Java", "Koltin"},
           1:1.79
           }

print(my_other_dict)
print(my_dict)

print(my_dict["Nombre"])
my_dict["Nombre"] = "Pedro"  # Actualizamos el elemento
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Av. Argentina"  # forma de aniadir un elelemanto
print(my_dict)

del my_dict["Calle"] # forma de eliminar un elemento
print(my_dict)

print("Roro" in my_dict)
print("Apellido" in my_dict) #Busca por las vairables

print(my_dict.items()) # Retorna toda la estructura
print(my_dict.keys())  # Retorna todas las claves
print(my_dict.values()) # Retorna los valores

my_new_dic = dict.fromkeys(("Nombre", 1))
print(my_new_dic)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,"Pepe") #asiga un valor a todas las claves
print(my_new_dict)