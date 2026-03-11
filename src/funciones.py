def nota_maxima(notas):
    if len(notas) == 0:
        return None
    max_nota = max(notas)
    indice = notas.index(max_nota)
    return max_nota, indice
