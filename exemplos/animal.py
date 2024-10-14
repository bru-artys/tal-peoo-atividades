# Classe Base é criada primeiro
class Animal:
    nome = ""
    idade = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} está emitindo um som.")

# Subclasse recebe a Classe Base, recebendo suas caracteristicas
class Cachorro(Animal):
    raca = ""
    # Novos atributos podem ser definidos para a Subclassse
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)   # Herança: herdando atributos da classe base
        self.raca = raca                # Herança: novo atributo específico do Cachorro

    def emitir_som(self):               # Polimorfismo: sobrescrevendo o método
        print(f"{self.nome}, o cachorro da raça {self.raca}, está latindo!")


class Gato(Animal):
    cor_pelo = ""

    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        print(f"{self.nome}, o gato com pelo {self.cor_pelo}, está miando.")


# Função polimórfica.
# Essa função recebe objetos do tipo Animal
# Então, pode receber objetos Cachorro e Gato também, pois herdam de Animal
def fazer_animal_emitir_som(animal):
    animal.emitir_som()

# Criando instâncias de subclasses
dog = Cachorro("Rex", 5, "Labrador")
cat = Gato("Mia", 3, "preto")

# Chamando a função polimórfica
fazer_animal_emitir_som(dog)
fazer_animal_emitir_som(cat)