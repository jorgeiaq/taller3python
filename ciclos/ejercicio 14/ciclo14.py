print("bienvenido")
number19 = int(input("ingrese un numero: "))
number16 = int(input("ingrese un numero: "))

if number19 >= number16:
  print("el primer numero ingresado debeser menor que el primero")
else:
  for number in range(number19, number16 + 1):
    print("-", number)