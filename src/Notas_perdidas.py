def notas_perdidas(notas):

    if not notas:
        return 0

    perdidas = 0

    for nota in notas:
        # Solo contar notas válidas entre 0 y 5
        if isinstance(nota, (int, float)) and 0 <= nota <= 5:
            if nota < 3.0:
                perdidas += 1
        else:
            print(f"Valor inválido ignorado: {nota}")
    return perdidas