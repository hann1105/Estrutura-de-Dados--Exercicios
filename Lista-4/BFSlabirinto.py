# ============================================
# LABIRINTO + BFS + GRÁFICO PROFISSIONAL
# ============================================

from collections import deque     # usado para fila eficiente do BFS
import matplotlib.pyplot as plt     # usado para plotar o gráfico
import numpy as np                  # usado para manipular matriz como array

# ---------------------------------------------------------
# MATRIZ DO LABIRINTO
# 0 = célula livre
# 1 = parede
# ---------------------------------------------------------
lab = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0],
    [0,0,0,1,0]
]

# coordenadas de início e fim
inicio = (0, 0)
fim    = (4, 4)

# movimentos possíveis: baixo, direita, cima e esquerda
direcoes = [(1,0),(0,1),(-1,0),(0,-1)]


# =========================================================
# FUNÇÃO BFS PARA ENCONTRAR O MENOR CAMINHO NO LABIRINTO
# =========================================================
def bfs_labirinto(mapa, start, goal):
    linhas, colunas = len(mapa), len(mapa[0])

    # fila da BFS começa com a posição inicial
    fila = deque([start])

    # dicionário que armazena de onde cada posição veio
    # essencial para depois reconstruir o caminho
    veio_de = {start: None}

    # ------------------ INÍCIO DO BFS ---------------------
    while fila:
        r, c = fila.popleft()   # retira o primeiro da fila

        # se chegamos ao final, interrompe a busca
        if (r, c) == goal:
            break

        # testa vizinhos (quatro direções)
        for dr, dc in direcoes:
            nr, nc = r + dr, c + dc

            # verifica limites do labirinto
            if 0 <= nr < linhas and 0 <= nc < colunas:
                
                # só podemos andar em células livres (0)
                # e que ainda não foram visitadas
                if mapa[nr][nc] == 0 and (nr, nc) not in veio_de:
                    veio_de[(nr, nc)] = (r, c)   # registra o predecessor
                    fila.append((nr, nc))        # adiciona na fila (expansão BFS)

    # ------------------ RECONSTRUÇÃO DO CAMINHO ---------------------

    caminho = []
    atual = goal

    # volta do objetivo até o início usando o dicionário "veio_de"
    while atual:
        caminho.append(atual)
        atual = veio_de[atual]

    caminho.reverse()  # inverte para ficar do início → fim
    return caminho


# EXECUÇÃO
caminho = bfs_labirinto(lab, inicio, fim)
print("Menor caminho:", caminho)
print("Passos:", len(caminho))


# =========================================================
#               GRÁFICO PROFISSIONAL DO LABIRINTO
# =========================================================

fig, ax = plt.subplots(figsize=(7, 7))

# converte lista para array para facilitar na plotagem
mat = np.array(lab)

# mostra paredes em preto e áreas livres em branco
ax.imshow(mat == 1, cmap="gray", vmin=0, vmax=1)

# desenha uma grade (grid) para visualizar as células
ax.set_xticks(np.arange(-0.5, 5, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 5, 1), minor=True)
ax.grid(which="minor", color="lightgray", linewidth=1)

# ------------------- MARCA O CAMINHO BFS -------------------

# cada célula do caminho vira um círculo azul
for r, c in caminho:
    ax.add_patch(plt.Circle((c, r), 0.30, color="deepskyblue"))

# marca início em verde
ir, ic = inicio
ax.add_patch(plt.Circle((ic, ir), 0.35, color="lime", label="Início"))

# marca fim em vermelho
fr, fc = fim
ax.add_patch(plt.Circle((fc, fr), 0.35, color="red", label="Fim"))

# cria símbolo para legenda (não aparece no gráfico, só na legenda)
ax.scatter([], [], c="deepskyblue", s=150, label="Caminho BFS")

# título do gráfico
ax.set_title("Labirinto - Menor Caminho Encontrado pelo BFS", fontsize=14)

# inverte eixo Y para o labirinto aparecer na orientação tradicional
ax.invert_yaxis()

# remove números dos eixos para deixar visual mais limpo
ax.set_xticks([])
ax.set_yticks([])

# mostra legenda no canto superior esquerdo
ax.legend(loc="upper left")

plt.show()
