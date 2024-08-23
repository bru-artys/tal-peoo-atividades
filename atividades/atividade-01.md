# Atividade 01

## Explicações

**Classe**: É um modelo para criar objetos. A Classe define os atributos (características) e métodos (ações) dos objetos dessa classe.

**Objeto**: É uma instância de uma classe. Objeto possui todas os atributos e métodos da sua classe.

**Atributos**: São as características de um objeto, como nome, idade, cor, etc. São como as variáveis dentro de uma classe.

**Métodos**: São as ações que um objeto pode realizar, como andar, falar, calcular, etc. São as funções dentro de uma classe.

**Construtor**: Um método especial chamado `__init__` que é executado automaticamente quando um objeto é criado. Ele é usado para inicializar os atributos do objeto.

---

## Exemplo

**[pessoa.py](../exemplos/pessoa.py)**
```python
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

# Criando um objeto da classe
pessoa1 = Pessoa("Ana", 18, 1.75)
# Também podemos criar um objetos dessa forma
pessoa2 = Pessoa(nome="Julio", idade=19, altura=1.80)

# Depois de criar um objeto podemos chamar os métodos da classe dele
pessoa1.andar()
# Ou exibir seus atributos
print(f"Nome: {pessoa2.nome}. Idade: {pessoa2.idade}")

```

---

## Questões

**Instruções**: Crie um arquivo chamado `cachorro.py` e faça as seguintes questões.

1. Crie uma classe `Cachorro` com os atributos nome, raça, peso, idade e vacinado. Defina idade como `int`, peso como `float`, vacinado como `bool` (True ou False), os demais atributos como `string`.

2. Defina esses atributos no **construtor da classe**.

3. Crie o método `latir` para a classe, esse método deve exibir o barulho do cachorro.

4. Crie o método `tem_vacina` para a classe, esse método deve verificar e exibir se o cachorro é vacinado ou não.

5. Crie um objeto da classe Cachorro e defina seus atributos. Mostre esses atributos com o `print`, faça a chamada dos métodos desse objeto.