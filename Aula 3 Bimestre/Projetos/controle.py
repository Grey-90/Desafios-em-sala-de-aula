sim = True
não = False

if sim:
    print("Entrou no if")
else: 
    print("Não entrou")

# ---------------------------------

resto = 5%2
print(resto)

# ---------------------------------
# imprimir número
# ---------------------------------

número = int(input("Digite um número: "))
resultado = número%2

if resultado == 0:
    print("Número par")
else:
    print("Número impar")

# ---------------

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
d = float(input("D = "))

if a > b:
    print("A é maior que B")
if a == b:
    print("A e B tem o mesmo valor")
if a != c:
    print("A e C são diferentes ")
if a < b:
    print("A é menor que B")
