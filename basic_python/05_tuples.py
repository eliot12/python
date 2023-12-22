### Tuples ###

my_tuple = tuple()
my_other_tuple = []

my_tuple = (35, 1.77, "Roro", "Ramon", "Roro")
my_other_tuple = (80, 90, 100)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) Index Error
# print(my_tuple[-6]) Index Error

print(my_tuple.count("Roro")) #cuenta cuanto elementos se encuentra en la tupla
print(my_tuple.index("Ramon")) 
print(my_tuple.index("Roro")) 

# my_tuple [1] =  1.80   # He AQUI LA PRINCIPAL DIFERENCIA QUE UNA TUPLA NO MODIFICA LOS VALORES A DIFERENCIA DE LAS LISTAS es la principal diferenecia. 
my_suma_tuple = my_tuple + my_other_tuple
print(my_suma_tuple) # si se puede  concatenar se puede sumar ambas.

print(my_suma_tuple[3:6]) # busca los elementos entre esos indices

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] =  "iQlevel"
my_tuple.insert(1,"Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(tuple(my_tuple))    # es recomendable se tiene que trabajar con tuple hast el final en caso extremo se puede efectuar estos cambios


del my_tuple # elimina toda la tuple
## print(my_tuple)