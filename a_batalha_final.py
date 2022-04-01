rodadas = int(input())
nums_pedro = []
nums_tulio = []
tot_vit_pedro = 0
tot_vit_tulio = 0

if rodadas > 0:
    for r in range(rodadas):
        cont = 0
        tam_l_pedro, tam_l_tulio = map(int, input().split())
        pedro = list(map(int, input().split()))
        tulio = list(map(int, input().split()))

        # Defindo as escolhas de Pedro

        num_pedro = 0
        maior_quant_rep = 0
        for n in pedro:
            quant_rep = pedro.count(n)
            if cont == 0:
                maior_quant_rep = quant_rep
                num_pedro = n
            else:
                if quant_rep > maior_quant_rep:
                    maior_quant_rep = quant_rep
                    num_pedro = n
                elif quant_rep == maior_quant_rep:
                    num_repetidos_pedro = []
                    num_repetidos_pedro.append(n)
                    num_repetidos_pedro.append(num_pedro)
                    num_pedro = max(num_repetidos_pedro)
            cont += 1
        nums_pedro.append(num_pedro)

        # Definindo as escolhas de Tulio

        num_tulio = 0
        maior_quant_rep = 0
        for n in tulio:
            quant_rep = tulio.count(n)
            if cont == 0:
                maior_quant_rep = quant_rep
                num_tulio = n
            else:
                if quant_rep > maior_quant_rep:
                    maior_quant_rep = quant_rep
                    num_tulio = n
                elif quant_rep == maior_quant_rep:
                    num_repetidos_tulio = []
                    num_repetidos_tulio.append(n)
                    num_repetidos_tulio.append(num_tulio)
                    num_tulio = max(num_repetidos_tulio)
            cont += 1
        nums_tulio.append(num_tulio)

    # Definindo a quantidade de vitorias

    for c in range(rodadas):
        print(f"pedro: {nums_pedro[c]} tulio: {nums_tulio[c]}")
        if nums_pedro[c] > nums_tulio[c]:
            tot_vit_pedro += 1
        elif nums_tulio[c] > nums_pedro[c]:
            tot_vit_tulio += 1
        else:
            tot_vit_tulio += 1
            tot_vit_pedro += 1

    # Definindo a situacao final

    if tot_vit_pedro > tot_vit_tulio:
        print(f"Pedro foi vitorioso com {tot_vit_pedro} pontos")
    elif tot_vit_tulio > tot_vit_pedro:
        print(f"Tulio foi vitorioso com {tot_vit_tulio} pontos")
    else:
        print(f"Tulio e Pedro empataram com {tot_vit_tulio} pontos")
else:
    print(0)