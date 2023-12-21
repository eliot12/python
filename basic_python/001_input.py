first_name:str
age: int

first_name = input('Cual es tu nombre ?')
age = input('Cual es tu edad ?')

print(first_name)
print(age) 

# Forzamos el tipo de variable EN todo caso el tipado es dinanico
first_name = "s"
print(first_name)

first_name = 100 
age = False 

print(first_name)
print(age)

print(type(first_name))
print(type(age))     