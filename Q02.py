Q = [0] * 20

for i in range(20):
    while True:
        valor = float(input(f"Digite o valor para a posição {i + 1}: "))
        if valor >= 0:
            Q[i] = valor
            break
        else:
            print("Por favor, digite um número positivo.")

maior_elemento = max(Q)
posicao_maior_elemento = Q.index(maior_elemento) + 1

menor_elemento = min(Q)
posicao_menor_elemento = Q.index(menor_elemento) + 1

print(f"O maior elemento de Q é {maior_elemento} e ocupa a posição {posicao_maior_elemento}.")
print(f"O menor elemento de Q é {menor_elemento} e ocupa a posição {posicao_menor_elemento}.")
