def adicionar_tarefa(lista_de_tarefas, tarefa):
    '''inclui  uma nova tarefa na lista'''
    lista_de_tarefas.append(tarefa)
    print("tarefa inclusa com sucesso!")
    print("\n")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    '''Exibe a lista de tarefas'''
    print("\n")
    print("-" * 50)
    print(f"{' ' * 15}LISTA DE TAREFAS{' ' * 15}")
    print("-" * 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f"{n} - {tarefa}")
        n += 1
        print("-" * 50)
    print("\n")

def deletar_tarefa(lista_de_tarefas, tarefa):
    '''some uma tarefa selecionada'''
    lista_de_tarefas.pop((tarefa - 1))
    return lista_de_tarefas

def exibir_menu():
    '''mostra as funções da lista para escolher'''
    print("• escolha uma opção •\n"
        "1 - incluir nova tarafa\n" 
        "2 - listar\n"
        "3 - apagar tarefa\n"      
        "4 - apagar todas as tarefas\n"
        "5 - sair"
         )
    print("-" * 50)

def deletar_todas_as_tarefas(lista_de_tarefas):
    '''exclui TODAS as tarefas'''
    lista_de_tarefas.clear()
    print("Todas as tarefas foram deletadas com sucesso!")
    print("\n")
    return lista_de_tarefas
    
# Inicialização de variáveis
lista_de_tarefas = []
continuar = True

# Cabeçalho do programa
print('-' * 50)
print(f"{' ' * 10}-essa é tua lista de tarefas-{' ' * 10}")
print('-' * 50)

# Loop principal
while continuar:
    exibir_menu()
    opcao = input('=> insira o que deseja fazer: ')
    
    if opcao == "1":
        print("\n")
        tarefa = input('=> insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3":
        tarefa = input('=> insira o número da tarefa que deseja deletar: ')
        if not tarefa.isnumeric():
            print("número inválido, tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas):
            print("número inválido, tente novamente.")
        elif int(tarefa) <= 0:
            print("número inválido, tente novamente.")
        else: 
            deletar_tarefa(lista_de_tarefas, int(tarefa))
            print("tarefa deletada com sucesso!")
    elif opcao == "4":
        confirmacao = input("tu tem certeza que deseja apagar TODAS as tarefas? (s/n): ").lower()
        if confirmacao == 's':
            lista_de_tarefas = deletar_todas_as_tarefas(lista_de_tarefas)
        print('\n')
    elif opcao == "5": 
         continuar = False
    else:
         print("opção anulada! tu pode tentar de novo, amigo.")
    print("\n")