"""
Classe abstrata ItemBiblioteca

atributos: codigo, titulo

método abstrato emprestar()

implemente __str__ e __repr__

Classes concretas:

Livro

Revista

Classe Usuario

Classe Biblioteca

lista de usuários

lista de itens
"""

from abc import ABC,abstractmethod

#CLASSE ITEM BIBLIOTECA
class ItemBiblioteca(ABC):
    def __init__(self, codigo:int,titulo:str):
        self.codigo = codigo
        self.titulo = titulo

    def __str__(self):
        return f"codigo:{self.codigo} , titulo:{self.titulo}"
    
    def __repr__(self):
        return f"ItemBiblioteca(codigo={self.codigo} , titulo={self.titulo})"

    @abstractmethod
    def emprestar(self):
        pass

#CLASSE LIVRO
class Livro(ItemBiblioteca):
    def __init__(self,codigo:int,titulo:str,autor:str):
        super().__init__(codigo,titulo)
        self.autor = autor

    def __repr__(self):
        return f"Livro(codigo={self.codigo} , titulo='{self.titulo}' , autor='{self.autor}')"
    
    def __str__(self):
        return f"codigo:{self.codigo} , titulo:{self.titulo} , autor:{self.autor}"

    def emprestar(self):
        return f"{self.titulo} emprestado com sucesso"
    

#CLASSE REVISTA
class Revista(ItemBiblioteca):
    def __init__(self,codigo:int,titulo:str,autor:str):
        super().__init__(codigo,titulo)
        self.autor = autor

    def __repr__(self):
        return f"Revista(codigo={self.codigo} , titulo='{self.titulo}' , autor='{self.autor}')"
    
    def __str__(self):
        return f"codigo:{self.codigo} , titulo:{self.titulo} , autor={self.autor}"

    def emprestar(self):
        return f"{self.titulo} emprestado com sucesso"

#CLASSE USUARIO
class Usuario:
    def __init__(self,nome:str):
        self.nome = nome
        self.itens = []
        
    def __repr__(self):
        return f"Usuario(nome='{self.nome}')"
    
    def __str__(self):
        return f"nome:{self.nome}"
    
    def realizar_compra(self,item):
        self.itens.append(item)
        return f"{item.titulo} comprado com sucesso"
    

#CLASSE BIBLIOTECA
class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.itens = []

    def __repr__(self):
        return f"Biblioteca(usuarios={self.usuarios} , itens={self.itens})"

    def inserir_usuarios(self,*usuario):
        self.usuarios.extend(usuario)

    def inserir_itens(self,*item):
        self.itens.extend(item)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print("usuario:" , usuario)

    def listar_itens(self):
       for item in self.itens:
           print("item:" , item)


#DADOS
livro_1 = Livro(102, "It a coisa" , "Stephen King")
livro_2 = Livro(9384, "Harry Potter" , "JK Rowling")

revista_1 = Revista(384, "Casas Bahia" , "Marcos Miguel")
revista_2 = Revista(458, "Rockstar Games" , "Peter Michael")

usuario_1 = Usuario("Marcos")
usuario_1.realizar_compra(livro_1)

usuario_2 = Usuario("Miguel")
usuario_2.realizar_compra(revista_2)

biblioteca_1 = Biblioteca()
biblioteca_1.inserir_itens(livro_1, livro_2, revista_1, revista_2)
biblioteca_1.inserir_usuarios(usuario_1,usuario_2)

biblioteca_1.listar_itens()
biblioteca_1.listar_usuarios()

