# calculadora.py - VERSIÓN MEJORADA
def suma(a, b):
    resultado = a + b
    print(f"Suma: {a} + {b} = {resultado}")
    return resultado

def resta(a, b):
    resultado = a - b
    print(f"Resta: {a} - {b} = {resultado}")
    return resultado

# ✅ AGREGAR NUEVA FUNCIÓN
def multiplicacion(a, b):
    return a * b

# ✅ AGREGAR OTRA FUNCIÓN
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b