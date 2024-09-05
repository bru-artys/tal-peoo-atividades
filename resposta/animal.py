class Animal:

    especies = ""
    descricao= ""
    idade = 0
    peso = 0.0
    adulto = True

    def __init__(self, especies, descricao, idade, peso, adulto):
        self.especies = especies
        self.descricao = descricao
        self.idade = idade
        self.peso = peso
        self.adulto = adulto

    def adulto_especie (self):
        if self.adulto == True:
             print(f"o {self.especies} é um adulto.")
        elif self.adulto == False:
            print(f"o {self.especies} é um filhote.")    

    def mostrar_informações (self):
        print(f"o animal de tal caracteristica é da especie {self.especies} com a descrição {self.descricao}, tem uma idade de {self.idade} anos, pesa uns {self.peso}kg e o")
        self.adulto_especie()

    def alimentar (self, quantidade):
        if self.peso > quantidade : 
            self.peso += quantidade
            print(f"seu/sua {self.especies} tem o total de {self.peso}kg atualmente.")
        elif self.peso < quantidade:
            print(f" error")

    def buscar_alimento (self):
        if self.adulto == True:
            print(f"o {self.especies} é um adulto, ou seja, ele ja pode caçar seus alimentos.Na sua caça conseguiu.")
            quantidade = int (input("Quantos quantidade de alimento voce quer adicionar para o animal? "))
            
            self.alimentar(quantidade)
        elif self.adulto == False:
            print(f"o {self.especies} é um filhote, então ele não pode caçar, pois depende dos seus pais.")

animal1 = Animal ("lobo guara","canídeo endêmico da América do Sul",1 ,20.2,True)
animal1.mostrar_informações()

print("--- --- ---")

quantidade = int (input("Quantos quantidade de alimento voce quer adicionar para o animal? "))
animal1.alimentar(quantidade)

print("--- --- ---")

animal1.buscar_alimento()
print("--- --- ---")