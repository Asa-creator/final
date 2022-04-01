def max_felicidade(comidas, max_kg):
    soma_felicidades = 0
    kg_perdidos = 0
    lista_comidas = []

    for c in range(comidas):
        felicidade, quant_kg = map(int, input().split())
        comida = []
        if quant_kg < 0:
            kg_perdidos += quant_kg
            soma_felicidades += felicidade
        if quant_kg > 0:
            comida.append(felicidade)
            comida.append(quant_kg)
            lista_comidas.append(comida.copy())
            comida.clear()

    quant_kg_p_ganhar = kg_perdidos - max_kg

    for c in lista_comidas:
        if c[1] + quant_kg_p_ganhar <= 0:
            soma_felicidades += c[0]
            quant_kg_p_ganhar += c[1]

    if soma_felicidades > 0:
        return soma_felicidades
    else:
        return 0


comidas, max_kg = map(int, input().split())

sit = max_felicidade(comidas, max_kg)
print(sit)
