## funtions ##

def my_funtion():
    print("Esto es una funcion")

my_funtion()
my_funtion()
my_funtion()

def sum_two_values(firts_number, second_number):
    print(firts_number+second_number)

sum_two_values(5,10)
sum_two_values(1.5,1.3)

def sum_two_values_return(firts_number:int, second_number:int):
    my_suma = firts_number + second_number
    return my_suma

myresult = sum_two_values_return(10,5)
print(myresult)


def  print_name(name, surname):
    print(f"{name} {surname}")

print_name("Marco", "Robres")

def  print_name_with_deafult(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_deafult("Theo", "Burgoa")
print_name_with_deafult("Theo", "Burgoa","Rey")

def print_upper_texts(*texts): #De este tipo de dato puedes pasar lo que quieras
    for text in texts:
        print(text.upper())
print_upper_texts("Hola", "python","Network")
print_upper_texts("yeah")