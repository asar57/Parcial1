from src.Notas_perdidas import notas_perdidas

def test_arreglo_vacio():
    assert notas_perdidas([]) == 0

def test_notas_perdidas_varias():
    # 2 notas perdidas (2.5 y 1.0)
    assert notas_perdidas([6, 4.0, 1.0, 3.5]) == 2

def test_todas_aprobadas():
    # ninguna nota menor a 3.0
    assert notas_perdidas([3.0, 4.5, 5.0]) == 0
