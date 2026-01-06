"""Implemente uma estrutura de Dados tipo Deque usando Listas Encadeadas. É
importante que o TAD possua as 4 operações para remover e inserir dados de ambas
as extremidades. Comente sobre o tipo de Lista Encadeada escolhida para
implementação."""

class Node:
    def __init__(self,dado):
        self.dado=dado
        self.next=None #ponteiro para o próximo nó
        self.prev=None #ponteiro para o nó anterior

class Deque:
    def __init__(self):
        self.head=None #ponteiro para o primeiro nó
        self.tail=None #ponteiro para o último nó
    
    def inserir_front(self,dado): #inserir no início
        new_node=Node(dado)
        if self.head is None:
            self.head=self.tail=new_node # new node é inicio e fim
        else:
            new_node.next=self.head #aponta o novo nó para o antigo head
            self.head.prev=new_node # o antigo head aponta denovo para o novo nó, assim fecha a conexão dupla
            self.head=new_node #logo o head vira o novo nó, ou seja, o novo nó vira o inicio da lista

    def inserir_final(self,dado): #inserir no final
        new_node=Node(dado)
        if self.tail is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node #o proimo ultimo aponta para o novo nó
            new_node.prev=self.tail #o prev do novo nó é o tail, logo o tail vira o novo nó
            self.tail=new_node
    
    def remover_front(self): # remover no inicio
        if self.head is None:
            return None
        
        dado=self.head.dado #guarda o valor do primeiro elemento 
        self.head=self.head.next #move head para o próximo nó
        if self.head is None:
            self.tail=None
        else:
            self.head.prev=None #o novo primeiro não tem prev
        return dado
    
    def remover_final(self): # remover no final
        if self.tail is None:
            return None
        
        dado=self.tail.dado #guarda o valor
        self.tail=self.tail.prev #move o tail para o seu anterior, já que irá remover o último
        if self.tail is None:
            self.head=None
        else:
            self.tail.next=None #o tail do últimoo aponta para node
        return dado
    
    def exibir_elementos(self):
        if self.head==None:
            print("Fila vazia")
            return
        current=self.head
        elementos=[]
        while current is not None:
            elementos.append(current.dado)
            current = current.next
        print(f"Fila: {elementos}")

    
    #Eu escolhi a lista duplamente encadeada pois com ela eu tenho um maior controle sobre o início e final do deque,
    #já que a lista duplamente encadeada já vem com uma estrutura de next,prev,head e tail que ajudam na implementação
    # de inserir e remover por ambos os lados. Com uma lista encadeada sem ser duplamente, ficaria mais complexo para
    #remover e inserir no fim, pois para remover do fim eu teria que percorrer a lista inteira para conseguir remover
    #o elemento do final e assim seria mais lento do que fazendo por uma lista duplamente encadeada que contém estrutura "semelhante".

    #Teste
"""deque=Deque()
deque.inserir_front(1)
deque.inserir_front(2)
deque.exibir_elementos()
deque.inserir_final(3)
deque.inserir_front(5)
deque.exibir_elementos()
deque.remover_final()
deque.exibir_elementos()
deque.remover_front()
deque.exibir_elementos()"""