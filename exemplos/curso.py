# Relacionamento: Estudante pode estar associado a um ou mais cursos
class Estudante:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def mostrar_detalhes(self):
        print(f"Estudante: {self.nome}")
        print(f"Idade: {self.idade}")
        print("-" * 30)


# Relacionamento: Curso pode ter muitos estudantes associados
class Curso:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome        # Nome do curso
        self.codigo = codigo    # Código único do curso
        self.estudantes = []    # Lista para armazenar objetos do tipo Estudante

    # Relacionamento: adiciona um estudante a um curso
    def adicionar_estudante(self, estudante: Estudante):
        if estudante not in self.estudantes:    # Verifica se o estudante já não está associado
            self.estudantes.append(estudante)   # Adiciona o estudante ao curso

    # Método para listar os estudantes do curso
    def listar_estudantes(self):
        print(f"Estudantes no curso '{self.nome}':")
        for estudante in self.estudantes:   # Passa por cada objeto da lista estudantes
            print(f"  - {estudante.nome}")  # Exibe o nome de cada estudante
        if not self.estudantes:             # Verifica se a lista está vazia
            print("  Nenhum estudante matriculado ainda.")
        print("-" * 30)

# Aqui iniciamos as conexões entre os objetos
# Um estudante pode estar em vários cursos, e um curso pode ter muitos estudantes

estudante1 = Estudante("Ana", 20)
estudante2 = Estudante("Carlos", 22)
estudante3 = Estudante("Beatriz", 19)

curso1 = Curso("Programação em Python", "PP101")
curso2 = Curso("Desing Web", "DW201")

# Relacionando estudantes com cursos
# Cada estudante é adicionado à lista de estudantes de um curso
curso1.adicionar_estudante(estudante1)
curso1.adicionar_estudante(estudante2)

curso2.adicionar_estudante(estudante3)
curso2.adicionar_estudante(estudante1)

# Listando os estudantes de cada curso
# Exibe os estudantes do curso Programação em Python
curso1.listar_estudantes()
# Exibe os estudantes do curso Desing Web
curso2.listar_estudantes()
