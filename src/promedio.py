def promedio(n):
    if not n:
        return 0
    return sum(n) / len(n)



notas = [4, 3, 5]
print(promedio(notas))