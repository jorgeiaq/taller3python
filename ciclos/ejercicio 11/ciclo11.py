print("bienvenido")
print("numeros primos hasta un numero ingresado por el usuario")
number45 = int(input("ingrese un numero: "))

for number32 in range(2, number45 + 1):
  number_primo = True
  for division in range(2, int(number32**0.5) + 1):
    if number32 % division == 0:
      number_primo = False
      break

  if number_primo:
    print(number32)