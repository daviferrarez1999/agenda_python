import textwrap
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def carregar_contatos():
    contatos = []
    try:
        with open(ROOT_PATH / "contatos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, email, numero = linha.strip().split(", ")
                contatos.append({
                    "nome": nome.split(": ")[1],
                    "email": email.split(": ")[1],
                    "numero": numero.split(": ")[1]
                })
    except FileNotFoundError:
        pass
    return contatos


def salvar_contatos(contatos):
    with open(ROOT_PATH / "contatos.txt", "w", encoding="utf-8") as arquivo:
        for contato in contatos:
            arquivo.write(f"Nome: {contato['nome']}, Email: {contato['email']}, Número: {contato['numero']}\n")


def menu():
    menu = """

    [1] Inserir contato
    [2] Filtrar contatos
    [3] Excluir contato
    [4] Alterar dados de um contato
    [5] Listar contatos
    [6] Sair

    =>  """

    return input(textwrap.dedent(menu))


def inserir_contato(contatos):
    nome = input("Informe o nome do contato: ")
    contato = filtrar_contatos(nome, contatos)

    if contato:
        print("Já existe um contato com esse nome")
        return contatos

    numero = input(
        "Informe o numero que deseja cadastar no formato: (XX) XXXX-XXXX para telefone fixo e (XX) XXXXX-XXXX para celular: "
    )
    email = input("Informe o email do contato: ")

    contatos.append({"nome": nome, "email": email, "numero": numero})
    salvar_contatos(contatos)
    return contatos


def filtrar_contatos(nome, contatos):
    contatos_filtrados = [contato for contato in contatos if contato["nome"] == nome]
    return contatos_filtrados[0] if contatos_filtrados else None


def excluir_contato(contatos):
    nome = input("Informe o nome do contato que deseja excluir: ")
    contato = filtrar_contatos(nome, contatos)

    if contato:
        contatos.remove(contato)
        print("Contato removido com sucesso!\n")
        salvar_contatos(contatos)
    else:
        print("Contato não encontrado!\n")


def alterar_contato(contatos):
    nome = input("Informe o nome do contato que deseja alterar: ")
    contato = filtrar_contatos(nome, contatos)

    if contato:
        print(contato)

        while True:
            opcao = """

            [an] Alterar nome
            [ae] Alterar email
            [anum] Alterar número
            [s] Sair

            => """

            opcao = input(textwrap.dedent(opcao))

            if opcao == "an":
                novo_nome = input("Informe o novo nome: ")
                if novo_nome:
                    contato["nome"] = novo_nome
                print("O nome foi atualizado com sucesso!\n")

            elif opcao == "ae":
                novo_email = input("Informe o novo e-mail: ")
                if novo_email:
                    contato["email"] = novo_email
                print("O e-mail foi atualizado com sucesso!\n")

            elif opcao == "anum":
                novo_numero = input("Informe o novo numero: ")
                if novo_numero:
                    contato["numero"] = novo_numero
                print("O numero foi atualizado com sucesso!\n")

            elif opcao == "s":
                break

            else:
                print(
                    "Opcao invalida! Informe uma das opcoes acima para realizar a operacao corretamente!\n"
                )

        salvar_contatos(contatos)

    else:
        print("Contato não encontrado!\n")


def listar_contatos(contatos):
    for contato in contatos:
        lista = f"""\
            Nome: \t{contato['nome']}
            Numero: {contato['numero']}
            E-mail: {contato['email']}
        """
        print(textwrap.dedent(lista))


def main():

    contatos = carregar_contatos()

    while True:

        opcao_agenda = menu()

        if opcao_agenda == "1":
            contatos = inserir_contato(contatos)

        elif opcao_agenda == "2":
            nome = input("Informe o nome do contato que desja filtrar: ")
            contato = filtrar_contatos(nome, contatos)
            if contato:
                print(contato)
            else:
                print("Nao existe esse contato!\n")

        elif opcao_agenda == "3":
            excluir_contato(contatos)

        elif opcao_agenda == "4":
            alterar_contato(contatos)

        elif opcao_agenda == "5":
            listar_contatos(contatos)

        elif opcao_agenda == "6":
            break

        else:
            print("Opcao invalida!\n")


main()
