# incognitos
b = float(input("b = "))
a = float(input("a = "))
c = float(input("c = "))

#Processamento
Delta = b**2 - 4*a*c
Valor = Delta

#Valor do Delta

if Delta > 0:
    print("A Equação tem DUAS raízes reais")
elif Delta == 0:
    print("A Equação tem UMA")
else:
    print("A Equação NÃO possui raízes reais")

print(Valor)