## Sets ##
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente esto es un diccionario

my_other_set = {"Roro", "Ramon", 37}
print(type(my_other_set))

print(len(my_other_set))



my_other_set.add("iQlevel")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("iQlevel")
print(my_other_set) # Un set no permite repetidos datos

# busquedas con Set 

print("iQlevel" in my_other_set)  # efecuta buquedas si iQlvel existe en my_other_set
print("More" in my_other_set)

my_other_set.remove("iQlevel")   # si puede eliminar datos
print(my_other_set)

my_other_set.clear() # Elimina todos los elementos del set pero ese set sigue creado
print(len(my_other_set))

del my_other_set  #Elimina el set por completo
#print(my_other_set)

my_set = {"Roro","Ramon",37}
my_list =list(my_set)
print(my_list)
print (my_list[0])   #muy arriesgado para realizar operaiones

my_other_set = {"C#", "GO", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_set).union(my_set).union({"C++", "Html"})) #ignora lo que existe y aniade lo que falta

print(my_new_set.difference(my_set))