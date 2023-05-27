print("bienvenido")
print("tabla de multiplicacion")

multiplication = int(input("ingrese un numero del 1 al 10: "))
print("la tabla de multiplicacion que escogio es:", multiplication)
if multiplication == 1:
  for q in range(1, 11):
    resultd1 = multiplication * q
    print(multiplication, "x", q, "=", resultd1)

elif multiplication == 2:
  for w in range(1, 11):
    resultd2 = multiplication * w
    print(multiplication, "x", w, "=", resultd2)

elif multiplication == 3:
  for e in range(1, 11):
    resultd3 = multiplication * e
    print(multiplication, "x", e, "=", resultd3)

elif multiplication == 4:
  for r in range(1, 11):
    resultd4 = multiplication * r
    print(multiplication, "x", r, "=", resultd4)

elif multiplication == 5:
  for t in range(1, 11):
   resultd5 = multiplication * t
   print(multiplication, "x", t, "=", resultd5)

elif multiplication == 6:
  for y in range(1, 11):
    resultd6 = multiplication * y
    print(multiplication, "x", y, "=", resultd6)

elif multiplication == 7:
   for u in range(1, 11):
    resultd7 = multiplication * u
    print(multiplication, "x", u, "=", resultd7)

elif multiplication == 8:
  for i in range(1, 11):
    resultd8 = multiplication * i
    print(multiplication, "x", i, "=", resultd8)

elif multiplication == 9:
  for p in range(1, 11):
    resultd9 = multiplication * p
    print(multiplication, "x", p, "=", resultd9)

elif multiplication == 10:
  for d in range(1, 11):
    resultd10 = multiplication * d
    print(multiplication, "x", d, "=", resultd10)

else:
  print("ingrese un numero del 1 al 10")