"""Desenvolva uma função que recebe duas listas encadeadas ordenadas e as combina em
uma única lista ordenada. Analise a complexidade da abordagem e sugira possíveis
oƟmizações para reduzir o tempo de execução."""

class Node:
    def __init__(self, nome, idade):
        self.nome = nome        
        self.idade = idade      
        self.next = None         

class Lista:
    def __init__(self):
        self.head = None         

    def inserir(self, nome, idade):
        new_node = Node(nome, idade)

        if self.head is None or idade < self.head.idade: #se a lista estiver vazia ou a idade for menor
            new_node.next = self.head    #
            self.head = new_node        
            return

        current=self.head
        #inserir no meio ou final
        while current.next and current.next.idade < idade:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def mostrar(self):
        
        if not self.head:
            print("Lista vazia")
            return
        current = self.head
        while current:
            print(f"{current.nome} - {current.idade}")
            current = current.next

def mesclar(lista1, lista2):

    ponteiro1, ponteiro2 = lista1.head, lista2.head
 #trata os casos de uma delas for vazia
    if not ponteiro1:
        nova_lista=Lista()
        nova_lista.head=ponteiro2
        return nova_lista
    if not ponteiro2:
        nova_lista=Lista()
        nova_lista.head=ponteiro1
        return nova_lista
 #vai ver qual o primeirio elemento para ser o head
    if ponteiro1.idade <= ponteiro2.idade:
        head = ponteiro1
        ponteiro1 = ponteiro1.next
    else:
        head = ponteiro2
        ponteiro2 = ponteiro2.next

    tail = head  #O tail começa sendo o mesmo nó que head, porque, até agora, só existe um nó na nova lista.

    while ponteiro1 and ponteiro2:
        if ponteiro1.idade <= ponteiro2.idade:
            tail.next = ponteiro1
            ponteiro1 = ponteiro1.next
        else:
            tail.next = ponteiro2
            ponteiro2 = ponteiro2.next
        tail = tail.next

    tail.next = ponteiro1 if ponteiro1 else ponteiro2

    nova_lista = Lista()
    nova_lista.head = head
    return nova_lista                 



if __name__ == "__main__":
    lista1 = Lista()
    lista1.inserir("Paola", 19)
    lista1.inserir("Lucas", 21)
    lista1.inserir("Heitor",19)

    lista2 = Lista()
    lista2.inserir("Ana", 18)
    lista2.inserir("Carlos", 25)

    print("Lista 1:")
    lista1.mostrar()
    print("\nLista 2:")
    lista2.mostrar()

    print("\nLista Mesclada:")
    lista_mesclada = mesclar(lista1, lista2)
    lista_mesclada.mostrar()
