# Atividade 05 - Encapsulamentos

## Explicações

**Encapsulamento** é um dos conceitos da programação orientada a objetos que consiste em proteger os atributos ou métodos de uma classe, restringindo o acesso direto a eles e permitindo sua manipulação apenas por meio de métodos controlados (*getters* e *setters*, por exemplo). Essa prática ajuda a proteger os dados e controlar como eles são modificados, dando maior segurança e organização no código.

Em Python, o encapsulamento é implementado principalmente por convenções de nomeação:

- Prefixos como `_` (um underscore) indicam que um atributo ou método é **protegido** (não deve ser acessado diretamente, mas ainda pode ser).
- Prefixos como `__` (dois underscores) indicam que o atributo ou método é **privado**, dificultando o acesso direto fora da classe.

---

## Exemplos

[conta_corrente.py](../exemplos/conta_corrente.py)

```python
class ContaCorrente:
    def __init__(self, cpf: str, saldo: float):
        # Atributo privado para armazenar o saldo
        self.__saldo = saldo
        self.__cpf = cpf

    # Em métodos get retornamos o valor do atributo privado
    def get_saldo(self):
        return self.__saldo

    # Em métodos set recebemos um parâmetro e atribuímos seu valor ao atributo privado
    def set_saldo(self, saldo):
        self.__saldo = saldo

    # Outros métodos também podem acessar o atributos privados
    def mostrar_detalhes(self):
        print(f"CPF: {self.__cpf}")
        print(f"Saldo: R${self.__saldo}")

    # Outros métodos também podem modificar esses atributos privados
    def depositar(self, valor):
      if valor > 0:
          self.__saldo += valor
          print(f"Depósito de R${valor} realizado com sucesso.")
      else:
          print("O valor do depósito deve ser positivo.")

    # E é possível retornar valores não cadastrados, fazendo cálculos nas funções
    def simular_deposito(self, valor):
      return valor + self.get_saldo()

# Criando um objeto
conta = ContaCorrente(cpf="000.001.002-03", saldo=0.0)
conta.mostrar_detalhes()
conta.depositar(valor=200.50)

print(f"Mostrar saldo: {conta.get_saldo()}")
valor = 350.35
print(f"Deposito Simulado de {valor}. Saldo futuro: {conta.simular_deposito(valor)}")
```

---

## Questões

**Instruções**: Crie um arquivo chamado `produtos.py` e faça as seguintes questões.

1. Crie uma classe `Produto` com os atributos **privados** `nome`, `preco`, `estoque`. Defina preco como `float`, estoque como `int` e nome como `string`. Defina os atributos no construtor.

2. Crie o método `mostrar_detalhes` para a classe, esse método deve exibir as informações do produto.

3. Crie o métodos `get` para todos os atributos. Crie métodos `set` para preço e nome, por padrão estoque é igual a 0.

4. Crie o método `adicionar_estoque` para a classe, esse método deve receber `quantidade` como parâmetro. Se a quantidade for maior que zero, esse valor é adicionado ao estoque, se não um erro é exibido.

5. Crie o método `diminuir_estoque` para a classe, esse método deve receber `quantidade` como parâmetro. Se a quantidade for maior que zero e menor ou igual ao estoque atual, esse valor é subtraído ao estoque, se não um erro é exibido.

6. Crie um objeto da classe `Produto`, teste seus métodos `get` e `set` e faça a chamada dos outros métodos.

---
