print("bienvenido")
print("conversion de grados fahrenheit a celcius")

while True:
   fahrenheit = float(input("ingrese una temperatura para converir a celsius: "))

   if fahrenheit == 999:
     print("el programa ha finalizado.")
     break

   celsius = 5/9 * (fahrenheit - 32)

   print("la temperatura en grados celcius es de:", celsius)