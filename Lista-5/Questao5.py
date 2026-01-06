""" O coeficiente de agrupamento mede o quanto
os vizinhos de um nó em um grafo estão conectados entre si. Ele indica o "nível de
comunidade local".
 valor próximo de 0 → os vizinhos quase não se conectam;
 valor próximo de 1 → os vizinhos formam um grupo bem conectado (quase um
“clube fechado”)
Dado um grafo não dirigido representado como lista de adjacência (defina seu próprio grafo
com, pelo menos, 10 nós), implemente uma função que calcule o coeficiente de
agrupamento de cada nó. Sua função deve:
1. Para cada nó v, idenƟficar seus vizinhos.
2. Contar quantas conexões existem entre esses vizinhos.
3. Calcular o valor usando a fórmula (onde k é o número de vizinhos de v):

4. Retornar um dicionário com os coeficientes"""

def coeficiente_agrupamento(grafo):
    coeficientes = {} #dicionário para colcoar os coeficientes por nó

    for v in grafo: #Para cada nó v, pega a lista de vizinhos (vizinhos) e conta quantos são (k).
        vizinhos = grafo[v]
        k = len(vizinhos) #quantidade de vizinhos

        # Se houver menos de 2 vizinhos, o denominador fica zero ,coeficiente = 0
        if k < 2:
            coeficientes[v] = 0.0
            continue

        # Conta conexões existentes entre vizinhos de v
        conexoes_existentes = 0 #contador que é o numerador

        # Percorre todos os pares de vizinhos
        for i in range(k): #Percorre todos os pares distintos de vizinhos (n1, n2) (somente uma vez por par)
            for j in range(i + 1, k):
                n1 = vizinhos[i]
                n2 = vizinhos[j]

                # Se n1 está conectado com n2, ent entra na lista de conexões
                if n2 in grafo[n1]:
                    conexoes_existentes += 1

        # Calcula o denominador da fórmula: k(k-1)/2
        conexoes_possiveis = (k * (k - 1)) / 2

        # Aplica a fórmula
        C_v = conexoes_existentes / conexoes_possiveis

        coeficientes[v] = round(C_v, 2) #Arredonda para 2 casas e guarda no dicionário.

    return coeficientes


grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['A', 'E'],
    'E': ['D', 'F', 'G'],
    'F': ['E', 'G'],
    'G': ['E', 'F', 'H'],
    'H': ['G', 'I', 'J'],
    'I': ['H'],
    'J': ['H']
}

resultado = coeficiente_agrupamento(grafo)
print(resultado)
