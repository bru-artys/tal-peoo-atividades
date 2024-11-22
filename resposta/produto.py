class Produto:

    def __init__(self,nome: str,preço: float,estoque = 0):
        self.__nome = nome 
        self.__preco = preço
        self.__estoque = estoque

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_preço(self):
        return self.__preco
    
    def set_preço(self,preco):
        self.__preco = preco

    def get_estoque(self):
        return self.__estoque
    

    def mostrar_detalhes(self):
        print(f"nome: {self.__nome}")
        print(f"preco:R$ {self.__preco}")
        print(f"estoque: {self.__estoque}")

    def adicionar_estoque(self,quantidade):
        if quantidade > 0:
            self.__estoque += quantidade  
            print(f"estoque atual:{self.__estoque}")
        else:
           quantidade < 0
           print(f"estoque atual:esgotado") 

    def diminuir_estoque(self,quantidade):
        if quantidade > 0:
            self.__estoque -= quantidade  
            print(f"estoque atual:{self.__estoque}")
        else:
           quantidade < 0
           print(f"estoque atual:esgotado") 


produto1 = Produto("maça",4.99,2)
produto1.mostrar_detalhes()
print("--- --- ---")
produto1.adicionar_estoque(quantidade=1)
print("--- --- ---")
produto1.diminuir_estoque(quantidade= 2)

print("--- --- ---")
print(produto1.get_nome())
produto1.set_nome("pão")
print(produto1.get_nome())
print("--- --- ---")
print(produto1.get_preço())
produto1.set_preço(2.50)
print(produto1.get_preço())

produto1.mostrar_detalhes()
# print(objeto.get_atributo())
# variavel = "dois"
# objeto.set_atributo(variavel)