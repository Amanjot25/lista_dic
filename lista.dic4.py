#coding:utf8

print("Dime numeros, 0 para finalizar la lista")
lista = []
num = input()
while num != 0:
    lista.append(num)
    num = input()
print("Numeros introducidos son: ") #ordena la lista
print(sorted(lista))
