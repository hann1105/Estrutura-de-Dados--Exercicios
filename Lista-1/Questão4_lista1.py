""" Implemente uma função para mesclar duas listas encadeadas ordenadas em uma única
lista encadeada também ordenada por idade. As listas de entrada já estão em ordem
crescente. Discuta a eficiência do algoritmo e possíveis otimizações."""

class Node:
    def __init__(self, nome, idade):
        self.nome = nome        
        self.idade = idade       
        self.next = None         # ponteiro para o próximo nó 

class Lista:
    def __init__(self):
        self.head = None     

    def inserir(self, nome, idade): #Insere de forma ordenada por idade (crescente) 
        
        new_node = Node(nome, idade)

        # lista vazia ou novo nó deve ir antes do head
        if self.head is None or idade < self.head.idade:
            new_node.next = self.head   # o próximo do novo nó será o head
            self.head = new_node        # o head passa a ser o novo nó
            return

        # encontrar a posição correta no meio/fim
        current = self.head
        # Avança enquanto o próximo existir e tiver idade menor que a do novo nó
        while current.next and current.next.idade < idade:
            current = current.next
        new_node.next = current.next #new node. next vai apontar para o póximo current
        current.next = new_node 

    def mostrar(self):
        if not self.head:
            print("Lista vazia")
            return
        current = self.head
        while current:
            print(f"{current.nome} - {current.idade}")
            current = current.next


def mesclar(l1, l2):
    
    #l1: Lista ordenada
    #l2: Lista ordenada
    # Nó ficticio (dummy) para simplificar a ligação dos nós no resultado.
    # Ele não representa um dado real; serve apenas como "âncora" do começo e evita muitos if's, e o dummy.next sempre aponta para o inico da lista
    dummy = Node(None, None) #ou seja, começa como none
    tail = dummy  # 'tail' manterá o último nó da lista resultante que está sendo constru´da com o dummy
 #o tail sempre aponta para o último nó da nova lista construída até o momento
    # Ponteiros que percorrem as duas listas
    p1=l1.head
    p2=l2.head

    # Enquanto houver elementos nas duas listas ele vai andar
    while p1 and p2: #está pegando um nó de cada lista por vez, de acordo com o menor
        # Escolhe o MENOR (ordem crescente por idade) e conecta no 'tail'
        if p1.idade <= p2.idade: #vê qual é a menor  idade 
            tail.next = p1     # o proximo depois do tail será o p1 que é menor de idade,Adiciona o menor à lista nova 
        else:
            tail.next = p2     # caso p2 for menor, o próximo nó do tail será o p2
            p2 = p2.next       # avança p2

        tail = tail.next       # atualiza 'tail' para o último nó adicionado, para saber onde a lista está

    # Quando uma lista acabar, conecta o resto da outra lista (que já está ordenado)
    if p1 is not None: #quando uma lista acaba, a outra ainda pode ter componentes, então liga os restos dos componentes ordenados no final
        tail.next = p1
    else:
        tail.next = p2


    # Constrói a nova lista com head em dummy.next (primeiro nó real)
    nova_lista = Lista()
    nova_lista.head = dummy.next #dummy.next é o primeiro nó
    return nova_lista


#teste
if __name__ == "__main__":
    lista1 = Lista()
    lista1.inserir("Paola", 19)
    lista1.inserir("Lucas", 21)

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
