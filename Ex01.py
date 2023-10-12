#Te muestra los números del 1 al 100 y cuales son pares e impares
#Shows first hundred numbers y tell wich one is even and odd
for i in range(1, 101):
    if i % 2 == 0:
        print(str(i) + " es par")
    else:
        print(str(i) + " es impar")
