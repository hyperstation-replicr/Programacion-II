def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Análisis de números")

numeros = []
for i in range(5):
    try:
        num = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        break

print("\nAnalisis")

for n in numeros:
    if n == 0:
        print(f"{n} es cero")
        print(f"{n} es par")
        print(f"El factorial de {n} es: {factorial(n)}")
        print("-" * 30)
        continue

    if n > 0:
        print(f"{n} es positivo")
    else:
        print(f"{n} es negativo")
    
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

    try:
        print(f"El factorial de {n} es: {factorial(n)}")
    except Exception as e:
        print("Error al calcular el factorial:", e)
    
    print("-" * 30)
