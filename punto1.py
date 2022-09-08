n = int(input("Ingrese la cantidad de números que desea ingresar: "))
multiplos2=0
multiplos3=0

for i in range(n):
    num=int(input("Ingrese un número entero: "))
    if num%2==0:
        multiplos2=multiplos2+1
    if num%3==0:
        multiplos3=multiplos3+1

print(f"Se ingresaron {multiplos2} múltiplos de 2 y {multiplos3} mpultiplos de 3")