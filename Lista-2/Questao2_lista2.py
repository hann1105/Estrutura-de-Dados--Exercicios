"""Ajuste o código anterior para criar uma função remover_duplicatas(fila) que recebe
uma fila como argumento e remove todas as duplicatas, deixando apenas a primeira
ocorrência de cada elemento na fila."""
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
            new_node.next=self.head 
            self.head.prev=new_node
            self.head=new_node

    def inserir_final(self,dado): #inserir no final
        new_node=Node(dado)
        if self.tail is None:
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
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
        
        dado=self.tail.dado
        self.tail=self.tail.prev
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
    
    #Implementando a função de excluir duplicatas
    def remover_duplicatas(self):
        vistos=set() #conjunto que não tem duplicatas
        current=self.head
        while current is not None:
            if current.dado in vistos: #se o valor do nó ja tiver no conjunto tem que remover
                if current.prev: #se o nó não é o primeiro
                    current.prev.next=current.next # o anterior vai ser o proximo, pulando o atual
                elif current.next: # se o nó não é o último
                    current.next.prev=current.prev # o prev do próximo nó vai ser o prev do current atual
                elif current==self.tail: # se o nó era o último 
                    self.tail=current.prev # o tail vai ser o anterior
            else: # não é duplicata
                vistos.add(current.dado)
            current=current.next

#teste
"""deque=Deque()
deque.inserir_final(3)
deque.inserir_front(11)
deque.inserir_front(8)
deque.inserir_final(13)
deque.inserir_final(3)
deque.exibir_elementos()
deque.remover_duplicatas()
deque.exibir_elementos()
"""