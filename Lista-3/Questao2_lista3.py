"""Pesquise algum outro algoritmo de ordenação não mencionado em sala de aula.
Implemente-o explicando linha a linha o processo de sorting."""

#COMB SORT

""" o Comb Sort foi criado para ser um 'Bubble Sort' mais rápido e otimizado, onde ele vai comparar
    vizinhos, começando dos mais longes aos mais pertos, reduzindo os saltos por um fator encolhimento que foi
    escolhido convencionalmente como 1.3, assim elementos distantes são comparados e trocados e quando o 
    salto chega no valor 1, ele vira um Bubble Sort para garantir a ordenação, geralmente é mais rápido 
    e com complexidade no pior caso de O(N²)"""

def comb_sort(lista):
    tamanho = len(lista)          # tamanho da lista
    salto = tamanho               # "gap" é salto: distância entre elementos comparados
    houve_troca = True            # indica se houve troca na passada

    fator_encolhimento = 1.3      # valor padrão do Comb Sort

    # repete enquanto ainda houver trocas ou o salto for maior que 1
    while salto > 1 or houve_troca: #Quando chegar em 1 → continue rodando enquanto houver trocas
#Se o salto for menor que 1, ele vira um Bubble e vai comparar os elementos adjacentes 
        # diminui o salto
        salto = int(salto / fator_encolhimento)
        if salto < 1:
            salto = 1

        houve_troca = False       # assume que não terá trocas nesta rodada
        i = 0                     # começa do início da lista

        # percorre enquanto o par (i, i+salto) estiver dentro da lista
        while i + salto < tamanho: #i + salto é o índice do segundo elemento da comparação,
                                        #e i + salto < tamanho garante que esse índice existe
            # se estiver fora de ordem, troca
            if lista[i] > lista[i + salto]:
                lista[i], lista[i + salto] = lista[i + salto], lista[i]
                houve_troca = True

            i += 1                # avança para o próximo índice

    return lista

#testando
lista = [8, 11, 3, 0, 9, 2, 10,5,12]
print(f"Antes:{lista}")
comb_sort(lista)
print(f"Depois com o comb sort: {comb_sort(lista)}")
