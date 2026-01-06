"""Implemente um Deque para simular o histórico de navegação de um navegador. Cada
página acessada deve ser inserida no fim do deque. O botão “voltar” remove uma página
do fim e a coloca em uma pilha auxiliar de “avançar”. O botão “avançar” remove uma
página da pilha auxiliar e a reinsere no fim do deque. Tarefas:"""

class Node:
    def __init__(self, pagina):
        self.pagina = pagina
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.front = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def inserirInicio(self, pagina):
        new_node = Node(pagina)
        if self.is_empty():
            self.front = new_node
        else:
            new_node.next = self.front #o next do novo nó será o front
            self.front.prev = new_node #assim o prev do front é o novo nó
            self.front = new_node #atualiza o front com o novo nó
        self._size += 1

    def inserirFim(self, pagina):
        new_node = Node(pagina)
        if self.is_empty():
            self.front = new_node
        else:
            current = self.front
            while current.next: 
                current = current.next
            current.next = new_node #vai inserir o novo nó no próximo
            new_node.prev = current #assim o prev vai ser o current (antigo)
        self._size += 1

    def removerInicio(self):
        if self.is_empty():
            return None
        pagina = self.front.pagina #guarda o item a ser removido no front
        self.front = self.front.next #vai pular o front e assim o next vai ser o novo front 
        if self.front: # se tiver só um nó, fica none
            self.front.prev = None
        self._size -= 1 #diminui o tamanho
        return pagina

    def removerFim(self):
        if self.is_empty():
            return None
        current = self.front #começa do primeiro nó para percorrer a lista toda
        while current.next:  
            current = current.next
        pagina = current.pagina #guarda o valor
        if current.prev: #se existe um nó anterior, o penúltimo nó agora passa a ser o último e asim não tem prev do next
            current.prev.next = None
        else: #se não tem um anterior, então só tinha um nó, logo o front é none
            self.front = None
        self._size -= 1
        return pagina

    def mostrar(self):
        current = self.front
        paginas = []
        while current:
            paginas.append(current.pagina)
            current = current.next
        return paginas


class Pilha: #pilha auxiliar
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        return self.itens.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.itens) == 0


class Navegador:
    def __init__(self):
        self.historico = Deque()
        self.pilha_avancar = Pilha()

    def acessar_pagina(self, pagina): #cada pagina deve ser inserida no fim do deque
        print(f"Acessando: {pagina}")
        self.historico.inserirFim(pagina)
        self.pilha_avancar = Pilha()

    def voltar(self): #botão voltar remove uma página do fim e insere na pilha de avançar
        if self.historico.size() > 1:
            pagina = self.historico.removerFim()
            self.pilha_avancar.push(pagina)
            print(f"Voltando de: {pagina}")
        else:
            print("Não há páginas para voltar.")

    def avancar_pagina(self): #O botão “avançar” remove uma página da pilha auxiliar e a reinsere no fim do deque
        pagina = self.pilha_avancar.pop()
        if pagina:
            self.historico.inserirFim(pagina)
            print(f"Avançando para: {pagina}")
        else:
            print("Não há páginas para avançar.")

    def mostrar_historico(self):
        print("Histórico atual:", " - ".join(self.historico.mostrar()))


# Teste
if __name__ == "__main__":
    navegador = Navegador()
    navegador.acessar_pagina("google.com")
    navegador.acessar_pagina("youtube.com")
    navegador.acessar_pagina("github.com")
    navegador.mostrar_historico()

    navegador.voltar()
    navegador.mostrar_historico()

    navegador.voltar()
    navegador.mostrar_historico()

    navegador.avancar_pagina()
    navegador.mostrar_historico()
