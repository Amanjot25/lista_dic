#coding:utf8

x=13
meses = (0, 'Enero', 'Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
while x != 0:
    x = int(input("Dime un número"))
    if x >= len(meses):
        print("Impossible")
        continue
    elif x < 0:
        print("Impossible")
        continue
    elif x == 0:
        break
    print(meses[x])
print("FIN")


