class Dog :

    nome = ""
    raca = ""
    peso = 0.0
    idade = 0
    vacinado = True

    def __init__ (self, nome1, raca1, peso1, idade1, vacinado1):
        self.nome = nome1
        self.raca = raca1
        self.peso = peso1
        self.idade = idade1
        self.vacinado = vacinado1

    def latir (self):
        print(f"{self.nome} esta latindo...")
    
    def tem_vacina (self):
        if self.vacinado == True:
            print(f"{self.nome} é vacinado!")
        elif self.vacinado == False:
            print(f"{self.nome} nao é vacinado!")
            
    
dog1 = Dog ("zezin", "caramelo", 15, 1, False)

dog1.latir()
dog1.tem_vacina()

print (f"nome: {dog1.nome}. raca: {dog1.raca}. peso: {dog1.peso}. idade: {dog1.idade}. vacinado:{dog1.vacinado} ")
