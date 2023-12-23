## listas ##

my_list = list() #Formas de definir 1
my_other_lis = []   #Formas de deinir 2

print(len(my_list)) 

my_list = [35 , 24, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_lis =[31,1.77,"Roro","Ramon"]
print(type(my_other_lis))
print(my_other_lis) # Un array no es lo mismo que un lista pero son iguales

print(my_other_lis[0])
print(my_other_lis[1])
print(my_other_lis[-1])
print(my_other_lis[-4])

print(my_list.count(30)) #sirve para contar cuantas veces se repite

#print(my_other_lis[4]) Index error
#print(my_other_lis[-5]) Index error


age, heigth, name, surname = my_other_lis #no aconcejable
print(name)

print(my_list + my_other_lis)

#Tener en cuenta con el tipado dinamico

my_other_lis.append("chocho")
print(my_other_lis)

my_other_lis.insert(0,"azul")
print(my_other_lis)