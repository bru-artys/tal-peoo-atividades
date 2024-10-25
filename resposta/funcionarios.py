class Funcionario:
    nome = ""
    salario = 0.0
    departamento = ""

    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def mostrar_detalhes (self):
        print(f"{self.nome} trabalha no departamento {self.departamento} e tem um salario de R${self.salario}")

    def calcular_salario (self):
        print(f"O salário de {self.nome} é de R${self.salario}")
    
    def informacoes_funcionario (self):
        self.mostrar_detalhes()
        self.calcular_salario()

class Gerente (Funcionario):
    bonus = 0.0

    def __init__(self, nome, salario, departamento,bonus):
        super().__init__(nome, salario, departamento)
        self.bonus= bonus

    def calcular_salario(self):
        aumento = self.salario + self.bonus
        print(f"{self.nome} tem um bônus de R${self.bonus}, seu salario é R${aumento}")

class Vendedor(Funcionario):
    comissao = 0.0

    def __init__(self, nome, salario, departamento, comissão):
        super().__init__(nome, salario, departamento)
        self.comissao = comissão
      
    def calcular_salario(self):
        comissao = self.salario + self.comissao
        print(f"{self.nome} tem um bônus de R${self.comissao}, seu salario é R${comissao}")

class Progamador(Funcionario):
    horas_extras = 0
    valor_da_hora = 0.0

    def __init__(self, nome, salario, departamento,horaExtra,valorHora):
        super().__init__(nome, salario, departamento)
        self.horas_extras = horaExtra
        self.valor_da_hora = valorHora

    def calcular_salario(self):
        bonus = self.valor_da_hora * self.horas_extras
        aumento = self.salario + bonus
        print(f"{self.nome} recebeu um bônus de R${bonus}, seu salario é R${aumento}")

trabalhador1 = Gerente("Julios",2750.89,"McDounads",459.88)
trabalhador1.informacoes_funcionario()
print("--- --- ---")

trabalhador2 = Vendedor ("Alfredo",1600.99,"Bom_Sempre_Ganha$",2987.98)
trabalhador2.informacoes_funcionario()
print("--- --- ---")

trabalhador3 = Progamador("Ari",4589.90,"Microondas",6,2599.45)
trabalhador3.informacoes_funcionario()
print("--- --- ---")
