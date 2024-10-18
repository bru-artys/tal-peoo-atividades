class Personagem:
   nome = ""
   vida = 0
   forca = 0

   def __init__ (self, nome, vida, força):
    self.nome = nome
    self.vida = vida
    self.forca = força

   def mostrar_detalhes (self):
     print(f"{self.nome} tem {self.vida} de vida e {self.forca} de força.")

   def atacar (self):
     print(f"{self.nome} fez um ataque com força {self.forca}!")

class Guerreiro(Personagem):
   arma = ""

   def __init__(self, nome, vida, forca, arma):
      super().__init__(nome, vida, forca)
      self.arma = arma
   
   def atacar (self):
     print(f"{self.nome} ataca com um(a) {self.arma}!")

class Mago(Personagem):
   magia = ""

   def __init__(self, nome, vida, força,magia):
     super().__init__(nome, vida, força)
     self.magia = magia 

   def atacar (self):
     print(f"{self.nome} usa magia {self.magia}!")

class Arqueiro(Personagem):
   flechas = 0 

   def __init__(self, nome, vida, força,flechas):
     super().__init__(nome, vida, força)
     self.flechas = flechas

   def atacar (self):
      if self.flechas <= 0:
        print(f"{self.nome} não tem mais flechas.")
      else:
        self.flechas = self.flechas - 1
        print(f"{self.nome} dispara uma flecha! {self.flechas} flechas restantes.")


jogador1 = Guerreiro("cavaleiro",75,60,"espada")
jogador1.atacar()

print("--- --- ---")

jogador2 = Mago ("ocultista",60,40,"decadência")
jogador2.atacar()

print("--- --- ---")

jogador3 = Arqueiro("Robin Hood",70,50,1)
jogador3.atacar()
jogador3.atacar()
print("--- --- ---")