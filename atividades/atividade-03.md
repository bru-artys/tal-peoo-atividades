# Atividade 01

## Explicações

A **herança** é um principio que permite a uma classe herdar atributos e métodos de outra classe. Isso ajuda na reusabilidade de código e facilita a manutenção. Por exemplo, classe `Animal` pode ter atributos como `nome` e `idade`, e suas subclasses, como `Cachorro` e `Gato`, herdam esses atributos.


O **polimorfismo** é quando objetos de direfentes classes sejam tratados como objetos de uma classe em comum. Por exemplo, um método de `Animal`, como `emitir_som`, pode ser passado para `Cachorro` ou `Gato` porque herdam de `Animal`, além disso os métodos podem ser reescritos, assim modificando o método para cada subclasse.

Funções polimorficas tratam diferentes objeto de forma igualitária. Por exemplo, objetos `Cachorro` e `Gato` seram tratados como `Animal`, dessa forma tornando o código mais flexível reutilizável.

---

## Exemplos

[**animal.py**](exemplos/animal.py)
```python
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

```

---

## Questões

**Instruções**: Crie um arquivo chamado `personagens.py` e faça as seguintes questões.

1. Crie uma classe base `Personagem` com os atributos nome, vida, força. Defina vida e força como `int`, nome como `string`.

2. Defina esses atributos no **construtor da classe base**.

3. Crie o método `mostrar_detalhes` para a classe base, esse método deve exibir os atributos do personagem.

4. Crie o método `atacar` para a classe base, esse método deve exibir que o personagem fez um ataque.

- Exemplo de Saída:
```
  Goldofredo fez um ataque com força 50!
```


5. Crie classes que herdam de Personagem, utilize o `super` para definir os atributos da classe base. Defina os novos atributos no construtor da classe.

- Guerreiro
    - Adicione o atributo arma (`string`)

    - Sobreescreva o método `atacar` para exibir o uso da arma

    - `Goldofredo ataca com Machado!`

- Mago
    - Adicione o atributo magia (`string`)

    - Sobreescreva o método `atacar` para exibir o uso da magia

    - `Falin usa a magia Bola de Fogo!`

- Arqueiro
    - Adicione o atributo flechas (`int`)

    - Sobreescreva o método `atacar` para utilizar flechas, a cada ataque reduza uma flecha. Se a quantidade de flechas for menor ou igual a zero, não executa o ataque.

    - `Ashe dispara uma flecha! 0 flechas restantes.`
    - `Ashe não tem mais flechas.`

---