def notas_perdidas(notas):

    if not notas:
        return 0

    perdidas = 0
    for nota in notas:
        if nota < 3.0:
            perdidas += 1
    return perdidas