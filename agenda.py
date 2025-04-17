
def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favorito_contato):
    # Verifica se o contato já existe
   contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": favorito_contato}
   contatos.append(contato)
   print(f"Contato {nome_contato} adicionado com sucesso")
   return

def ver_contatos(contatos): 
    print("\nLista de Contatos:")
    print(contatos)
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        print(f"{indice}. [{status}] {contato['nome']} - {contato['telefone']} - {contato['email']}")
    return

def editar_contato(contatos, indice, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    indice_ajustado = int(indice) - 1
    if 0 <= indice_ajustado < len(contatos):
        if "nome" in contatos[indice_ajustado]:  # Assuming your task dictionary has a "nome" key
            contatos[indice_ajustado]["nome"] = novo_nome_contato
            print(f"Contato {indice} atualizado para {novo_nome_contato}")
        else:
            print("Estrutura do contato inválido.")
    else:
        print("Contato não encontrado.")
    return

def marcar_favorito(contatos, indice):
    indice_ajustado = int(indice) - 1
    contatos[indice_ajustado]["favorito"] = True
    print(f"Contato {indice} marcado como favorito")
    return

def lista_contato_favorito(lista_contatos, indice_str):
    """Marca um contato como favorito na lista."""
    try:
        indice = int(indice_str) - 1  # Adjust index to be 0-based
        if 0 <= indice < len(lista_contatos):
            lista_contatos[indice]['favorito'] = True
            print(f"Contato {lista_contatos[indice]['nome']} marcado como favorito.")
        else:
            print("Índice de contato inválido.")
    except ValueError:
        print("Por favor, digite um número válido para o contato.")
    return

def deletar_contatos(contatos, indice):
    indice_ajustado = int(indice) - 1
    contatos[indice_ajustado]["deletado"] = True
    print(f"Contato {indice} marcado como deletado")
    return

contatos = []
while True:
    print("\nOpções:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")


    if escolha == "1":
        nome_contato = input("Digite o nome do contato:")
        telefone_contato = input("Digite o telefone do contato:")
        email_contato = input("Digite o email do contato:")
        favorito_contato = False  # Valor padrão para favorito
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favorito_contato)


    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        indice = input("Digite o número do contato que deseja editar:")
        novo_nome_contato = input("Digite o novo nome do contato:")
        novo_telefone_contato = input("Digite o novo telefone do contato:")
        novo_email_contato = input("Digite o novo email do contato:")
        editar_contato(contatos, indice, novo_nome_contato, novo_telefone_contato, novo_email_contato)

    elif escolha == "4":
        ver_contatos(contatos)
        indice = input("Digite o número do contato que deseja marcar como favorito:")
        marcar_favorito(contatos, indice)

    elif escolha == "5":
        print("\nLista de Contatos Favoritos:")
        for indice_str, contato in enumerate(contatos, start=1):
            if contato["favorito"]:
                print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")
        lista_contato_favorito(contatos,indice_str)

    elif escolha == "6":
        ver_contatos(contatos)
        indice = input("Digite o número do contato que deseja deletar:")
        deletar_contatos(contatos, indice)

    if escolha == "7":
        break
    
    print("Programa finalizado")