print("bienvenido")

number = int(input("ingrese un numero: "))
number2 = int(input("ingrese un numero: "))


for y in range(number + 1):
  for t in range(y, number2 + 1):
    print(f"{y}-{t}")