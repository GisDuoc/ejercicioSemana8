def menu():
    print("Bienvenido")
    print("1. Calcular IVA")
    print("2. Descuento")
    print("3. Calcular IMC")
    print("4. Salir")

def calcularIVA(valor):
    return valor * 0.19

def calcularDesc(valor, descuento):
    resultado = valor - (valor * (descuento / 100))
    return resultado

def calcularImc(peso, estatura):
    resultado = peso / (estatura ** 2)
    if resultado < 18.5:
        print("Tienes un peso bajo")
    elif 18.5 <= resultado <= 24.9:
        print("Tienes un peso adecuado")
    elif 25.0 <= resultado <= 29.9:
        print("Tienes sobrepeso")
    elif 30.0 <= resultado <= 34.9:
        print("Tienes Obesidad grado 1")
    elif 35.0 <= resultado <= 39.9:
        print("Tienes Obesidad grado 2")
    elif resultado >= 40:
        print("Tienes Obesidad grado 3")

while True:
    menu()
    try:
        opcion = int(input("Por favor ingrese una opción: "))
        if opcion == 1:
            valor = float(input("Por favor ingrese un valor para calcular su IVA: "))
            print(f"Tu IVA es: {calcularIVA(valor)}")
        elif opcion == 2:
            valor = float(input("Por favor ingrese el valor original: "))
            descuento = float(input("Por favor ingrese el porcentaje de descuento: "))
            print(f"El precio con descuento es: {calcularDesc(valor, descuento)}")
        elif opcion == 3:
            peso = float(input("Por favor ingrese su peso en kg: "))
            estatura = float(input("Por favor ingrese su estatura en metros: "))
            calcularImc(peso, estatura)
        elif opcion == 4:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Por favor ingrese una opción válida.")
    except ValueError:
        print("Por favor ingrese un valor numérico válido.")





