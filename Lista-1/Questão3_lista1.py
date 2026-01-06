""" Desenvolva uma função para inserir um nó em uma lista encadeada circular de pessoas,
garantindo que a ordenação crescente por idade seja mantida. Defina atributos
adequados para o nó, como nome e idade, e valide se a lista continua circular após a
inserção."""
class Node:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
        self.next=None

class Pessoas:
    def __init__(self):
        self.head=None

    def inserir(self,nome,idade):
        new_node=Node(nome,idade)
        if self.head is None: #se estiver vazia
            self.head=new_node #cabeça vai ser o novo nó
            new_node.next=self.head #e o next do novo nó será a cabeça, deixando circular
            return
        current=self.head #caso não, o current começa na cabeça
        if idade <self.head.idade: #se a idade for menino que a da cabeça
            while current.next !=self.head: #enquanto o current. next for diferente da cabeça (pois se chega na cabeça é o final)
                current=current.next #vai andar a lista
            current.next=new_node #vai adicionar o novo nó antes da cabeça
            new_node.next=self.head #o próximo do novo nó será a cabeça deixando circular
            self.head=new_node # substitui a cabeça pela menor idade
            return
        
        while current.next!=self.head and current.next.idade<idade: #se a idade inserida for maior que as que já estão
            current=current.next # vai andar a lista toda ate chegar antes do head, vai adicionar o novo nó entre current e current.next
        new_node.next = current.next # adiciona o novo nó , o new_node aponta para o próximo do current
        current.next = new_node #e o current atual aponta para o novo nó
    
    def mostrar(self):
        if self.head is None:
            print("Lista vazia")
            return
        
        current=self.head
        print("----Pessoas----")
        while True:
            print(f"{current.nome} - {current.idade} ")
            current=current.next
            if current==self.head:
                break
    
    def validar_circularidade(self):
        if self.head is None:
            print("A lista está vazia! E é circular")
            return True
        
        current=self.head.next #começa a percorrer a partir do segundo nó
        while current is not None and current !=self.head: #Enquanto current não for None (fim da lista normal) e ainda não tiver voltado para self.head
            current=current.next
        if current ==self.head: #se o últimoo nó for a cabeça novamente, então é circular
            print("Lista circular!")
            return True
        else:
            print("Lista não está circular")
            return False

pessoa=Pessoas()
pessoa.inserir("Paola",19)
pessoa.inserir("Lucas",21)
pessoa.inserir("maria",9)
pessoa.inserir("Isaac",34)
pessoa.inserir("Alex",2)
pessoa.mostrar()
pessoa.validar_circularidade()