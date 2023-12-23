## Clases ##

class MyEmptyPerson:
    pass
print(MyEmptyPerson)


class Person:
    def __init__(self, name,surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name  # propiedad  privadas

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("Roro","Valdez")
print(my_person.full_name)
print(my_person.get_name()) #ingresado a leer propiedad privada
my_person.walk()

my_other_person = Person("Roy", "Bay", "Developer")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Hector de Leon (El loco de los perros)" #tener cuidado como tiene un tipado variado puede cambioar
print(my_other_person.full_name)

my_other_person.full_name = 666 #tener cuidado aqui tambien porque el tipado es dinamico
print(my_other_person.full_name)
