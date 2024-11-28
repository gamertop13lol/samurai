livros = [{'título': 'Os Cavalos são Os Melhores', 'autor': 'Cavalo', 'emprestado': False, 'id': 1}, {'título': 'És um Animal', 'autor': 'Sopa de pedra', 'emprestado': False, 'id': 2}, {'título': 'És um Animal', 'autor': 'Sopa de pedra', 'emprestado': False, 'id': 3}, {'título': 'A Bíblia', 'autor': 'Não sei', 'emprestado': False, 'id': 4}, {'título': 'És um Animal', 'autor': 'Sopa de pedra', 'emprestado': False, 'id': 5}, {'título': 'Amor às Estantes', 'autor': 'Partitura da Silva', 'emprestado': False, 'id': 6}, {'título': 'COBOL pra burros', 'autor': 'José Rodrigo António Barroso Pedroso Pereira Macieira', 'emprestado': False, 'id': 7}] # [{"título", "autor", "id", "emprestado": False}]
livrosemprestados = []
utilizadores = [{"nome": "Ana", "id": 1}, {"nome": "Bruno", "id": 2}, {"nome": "Célia", "id": 3}, {"nome": "Dinis", "id": 4}] # [{"nome", "id"}]

def pesquisaPorID(array, id):
    s = 0
    i = len(array)//2
    while array[i]["id"] != id:
        if array[i]["id"] > id:
            array = array[0:i]
        else:
            s += i
            array = array[i:]
        i = len(array)//2
        if i == 0:
            return -1
    return s + i

def pesquisaPorTitulo(titulo):
    global livros
    res = []
    for livro in livros:
        if livro["título"] == titulo:
            res.append(livro)
    return res

def construirLivro():
    print("Dados do livro:\n")
    titulo = input("Título: ")
    autor = input("Autor: ")
    return {"título": titulo, "autor": autor, "emprestado": False}

def listarLivros():
    global livros
    print("=== Livros ===\n")
    for livro in livros:
        print(f'= {livro["título"]} || de {livro["autor"]}, ID do livro {livro["id"]}')

def adicionarLivro():
    global livros
    livro = construirLivro()
    if livros != []:
        livro["id"] = livros[-1]["id"] + 1
        livros.append(livro)
        return
    livro["id"] = 1
    livros.append(livro)

def removerLivro():
    global livros, livrosemprestados
    titulo = input("Qual o título dos livros que deseja remover? ")
    livro = pesquisaPorTitulo(titulo)
    if input(f"Confirma que quer remover todos os livros de título {titulo} (são {len(livro)} livros)? [y/N] ").lower() != "y":
        print("Nenhum livro foi ejetado (?!)")
        return
    for l in livro:
        livros.remove(l)
        if l in livrosemprestados:
            livrosemprestados.remove(l)
    if livro != []:
        print(titulo + " não era o impostor.")
    else:
        print("Nenhum livro foi encontrado.")

def removerLivroPorID():
    global livros, livrosemprestados
    id = int(input("Qual o ID do livro que deseja remover? "))
    index = pesquisaPorID(livros, id)
    if index == -1:
        print("Livro não encontrado!")
    if input(f"Confirma que quer remover o livro {livros[index]["título"]}? [y/N] ").lower() != "y":
        print("Nenhum livro foi ejetado (?!)")
        return
    livro = livros[index]
    print(livro["título"] + " não era o impostor.")
    if livro in livrosemprestados:
        livrosemprestados.remove(livro)
    livros.remove(livro)

def emprestarLivro():
    global livros, utilizadores
    livroid = int(input("Qual o ID do livro? "))
    userid = int(input("Qual o ID do utilizador? "))
    index = pesquisaPorID(livros, livroid)
    userindex = pesquisaPorID(utilizadores, userid)
    if index == -1:
        print("Livro não encontrado!")
        return
    if userindex == -1:
        print("Utilizador não encontrado!")
        return
    livro = livros[index]
    livro["emprestado"] = userid
    livrosemprestados.append(livro)
    print(f"Livro {livro["título"]} emprestado a {utilizadores[userindex]["nome"]}.")

def devolverLivro():
    global livros, utilizadores
    livroid = int(input("Qual o ID do livro? "))
    userid = int(input("Qual o ID do utilizador? "))
    index = pesquisaPorID(livros, livroid)
    userindex = pesquisaPorID(utilizadores, userid)
    if index == -1:
        print("Livro não encontrado!")
        return
    if userindex == -1:
        print("Utilizador não encontrado!")
        return
    livro = livros[index]
    if livro not in livrosemprestados:
        print("O livro não estava emprestado!")
        return
    livrosemprestados.remove(livro)
    livro["emprestado"] = False
    print(f"Livro {livro["título"]}, antes emprestado a {utilizadores[userindex]["nome"]}, devolvido à Biblioteca!")

def listarLivrosEmprestados():
    global livrosemprestados, utilizadores
    print("=== Livros emprestados ===")
    for livro in livrosemprestados:
        print(f"= {livro["título"]} || de {livro["autor"]} - ID do livro {livro["id"]} || Emprestado a {utilizadores[pesquisaPorID(utilizadores, livro["emprestado"])]["nome"]}, ID {livro["emprestado"]}")

def informacoesDoLivro():
    global livros, utilizadores
    titulo = input("Qual o título do livro? ")
    livro = pesquisaPorTitulo(titulo)
    print(f"=== Livro {titulo} === \nAutor: {livro[0]["autor"]}\nCópias:")
    for l in livro:
        print(f"= ID {l["id"]}: {"Disponível" if not l["emprestado"] else f"Emprestado a {utilizadores[pesquisaPorID(utilizadores, l["emprestado"])]["nome"]}, ID {l["emprestado"]}"}")

def sair():
    global operar
    operar = False

operar = True
print("Bem vindo à Biblioteca!\n")
operacoes = {"listarlivros": listarLivros, "adicionarlivro": adicionarLivro, "removerlivro": removerLivro, "removerlivroporid": removerLivroPorID, "pedirlivrosemprestados": emprestarLivro, "devolverlivros": devolverLivro, "listarlivrosemprestados": listarLivrosEmprestados, "informaçõesdolivro": informacoesDoLivro, "sair": sair}
operacoesvalidas = ["listarlivros", "adicionarlivro", "removerlivro", "removerlivroporid", "informaçõesdolivro", "pedirlivrosemprestados", "devolverlivros", "listarlivrosemprestados"]

while operar:
    print("""
    == Operações ==\n
    Listar livros
    Adicionar livro
    Remover livro (por ID)
    Pedir livros emprestados
    Devolver livros
    Listar livros emprestados
    Informações do livro
    Sair\n""")
    operacao = input("Que operação deseja realizar? ").replace(" ", "").lower()
    if operacao in operacoesvalidas:
        operacoes[operacao]()
    else:
        print("Operação inválida!\n")