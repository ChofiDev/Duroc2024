def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    return a / b
def suma_2():
    try:
        cant = int(input("Ingresa la cantidad de numeros a sumar"))
    except:
        print("Ingresa solo números enteros")
    total = 0
    for i in range(cant):
        total += int(input(f"Ingresa el número {i+1}"))
    return total