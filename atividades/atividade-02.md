# Atividade 02

## Exemplos
Os métodos, as funções de uma classe, podem acessar e alterar valores dos atributos do objeto.

**[pessoa.py](../exemplos/pessoa.py)**
```python
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

    # Métodos podem alterar os valores dos atributos da classe
    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} completou {self.idade} anos!")

    # Métodos podem receber variaveis de fora da classe
    def adicionar_idade(self, anos):
        self.idade = self.idade + anos
        print(f"{self.nome} tem {anos} a mais! Agora tem {self.idade}")
     
```

- Método `fazer_aniversario`:
Este método adiciona mais 1 no atributo idade do objeto e imprime uma mensagem informando quantos anos completou.

- Método `adicionar_idade`:
Este método adiciona um número específico no atributo idade do objeto e imprime uma mensagem informando os anos.

```python
pessoa3 = Pessoa(nome="Pedro", idade=16, altura=1.60)
# Mostra a idade inicial
print(f"{pessoa3.nome} tem {pessoa3.idade} anos.")

# Chama o método para fazer aniversário
pessoa3.fazer_aniversario()  # idade = 17

# Perguta ao usuário quantos anos a mais adicionar
anos1 = int(input(f"Quantos anos a mais {pessoa3.nome} tem? "))

# Adiciona a quantidade de anos digitada pelo usuário
pessoa3.adicionar_idade(anos1)

```

## Questões
**Instruções**: Crie um arquivo chamado `animal.py` e faça as seguintes questões.

1. Crie uma `classe Animal` com os atributos espécie, descrição, idade, peso, e adulto. Defina peso como `float`, idade como `int`, adulto como `bool` (True ou False), os demais atributos como `string`.

2. Defina esses atributos no construtor da classe.

3. Crie o método `mostrar_informacoes` para a classe, esse método deve imprimir os atributos do animal.

4. Crie o método `alimentar` para a classe, esse método deve receber a variável `quantidade`. Se a quantidade de alimento for maior que o peso do animal, deve imprimir uma mensagem de erro. Caso contrário, deve atualizar o peso somando a quantidade de alimento.

5. Crie o método `buscar_alimento`. Esse método deve verificar se o animal é adulto ou não. Se for adulto, deve informar que ele já pode caçar seu alimento. Caso contrário, informar que ele não pode caçar sozinho.

6. Crie um objeto da classe Animal e defina seus atributos. Faça a chamada dos métodos desse objeto.

- EXTRA. No método `buscar_alimento`, se o animal for adulto, pergunte ao usuário a quantidade de alimento que ele caçou e faça a chamada do método `alimentar`.