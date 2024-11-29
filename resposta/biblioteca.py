class Autor:
    
    def __init__(self,nome: str,nacionaldade: str,idade:int):
        self.nome = nome
        self.nacionalidade = nacionaldade
        self.idade = idade

    def mostrar_detalhes (self):
        print(f"Autor:{self.nome}")
        print(f"Nacionalidade:{self.nacionalidade}")
        print(f"Idade: {self.idade} anos")

class Livro:

    def __init__(self, nome: str, ano_lancamento: int):
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.autores = []

    def mostrar_detalhes(self):
        print(f"Livro: {self.nome}")
        print(f"Ano de Lançamento: {self.ano_lancamento}")
        print("Autores:")
        if self.autores:
            for autor in self.autores:
                print(f" {autor.nome}, {autor.nacionalidade}, {autor.idade} anos")
        else:
            print("  Nenhum autor cadastrado.")

    def adicionar_autor(self, autor: Autor):
        if autor not in self.autores:
            self.autores.append(autor)
            print(f"Autor {autor.nome} adicionado ao livro {self.nome}")
        else:
            print(f"Autor {autor.nome} já está adicionado no livro {self.nome}")


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro {livro.nome} adicionado à biblioteca.")

    def listar_livros(self):
        if self.livros:
            print("Livros na biblioteca:")
            for livro in self.livros:
                livro.mostrar_detalhes()
                print()
        else:
            print("Nenhum livro na biblioteca.")

    def buscar_livros_pelo_ano(self, ano: int):
        livros_encontrados = [livro for livro in self.livros if livro.ano_lancamento == ano]
        if livros_encontrados:
            print(f"Livros lançados no ano {ano}:")
            for livro in livros_encontrados:
                livro.mostrar_detalhes()
                print()
        else:
            print(f"Nenhum livro encontrado para o ano {ano}.")

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
        print(f"Livro {livro.nome} adicionado à biblioteca.")

    def listar_livros(self):
        if self.livros:
            print("Livros na biblioteca:")
            for livro in self.livros:
                livro.mostrar_detalhes()
                print()
        else:
            print("Nenhum livro na biblioteca.")

    def buscar_livros_pelo_ano(self, ano: int):
        livros_encontrados = [livro for livro in self.livros if livro.ano_lancamento == ano]
        if livros_encontrados:
            print(f"Livros lançados no ano {ano}:")
            for livro in livros_encontrados:
                livro.mostrar_detalhes()
                print()
        else:
            print(f"Nenhum livro encontrado para o ano {ano}.")

autor1 = Autor("Junin do Bolo", "Brasileiro", 35)
autor2 = Autor("Maria das Couves", "Portuguesa", 42)
autor3 = Autor("John Smith", "Americano", 50)
livro1 = Livro("A volta dos que não foram", 2021)
livro2 = Livro("O mistério do tempo", 2018)
livro3 = Livro("Viagem ao infinito", 2021)


livro1.adicionar_autor(autor1)
livro1.adicionar_autor(autor2)
livro1.adicionar_autor(autor1) 
livro2.adicionar_autor(autor3)
livro3.adicionar_autor(autor2)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()

biblioteca.buscar_livros_pelo_ano(2021)
biblioteca.buscar_livros_pelo_ano(2015)


