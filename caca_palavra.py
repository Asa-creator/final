tabela_ascci = {"65": "A", "78": "N",
                "66": "B", "79": "O",
                "67": "C", "80": "P",
                "68": "D", "81": "Q",
                "69": "E", "82": "R",
                "70": "F", "83": "S",
                "71": "G", "84": "T",
                "72": "H", "85": "U",
                "73": "I", "86": "V",
                "74": "J", "87": "W",
                "75": "K", "88": "X",
                "76": "L", "89": "Y",
                "77": "M", "90": "Z"}


relacao_letra_linha = {"0": "A", "13": "N",
                       "1": "B", "14": "O",
                       "2": "C", "15": "P",
                       "3": "D", "16": "Q",
                       "4": "E", "17": "R",
                       "5": "F", "18": "S",
                       "6": "G", "19": "T",
                       "7": "H", "20": "U",
                       "8": "I", "21": "V",
                       "9": "J", "22": "W",
                       "10": "K", "23": "X",
                       "11": "L", "24": "Y",
                       "12": "M", "25": "Z"}

tot_p_achadas = 0

# Entradas
tam_palavra = int(input())
palavra = str(input())
linhas, colunas = map(int, input().split())


matriz = []

for l in range(linhas):
    c = list(map(int, input().split()))
    matriz.append(c)


cont = 0
palavra_horizontal = []
for l in range(linhas):
    for c in range(colunas):
        letra = tabela_ascci[str(matriz[l][c])]
        palavra_horizontal.append(letra)
        if cont < linhas-1:
            cont += 1
        else:
            pl = ""
            for let in palavra_horizontal:
                pl += let
            if palavra in pl:
                tot_p_achadas += 1
                primeira_letra_da_palavra_buscada = palavra[0]
                posicao_da_primeira_letra = pl.rfind(primeira_letra_da_palavra_buscada)+1
                linha_achada = relacao_letra_linha[str(l)]
                ultima_coluna_achada = c
                print(f"{linha_achada}{posicao_da_primeira_letra}")
                print(f"{linha_achada}{ultima_coluna_achada}")
            palavra_horizontal.clear()
            cont = 0
    print()

palavra_vertical = []
for c in range(colunas):
    for l in range(linhas):
        letra = tabela_ascci[str(matriz[l][c])]
        palavra_vertical.append(letra)
        if cont < colunas:
            cont += 1
        else:
            pl = ""
            for let in palavra_vertical:
                pl += let
            if palavra in pl:
                tot_p_achadas += 1
                primeira_letra_da_palavra_buscada = palavra[0]
                ultima_letra_da_palavra_buscada = palavra[len(palavra)-1]
                numero_da_coluna_onde_a_palavra_comeca = c+1
                numero_da_coluna_onde_a_palavra_termina = pl.find(ultima_letra_da_palavra_buscada)
                achou = pl.find(primeira_letra_da_palavra_buscada)
                linha_comeca = relacao_letra_linha[str(achou)]
                achou2 = pl.find(ultima_letra_da_palavra_buscada)
                linha_termina = relacao_letra_linha[str(achou2)]
                print(f"{linha_comeca}{numero_da_coluna_onde_a_palavra_comeca}")
                print(f"{linha_termina}{numero_da_coluna_onde_a_palavra_termina}")
            palavra_vertical.clear()
            cont = 0
        print()

if tot_p_achadas == 0:
    print(0)
