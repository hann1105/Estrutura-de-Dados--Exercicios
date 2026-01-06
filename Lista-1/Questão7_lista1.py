"""Implemente uma fila circular para gerenciar requisições de impressão. Cada requisição
tem um número e um tamanho de arquivo. A cada atendimento, a fila avança
circularmente, liberando a impressora para a próxima tarefa."""

class Node:
    def __init__(self,numero_req,tamanho):
        self.numero_req=numero_req
        self.tamanho=tamanho
        self.next=None

class Impressora:
    def __init__(self):
        self.front=None # Primeiro da fila
        self._size=0
    
    def enqueue(self,numero_req,tamanho): #inserir
        new_node=Node(numero_req,tamanho)
        if self.front is None: #se o front for vazio, o novo nó e o seu next será o front (circular)
            self.front=new_node
            new_node.next=self.front
        else: # caso não
            current=self.front #o current começa do front(primeiro nó)
            while current.next != self.front: #enquanto o current.next não for o front que será o seu último por ser circular
                current=current.next
            current.next=new_node #vai inserir o new node antes do front
            new_node.next=self.front #e o next do novo nó será o front para ter a circularidade
        self._size+=1 #aumenta o tamanho da fila
        print(f"Requisição n° {numero_req} adicionada! Tamanho:{tamanho}MB")

    def dequeue(self): 
        if self.is_empty():
            return ("Fila vazia")
        remover_requisicao=self.front #guarda a requisição que será removida no front
        if self.front.next ==self.front: #só tem um nó então o front fica none
            self.front=None
        else:
            current=self.front #começa do front
            while current.next !=self.front:
                current=current.next
            current.next=self.front.next #o proximo será o antigo next do front 
            self.front=self.front.next #atualiza o novo front
        self._size-=1
        print(f"Processando Requisição n°{remover_requisicao.numero_req} ")
        return remover_requisicao.numero_req
    
    def is_empty(self):
        return self._size==0
    
    def size(self):
        return self._size
    
    def mostrar_fila(self):
        if self.is_empty():
            print("Fila Vazia")
            return
        print("----- FILA ------")
        current=self.front
        for requerimentos in range(self._size):
            print(f"Requerimento n° {current.numero_req} -> {current.tamanho} MB")
            current=current.next
        
if __name__ == "__main__":
    fila = Impressora()
    fila.enqueue(1, 10)
    fila.enqueue(2, 5)
    fila.enqueue(3, 8)
    fila.mostrar_fila()

    fila.dequeue()
    fila.mostrar_fila()

    fila.enqueue(4, 12)
    fila.mostrar_fila()

        