from src.funciones import nota_maxima

def test_arreglo_vacio():
    assert nota_maxima([]) == None

def test_notas_normales():
    assert nota_maxima([3,4,2,5]) == 5

def test_notas_decimales():
    assert nota_maxima([6.0,4.8,3.1]) == 6.0
