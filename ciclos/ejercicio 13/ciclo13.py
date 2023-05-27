print("bienvenido")

addition = 0
total = 0


while True:
  number99 = int(input("ingrese un numero al azar: "))
  number98 = int(input("ingrese un numero al azar: "))

  if number99 == 0 or number98 == 0:
    print("finalizo ejecucion")
    break

  total = number98 + number99
  addition += 1
  if addition >= 0:
    average = total / addition
    print("el promedio de la suma de los numeros es:", average)
else:
  print("ingrese un numero positivo")