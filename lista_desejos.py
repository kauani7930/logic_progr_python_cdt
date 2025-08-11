print ("Minha lista de Desejo para o Futuro\n")
NOME_ARQUIVO = "meus_desejos.txt"
desejos = [] 

try:

    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            desejos.append(linha.strip())
        print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'!\n") 
except FileNotFoundError:
        print("Parece que sua primeira vez! Vamos criar uma lista de desejos.\n")
except Exception as e:
        print(f"Ocorreu um erro ao carregar os desejos: {e}")
def salvar_desejos(listas_de_desejos):
    try:
        with open(NOME_ARQUIVO , 'w', encoding='utf-8') as arquivos:
            for desejos in listas_de_desejos:
                arquivo.write(desejos + "\n")
        print("\n Seus desejos foram salvos com sucesso!")  
    except Exception as e:
        print(f"\n Erro ao salvar os desejos: {e}")
while true:
        print("\n---O que você quer fazer?---")
        print("1- Adicionar um novo desejo")
        print("2- Ver meus desejos")
        print("3- Sair")

        opcao = input("Digite sua opção (1, 2 ou 3): ")
        if opcao =="1":
            novo_desejo = input("Qual é o seu novo desejo para o futuro?")
            if novo_desejo.dtrip():
                desejos.append(novo_desejo.strip())
                salvar_desejos(desejo)
            else:
                print("Desejos não pode ser vazio!v tente novamente.")
        elif opcao == "2":
            print("\n Seus Desejos para o Futuro")
            if not desejos:
                print("Ainda não há desejos na sua lista. Que tal adicionar um?")
            else:
                for i, desejo in enumerate(desejos):
                    print("-------------------------")
        elif opcao == "3"
            print("Até a proxima! Continue sonhando alto!")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2 ou 3.")
