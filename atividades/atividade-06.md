# Atividade 06 - Relacionamentos

## Explicações

**Relacionamentos** na programação orientada a objetos representam como as classes se conectam ou interagem entre si. Esses relacionamentos ajudam a modelar cenários do mundo real em que objetos possuem associações entre si. Existem três tipos principais de relacionamentos:

- **Associação**: Uma classe usa outra, mas ambas podem existir separadamente. 

    Ex.: Um `Curso` tem vários `Estudantes`.

- **Agregação**: Uma classe contém outras, mas as partes podem existir sozinhas. 

    Ex.: Uma `Biblioteca` tem `Livros`, mas os `Livros` podem existir sem a `Biblioteca`.

- **Composição**: Uma classe depende completamente de suas partes. 
    
    Ex.: Um `Pedido` por ter `Itens`, mas os `Itens` não existem fora do contexto do `Pedido`.

---

## Exemplos

[curso.py](../exemplos/curso.py)

```python
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

```

---

## Questões

**Instruções**: Crie um arquivo chamado `biblioteca.py` e faça as seguintes questões.

1. Crie uma classe `Autor` com os atributos `nome`, `nacionalidade`, `idade`. Defina idade como `int` e os outros atributos como `string`.

2. Crie o método `mostrar_detalhes` para `Autor`, esse método deve exibir as informações do autor.

3. Crie uma classe `Livro` com os atributos `nome`, `autores`, `ano_lancamento`. Defina ano de lançamento como `int`, nome como `string` e autores como `list`, uma lista vazia por padrão.

4. Crie o método `mostrar_detalhes` para `Livro`, esse método deve exibir as informações do livro e seu(s) autor(es).

5. Crie o método `adicionar_autor` para `Livro`, esse método deve receber um objeto da classe `Autor` e adicioná-lo à lista `autores`. Se o autor não estiver na lista de autores, ele é adicionado a lista, se não, uma mensagem alertando que já foi adicionado é exibida.

    - `Autor Junin do Bolo adicionado ao livro "A volta dos que não foram"`

    - `Autor Junin do Bolo já está adicionado no livro "A volta dos que não foram"`


6. Crie uma classe `Biblioteca` com o atributo `livros`, defina livros como `list`, uma lista vazia por padrão.

7. Crie o método `adicionar_livro` para `Biblioteca`, esse método deve receber um objeto da classe `Livro` e adicioná-lo à lista `livros`. 

8. Crie o método `listar_livros` para `Biblioteca`, esse método deve exibir todos os livros da biblioteca.

9. Crie pelo menos três objetos `Autor` e `Livro`, e um objeto `Biblioteca`. Faça o teste de seus métodos.

**EXTRA**. Crie o método `buscar_livros_pelo_ano` para `Biblioteca`, esse método receber um ano (`int`) como parâmetro e deve percorrer a lista de `livros` da biblioteca procurando por livros daquele ano. Esses livros dever ser adicionados em uma lista e ela dever ser exibida para o usuário.


---