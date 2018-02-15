 #coding: utf-8
numero1 = int(input("Escriba un número entero: "))

while numero1 < 0:
    print("el numero introducido es divisible")
for i in range(1, numero1 + 1):
	if numero1 % i == 0:
		print "divisores del numero introducido:",i
