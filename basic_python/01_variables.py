# Variables
my_str_variable = "My String variable"
print(my_str_variable)

my_int_variable = 10
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Imprime varias variables concatenacion
 
print(my_str_variable, my_int_variable, my_bool_variable)

# Convirtiendo con entero a String

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Algunas Funciones del sistema
print(len(my_str_variable))

print("Ese es una variable:", my_bool_variable)

# Variables en una sola linea NO ES TAN BUENO ESTA SINTAXIS
name, surname, alias, age = "Eliot", "Torrez", "NewDev", 37 
print("Me llamo:",name,surname, ". Mi edad es", age, "y mi alias es:", alias)