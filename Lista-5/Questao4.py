"""Implemente uma versão modificada do algoritmo de Dijkstra que permita restringir alguns
nós (por exemplo, ruas em obras ou regiões perigosas). Tarefas:
 Implementar Dijkstra padrão.
 Criar lista de nós proibidos (você quem define, dinamicamente, quais são).
 Alterar o algoritmo para evitar tais nós."""

#Dijkstra é um algoritmo para achar a menor distância (caminho de custo mínimo) 
# de um nó origem para todos os outros nós em um grafo com pesos não-negativos nas arestas.

import heapq

class GrafoComRestricoes:
    def __init__(self, grafo):
        self.grafo = grafo
        self.restritos = set()   # nós proibidos

    def adicionar_restrito(self, no): #adicionar nó no conjunto de proibido
        self.restritos.add(no)

    def remover_restrito(self, no): #retirar nó do conjunto de proibido
        if no in self.restritos:
            self.restritos.remove(no)

    
    def dijkstra(self, inicio):
        dist = {n: float('inf') for n in self.grafo} #mantém a melhor distância conhecida de inicio a cada nó (inicialmente infinito
        dist[inicio] = 0

        fila = [(0, inicio)] #fila de prioridades (heap) onde sempre tiramos o nó com menor distância conhecida.

        while fila:
            distancia_atual, no_atual = heapq.heappop(fila) #tira o primeiro menor

            if distancia_atual > dist[no_atual]:#evita processar entradas antigas no heap.
                continue 

            for vizinho, peso in self.grafo[no_atual].items(): #melhorar a dist de um vizinho passando pelo nó atual
                nova_dist = distancia_atual + peso

                if nova_dist < dist[vizinho]: #Se nova_dist for melhor que o dist conhecido, atualiza
                    dist[vizinho] = nova_dist
                    heapq.heappush(fila, (nova_dist, vizinho))# coloca no heap para que esse vizinho seja processado mais tarde 
                    #(na ordem de menor distância)

        return dist

    def dijkstra_restrito(self, inicio):
        dist = {n: float('inf') for n in self.grafo}

        # Se o nó inicial for proibido, nem começamos
        if inicio in self.restritos:
            print("ERRO: Nó inicial está na lista de restritos!")
            return dist

        dist[inicio] = 0
        pq = [(0, inicio)] #fila de prioridade

        while pq:
            distancia_atual, no_atual = heapq.heappop(pq)

            if distancia_atual > dist[no_atual]:
                continue

            # Evitar processar nós proibidos
            if no_atual in self.restritos:
                continue

            for vizinho, peso in self.grafo[no_atual].items():

                # Evitar expandir para vizinhos proibidos
                if vizinho in self.restritos:
                    continue

                nova_dist = distancia_atual + peso

                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    heapq.heappush(pq, (nova_dist, vizinho))

        return dist



graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 3, 'D': 7, 'E': 5},
    'C': {'A': 2, 'B': 3, 'E': 6},
    'D': {'B': 7, 'E': 4, 'F': 2},   
    'E': {'B': 5, 'C': 6, 'D': 4, 'G': 3},
    'F': {'D': 2, 'G': 4},
    'G': {'E': 3, 'F': 4}
}

g = GrafoComRestricoes(graph)

print("---- Dijkstra normal ----")
print(g.dijkstra("A"))

# Adicionar nós proibidos
g.adicionar_restrito("E")
g.adicionar_restrito("C")

print("\n---- Nós proibidos ----")
print(g.restritos)

print("\n---- Dijkstra com restrições ----")
print(g.dijkstra_restrito("A"))
