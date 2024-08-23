class Pessoa:
    # Atributos da Classe Pessoa
    nome = ""
    idade = 0
    altura = 0.0

    # O construtor recebe os atributos
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    # Métodos define ações do objeto
    def andar(self):
        print(f"{self.nome} está andando...")

    # Métodos podem alterar os valores dos atributos da classe
    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} completou {self.idade} anos!")

    # Métodos podem receber variaveis de fora da classe
    def adicionar_idade(self, anos):
        self.idade = self.idade + anos
        print(f"{self.nome} tem {anos} a mais! Agora tem {self.idade}")


# Criando um objeto da classe
pessoa1 = Pessoa("Ana", 18, 1.75)
# Também podemos criar um objetos dessa forma
pessoa2 = Pessoa(nome="Julio", idade=19, altura=1.80)

# Depois de criar um objeto podemos chamar os métodos da classe dele
pessoa1.andar()
# Ou exibir seus atributos
print(f"Nome: {pessoa2.nome}. Idade: {pessoa2.idade}")


pessoa3 = Pessoa(nome="Pedro", idade=16, altura=1.60)

# Mostra a idade inicial
print(f"{pessoa3.nome} tem {pessoa3.idade} anos.")

# Chama o método para fazer aniversário
pessoa3.fazer_aniversario()  # Agora a idade é 17

# Pede ao usuário quantos anos a mais adicionar
anos1 = int(input(f"Quantos anos a mais {pessoa3.nome} tem? "))

# Adiciona a quantidade de anos fornecida pelo usuário
pessoa3.adicionar_idade(anos1)
