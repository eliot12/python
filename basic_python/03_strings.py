# strings #
my_string = "Mi string"
my_other_string = 'Otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " "  + my_other_string)

my_new_line_string = "Este  es un String \n con salto de linea"
print(my_new_line_string)

my_tab_string = "\t Este es con string tabulacion"
print(my_tab_string)

my_scape_string = "\t Este es con string \n escapado"
print(my_scape_string)


# formateo #
name, surname, age = "Roro", "Perez", 12
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))           # Esta es simple

print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # De manera profesional se debe realizar el siguiente formato. 



# Desempaquetado de caracteres #

language = "python"
a,b,c,d,e,f = language
print(a)
print(b)


# Division 

language_slice =language[1:3]
print(language_slice)

language_slice =language[1:]
print(language_slice)

language_slice =language[-2]
print(language_slice)

language_slice =language[0:6:2]   # Ojo
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

print(" // ---- Funciones")
# funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("py"))