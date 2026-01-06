"""Implemente em um único código uma comparação de tempo dos 5 algoritmos de
ordenação vistos em sala de aula juntamente com o algoritmo visto na questão
anterior para listas randômicas com 1.000, 10.000, 20.000, 30.000, 40.000, e 50.000
elementos. Crie uma discussão acerca dos resultados plotados. Aproveite o código
e faça uma comparação com uma única lista de 50.000 elementos, porém, force para
que os elementos sejam preenchidos em forma descendente. Plote o tempo e
discuta sobre o resultado alcançado fazendo uma comparação com o resultado da
questão anterior."""

import random
import time
import matplotlib.pyplot as plt

def bubbleSort(arr):
    tamanho = len(arr)
    for i in range(tamanho):
        troca = False
        for j in range(0, tamanho - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                troca = True
        if not troca:
            break

def selectionSort(arr):
    tamanho = len(arr)
    for i in range(tamanho-1): #o ultimo elemento ja estará no lugar certo
        min_index = i
        for j in range(i+1, tamanho):
            if arr[j] < arr[min_index]:
                min_index = j #objetivo é buscar o menor elemento entre os índices seguintes ao índice atual i
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertionSort(arr):
    tamanho = len(arr)
    for i in range(1, tamanho):
        current_value = arr[i]#armazena valor do atual para inserir na posição certa
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j+1] = arr[j]#move o elemento maior para a direita
            j -= 1 #vai voltando pela lista até encontrar um valor menor ou igual ao current
        arr[j+1] = current_value#posição j+1 é onde o current deve ser inserido

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) // 2
    esquerda = mergeSort(arr[:meio]) #chama recursivamente para ordenar as partes
    direita = mergeSort(arr[meio:])

    return merge(esquerda, direita)

def merge(esq, dir): #função que vai mesclar as duas listas do mergesort
    merged = []
    i, j = 0, 0 #dois indices para acompanhar a posição atual em cada lista i indice esq, j indice dir
    while i < len(esq) and j < len(dir): #enquanto houver elementos nas duas listas
        if esq[i] < dir[j]: # se o elemento da esquerda for menor que o da direita 
            merged.append(esq[i]) #coloca o elemento na lista final e avança uma casa na lista da esquerda
            i += 1
        else:
            merged.append(dir[j])
            j += 1
    merged.extend(esq[i:]) #adiciona todos os elementos que sobraram  da esquerda
    merged.extend(dir[j:]) #e da direita
    return merged #retorna a lista junta e ordenada

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr)//2] #pivo sendo o elemento do meio da lista 
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    return quickSort(esquerda) + meio + quickSort(direita)

def combsort(lista):
    tamanho = len(lista)
    salto = tamanho
    houve_troca = True
    fator = 1.3

    while salto > 1 or houve_troca:
        salto = int(salto / fator)
        if salto < 1:
            salto = 1
        houve_troca = False

        i = 0
        while i + salto < tamanho:
            if lista[i] > lista[i + salto]:
                lista[i], lista[i + salto] = lista[i + salto], lista[i]
                houve_troca = True
            i += 1
    return lista

# FUNÇÃO DE MEDIR TEMPO        

def medir_tempo(algoritmo, lista): #vai receber o algoritmo de ordenação e a lista para ordenar
    copia = lista.copy() #Cria uma cópia da lista para garantir que cada algoritmo receba a mesma 
    #lista original, evitando que um algoritmo use a lista já ordenada por outro.
    inicio = time.time()

    algoritmo(copia)

    return time.time() - inicio #retorna o tempo gasto

if __name__ == "__main__":

    # Algoritmos mais lentos
    alg_quadraticos = {
        "Bubble": bubbleSort,
        "Selection": selectionSort,
        "Insertion": insertionSort
    }

    # Algoritmos eficientes
    alg_eficientes = {
        "Merge": mergeSort,
        "Quick": quickSort,
        "Comb": combsort
    }
    print("Teste com tamanho menores:\n")

    tamanhos_pequenos = [1000, 2000, 3000, 4000, 5000]
    resultados_peq = {alg: [] for alg in alg_quadraticos} #dois dicionários que armazenarão os tempos de execução para cada algoritmo.
    resultados_peq2={alg:[] for alg in alg_eficientes}

    for t in tamanhos_pequenos: #para cada tamanho  
        lista = [random.randint(0, 1000000) for _ in range(t)] #cria uma lista com t números aleatórios entre 0 e 1 milhão.
        print(f"\nTamanho: {t}")

        for nome, alg in alg_quadraticos.items(): #para cada algoritmo mais lento
            tempo = medir_tempo(alg, lista) #Mede quanto tempo o algoritmo demorou.
            resultados_peq[nome].append(tempo) #e armazena o tempo no dicionario
            print(f"  {nome}: {tempo:.5f}s")
        
        for nome, alg in alg_eficientes.items(): 
            tempo= medir_tempo(alg,lista)
            resultados_peq2[nome].append(tempo)
            print(f"  {nome}: {tempo:.5f}s")
    

    print("TESTES GRANDES APENAS PARA ALGORITMOS RÁPIDOS \n")

    tamanhos_grandes = [10000, 20000, 30000, 40000, 50000] #lista com os tamanhos maiores
    resultados_grd = {alg: [] for alg in alg_eficientes} #dicionario com a chave do nome para cada algoritmo
                                                        #e o valor começa com a lista vazia
    for t in tamanhos_grandes:
        lista = [random.randint(0, 1000000) for _ in range(t)]#faz uma lista com numeros aleatorios com random
        print(f"\nTamanho: {t}")

        for nome, alg in alg_eficientes.items(): 
            tempo = medir_tempo(alg, lista)
            resultados_grd[nome].append(tempo)
            print(f"  {nome}: {tempo:.5f}s")

print("\n teste para LISTA DECRESCENTE 50.000 \n")

lista_dec = list(range(50000, 0, -1)) #range indo de 50.000 decrescendo para 0
tempos_dec = {} #dicionario para guardar resultados

# Apenas os algoritmos eficientes
for nome, alg in alg_eficientes.items():
    print(f"Testando {nome}...")
    tempo = medir_tempo(alg, lista_dec)
    tempos_dec[nome] = tempo
    print(f"  {nome}: {tempo:.5f}s\n")

# Gráfico da lista decrescente
plt.figure(figsize=(12, 6)) #tamanho da imagem
plt.bar(tempos_dec.keys(), tempos_dec.values(), color="darkorange") #grafico de barras com nome e tempo
plt.ylabel("Tempo (s)")
plt.title("Tempo de execução - Lista Decrescente (50.000 elementos)")
plt.grid(axis="y")
plt.show()

"""A partir da análise do gráfico e dos tempos dos métodos, percebe-se que os algoritmos como o Bubble, Selection 
e InsertionSort não são apropriados para um volume de dados tão grandes, pois demoraria muito tempo para fazer com 50.000
dados, Para o tamanho de 1000, o Insertion conseguiu ser o mais rápido, e o Bubble, ficou por último, visto sua estrutura 
mais lenta; Para o tamanho de 3000 e 4000 o Bubble obteve mais tempo e o Selection e o Insertion ficaram com diferença de 1 
segundo, assim como no de 5.000, que teve pouca diferença de segundo entre eles, já para os eficientes, os tempos foram bem
menores do que os outros sendo o Quick Sort o que mais rápido em 1000 e 2000, em 3000 o comb se destacou e em 4000 e 5000 o Quick voltou.
 Já para os testes maiores, O Quick se mantém como mais rápido, e na lista decrescente também, visto no meu código eu coloquei para o 
 pivô ser na metade do tamanho, mas caso fosse escolhido aleatoriamente, o quick seria o mais lento, que seguido do Merge, 
 e o comb se torna o mais lento com 19s"""