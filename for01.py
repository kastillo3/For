 #coding: utf-8
numero1 = int(input("Escriba un número entero: "))
numero2 = int(input("Escriba un número entero mayor o igual que numero1:"))

if numero2 < numero1:
    print("no es mayor")
else:
    for i in range(numero1, numero2 + 1):
        if i % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")

