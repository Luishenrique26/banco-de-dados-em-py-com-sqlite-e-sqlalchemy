import re

# Modelo
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao})"

# Visão
class LivroView:
    @staticmethod
    def exibir_livro(livro):
        print(f"Livro cadastrado: {livro}")

    @staticmethod
    def exibir_mensagem(mensagem):
        print(mensagem)

# Controlador
class LivroController:
    def __init__(self, view):
        self.view = view
        self.livros = []

    def cadastrar_livro(self, titulo, autor, ano_publicacao):
        # Validação de dados (opcional)
        if not titulo or not autor or not re.match(r"^\d{4}$", ano_publicacao):
            self.view.exibir_mensagem("Dados inválidos. Certifique-se de preencher corretamente.")
            return
        novo_livro = Livro(titulo, autor, ano_publicacao)
        self.livros.append(novo_livro)
        self.view.exibir_livro(novo_livro)

    def listar_livros(self):
        if self.livros:
            print("\nLista de livros cadastrados:")
            for livro in self.livros:
                print(livro)
        else:
            self.view.exibir_mensagem("Nenhum livro cadastrado ainda.")

# Programa principal
def main():
    view = LivroView()
    controller = LivroController(view)

    while True:
        print("\nMenu:")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação (quatro dígitos): ")
            controller.cadastrar_livro(titulo, autor, ano_publicacao)
        elif escolha == '2':
            controller.listar_livros()
        elif escolha == '3':
            print("Encerrando o programa. Até mais!")
            break
        else:
            view.exibir_mensagem("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
