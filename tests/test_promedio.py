from src.promedio import promedio

def test_promedio():
    notas = [4, 3, 5]
    assert promedio(notas) == 4