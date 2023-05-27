print("bienvenido")
print("suma de 100 numeros siguientes del numero ingresado por teclado")
number4 = int(input("ingrese un numero cualquiera: "))
addition = 0

for q in range(number4 + 1, number4 + 101):
    addition += q
print("la suma da como resultado:", addition)