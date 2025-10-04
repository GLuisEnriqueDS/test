# calculadora.py - CON NUEVAS MEJORAS
def suma(a, b):
    resultado = a + b
    print(f"Suma: {a} + {b} = {resultado}")
    return resultado

def resta(a, b):
    resultado = a - b
    print(f"Resta: {a} - {b} = {resultado}")
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    print(f"Multiplicación: {a} x {b} = {resultado}")
    return resultado

def division(a, b):
    if b == 0:
        print("Error: No se puede dividir por cero")
        return "Error: No se puede dividir por cero"
    resultado = a / b
    print(f"División: {a} ÷ {b} = {resultado}")
    return resultado

# ✅ NUEVA FUNCIÓN: POTENCIA
def potencia(a, b):
    resultado = a ** b
    print(f"Potencia: {a} ^ {b} = {resultado}")
    return resultado

# ✅ NUEVA FUNCIÓN: RAÍZ CUADRADA
def raiz_cuadrada(a):
    if a < 0:
        print("Error: No se puede calcular raíz de número negativo")
        return "Error: Número negativo"
    resultado = a ** 0.5
    print(f"Raíz cuadrada: √{a} = {resultado}")
    return resultado

# ✅ FUNCIÓN QUE USA LAS OTRAS FUNCIONES
def calculadora_completa():
    print("\n=== CALCULADORA COMPLETA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    
    opcion = input("Elige una opción (1-6): ")
    
    if opcion in ['1', '2', '3', '4', '5']:
        num1 = float(input("Primer número: "))
        num2 = float(input("Segundo número: "))
        
        if opcion == '1':
            return suma(num1, num2)
        elif opcion == '2':
            return resta(num1, num2)
        elif opcion == '3':
            return multiplicacion(num1, num2)
        elif opcion == '4':
            return division(num1, num2)
        elif opcion == '5':
            return potencia(num1, num2)
    
    elif opcion == '6':
        num1 = float(input("Número: "))
        return raiz_cuadrada(num1)
    
    else:
        print("Opción no válida")
        return None