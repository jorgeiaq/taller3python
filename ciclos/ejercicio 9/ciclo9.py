print("bienvenido")
print("numero factorial del numero ingresado por teclado")
number3 = int(input("ingrese un numero: "))
factorial = 1
for z in range(1, number3 + 1):
   factorial *= z
print("el factorial es:", factorial)