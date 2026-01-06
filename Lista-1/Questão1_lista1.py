""" 1. Modele um TAD para representar livros de uma biblioteca (titulo, autor, ano, código). Em
seguida, implemente operações básicas: adicionar livro, buscar por titulo e remover por
código."""

class Node():
    def __init__(self,titulo,autor,ano,codigo):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.codigo=codigo
        self.next=None

class Biblioteca:
    def __init__(self):
        self.head=None

    def adicionar_livro(self,titulo,autor,ano,codigo):
        new_node=Node(titulo,autor,ano,codigo)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
        
    def remover_livro(self,codigo):
        if self.head is None:
            print("Biblioteca vazia")
            return
        if self.head.codigo==codigo:
            self.head=self.head.next
            print("Livro removido com sucesso!")
            return
        current=self.head
        while current.next is not None and current.next.codigo != codigo:
            current=current.next
        if current.next is None:
            print("Livro não encontrado")
        else:
            current.next=current.next.next
            print("Livro removido com sucesso")
    
    def buscar_livro(self,titulo):
        current=self.head
        while current is not None:
            if current.titulo==titulo:
                return current
            current=current.next
        return None
    
    def mostrar_livros(self):
        if self.head is None:
            print("Nenhum livro cadastrado.")
            return
        current = self.head
        while current:
            print(f"{current.codigo} - {current.titulo} | {current.autor} ({current.ano})")
            current = current.next

def main():
    library=Biblioteca()
    print("Bem vindo!")
    while True:
        print("------------ MENU ------------")
        print("A) Adicionar Livro")
        print("B) Buscar Livro")
        print("R) Remover Livro")
        print("L) Listar Livros")
        print("S) Sair")

        opcao=str(input("Escolha uma opção para continuar: ")).upper()
        if opcao=="A":
            titulo=str(input("Digite o titulo do livro: "))
            autor=str(input("Digite o autor do livro: "))
            ano=int(input("Digite o ano de publicação do livro: "))
            codigo=int(input("Digite o código do livro: "))
            library.adicionar_livro(titulo,autor,ano,codigo)
            print("Livro adicionado com sucesso!")
        
        elif opcao=="B":
            titulo_livro=str(input("Digite o titulo do livro: "))
            livro=library.buscar_livro(titulo_livro)
            if titulo_livro:
                print(f"Livro encontrado: {livro.titulo} - {livro.autor} ({livro.ano}) | Código: {livro.codigo}")
            else:
                print("Livro não encontrado.")
        
        elif opcao=="R":
            codigo_livro=int(input("Digite o código do livro que deseja remover: "))
            library.remover_livro(codigo_livro)
        
        elif opcao=="L":
            library.mostrar_livros()
        
        elif opcao=="S":
            print("Encerrando...")
            break

        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()