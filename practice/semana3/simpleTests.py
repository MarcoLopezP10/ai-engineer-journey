#Escribir 5 tests simples para funciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def es_par(numero):
    return numero % 2 == 0

def calcular_cuadrado(numero):
    return numero ** 2

# Test 1: Comprobar la suma de dos números positivos
def test_sumar_positivos():
    assert sumar(3, 5) == 8

# Test 2: Comprobar la resta con resultados negativos
def test_restar_da_negativo():
    assert restar(10, 15) == -5

# Test 3: Comprobar la multiplicación por cero
def test_multiplicar_por_cero():
    assert multiplicar(7, 0) == 0

# Test 4: Comprobar si un número es par (debe devolver True)
def test_es_par_verdadero():
    assert es_par(4) is True

# Test 5: Comprobar el cálculo del cuadrado de un número
def test_cuadrado_positivo():
    assert calcular_cuadrado(6) == 36

