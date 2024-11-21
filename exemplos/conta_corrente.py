
class ContaCorrente:
    def __init__(self, cpf: str, saldo: float):
        # Atributo privado para armazenar o saldo
        self.__saldo = saldo
        self.__cpf = cpf

    # Em métodos get retornamos o valor do atributo privado
    def get_saldo(self):
        return self.__saldo

    # Em métodos set recebemos um paramêtro e atribuimos seu valor ao atributo privado
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

    # E é possivel retorna valores não cadastrados, fazendo calculos nas funções
    def simular_deposito(self, valor):
      return valor + self.get_saldo()

# Criando um objeto
conta = ContaCorrente(cpf="000.001.002-03", saldo=0.0)
conta.mostrar_detalhes()
conta.depositar(valor=200.50)

print(f"Mostrar saldo: {conta.get_saldo()}")
valor = 350.35
print(f"Deposito Simulado de {valor}. Saldo futuro: {conta.simular_deposito(valor)}")