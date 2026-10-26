import json
TIPOS = ('notebook', 'tablet', 'kit arduino', 'fone')

equipamentos = [
    {'codigo': '', 'tipo': 'notebook', 'disponivel': True, 'com': '', 'emprestimos': 0},
    {'codigo': '', 'tipo': 'notebook', 'disponivel': True, 'com': '', 'emprestimos': 0},
    {'codigo': '', 'tipo': 'tablet', 'disponivel': True, 'com': '', 'emprestimos': 0},
    {'codigo': '', 'tipo': 'kit arduino', 'disponivel': True, 'com': '', 'emprestimos': 0},
    {'codigo': '', 'tipo': 'fone', 'disponivel': True, 'com': '', 'emprestimos': 0},
]

ARQUIVO_JSON = "equipamentos.json"

def carregar_dados():
    """Carrega os dados do arquivo JSON se ele existir, senão usa a lista padrão."""
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arq: #with fecha o arquivo após a leitura para evitar memory leak, r é read, utf-8 codificação do nosso idioma para entender ç e acentos
            return json.load(arq) #load carrega os dados do arquivo, pull
    except FileNotFoundError:
        return equipamentos #se não encontrar o arquivo, carrega a template padrão

def salvar_dados():
    """Salva a lista atual de equipamentos no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arq: #w de write
        json.dump(equipamentos, arq, indent=4, ensure_ascii=False) #dump envia os dados para o arquivo, push. Ascii false porque usamos utf-8

# Inicializa os equipamentos carregando do arquivo
equipamentos = carregar_dados()

def listar():
    '''Lista todos os equipamentos cadastrados, em formato de tabela'''
    print(f"\n{ '--- LISTA DE EQUIPAMENTOS ---':^80}\n") # ^ centraliza num espaço de 80
    cabecalho = f"{ 'CÓDIGO':<10} | { 'TIPO':<15} | { 'STATUS':<30}"
    print(cabecalho.center(80))
    print(f"{'-' * 80}".center(80))
    
    for eq in equipamentos:
        status = "Disponível" if eq['disponivel'] else f"Emprestado para ({eq['com']})"
        linha = f"{eq['codigo']:<10} | {eq['tipo']:<15} | {status:<30}"
        print(linha.center(80))



def cadastrar():
    '''Cadastra um novo equipamento verificando o prefixo (Atualiza o JSON)'''
    print(f"\n{ '--- CADASTRAR EQUIPAMENTO ---' :^80}\n")
    print("┌────────────────────────────────────────┐")
    print("│ Prefixos obrigatórios para os códigos: │")
    print("│ • NB - Notebook   • TB - Tablet        │")
    print("│ • AR - Kit Arduino • FN - Fone         │")
    print("└────────────────────────────────────────┘")
    
    codigo = input("Digite o código do equipamento: ").strip().upper()
    
    for eq in equipamentos:
        if eq.get("codigo") == codigo:#get pega o valor de uma chave dentro de uma lsita, se não existir retorna none, sem dar erro no programa
            print("\n Erro: Já existe um equipamento com este código!")
            return
            
    mapa_tipos = {
        "NB": "notebook",
        "TB": "tablet",
        "AR": "kit arduino",
        "FN": "fone"
    }
    
    prefixo = codigo[:2] #:2 pega apenas os dois primeiros itens 0 e 1.
    
    if prefixo not in mapa_tipos:
        print("\n Erro: Código inválido! O código deve começar com NB, TB, AR ou FN.")
        return
        
    tipo = mapa_tipos[prefixo]
    
    novo = {
        "codigo": codigo,
        "tipo": tipo,
        "disponivel": True,
        "com": "",
        "emprestimos": 0
    }
    
    equipamentos.append(novo)
    salvar_dados()
    print(f"\n Equipamento {codigo} ({tipo.upper()}) cadastrado com sucesso!")



def emprestar():
    '''Registra o emprestimo de um quipamento disponivel para uma pessoa gravando seu nome (Atualiza o JSON)'''
    print(f"\n{ '--- EMPRESTAR EQUIPAMENTO ---' :^80}\n")
    codigo = input("Digite o código do equipamento que deseja emprestar:").strip().upper()

    for eq in equipamentos:
        if eq['codigo'] == codigo:
            if not eq['disponivel']:
                print(f"\nErro: Este equipamento já está emprestado para {eq['com']}.")
                return

            nome = input("Digite o nome de quem está pegando o empréstimo: ")
            if not nome:
                print("\nErro: o nome não pode ser vazio!")
                return

            eq['disponivel'] = False
            eq['com'] = nome
            eq['emprestimos'] += 1
            salvar_dados()
            print(f"\nSucesso! {codigo} emprestado para {nome}.")
            return



def devolver():
    '''Registra a devolução de um equipamento que estava emprestado (Atualiza o JSON)'''
    print(f"\n{ '--- DEVOLVER EQUIPAMENTO ---' :^80}\n")
    codigo = input("Digite o código do equipamento que deseja devolver:").strip().upper()

    for eq in equipamentos:
        if eq['codigo'] == codigo:
            if eq['disponivel']:
                print(f"\nErro: Este equipamento não está emprestado")
                return

            eq['disponivel'] = True
            eq['com'] = ""
            eq['emprestimos'] -= 1
            salvar_dados()
            print(f"\nSucesso! {codigo} devolvido")
            return



def consultar():
    '''Busca um equyipamento pelo seu codigo e mostra seu tipo e status'''
    print(f"\n{ '--- CONSULTAR EQUIPAMENTO ---' :^80}\n")
    codigo = input("Digite o código do equipamento que deseja consultar:").strip().upper()

    for eq in equipamentos:
        if eq['codigo'] == codigo:

            print(eq['tipo'])
            if (eq['disponivel']) == True:
                print("Disponivel")
            else:
                print(f"Equipamento emprestado para {(eq['com'])}")



def relatorio():
    '''Mostra o historico de quantas vezers um equipamento especifico foi emprestado'''
    print(f"\n{ '--- RELATÓRIO DE USO ---' :^80}\n")
    codigo = input("Digite o código do equipamento que deseja consultar o relatório de uso: ").strip().upper()

    for eq in equipamentos:
        if eq['codigo'] == codigo:
            print(f"O equipamento foi emprestado {eq['emprestimos']} vezes")


def remover():
    '''Exclui um equipamento do sistema somente se ele não estiver emrpestado (Atualiza o JSON)'''
    print(f"\n{ '--- REMOVER EQUIPAMENTO ---' :^80}\n")

    codigo_remover = input ("Informe o código do equipamento a ser removido: ").strip().upper()

    for eq in equipamentos:
        if (eq['codigo']) == codigo_remover:
            if not (eq['disponivel']):
                print("Equipamento atualmente emprestado, não é possivel remover.")
                return

    
            equipamentos.remove(eq)
            salvar_dados()
            print(f"O equipamento {codigo_remover} foi removido com sucesso")
            return
    print("Equipamento não encontrado")


    
while True:
    try:
        print("\n╔═════════════════════════════════════════════════╗")
        print("║                     MENU                        ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 1 - Listar Todos                                ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 2 - Cadastrar Novo                              ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 3 - Registrar Empréstimo                        ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 4 - Devolver Empréstimo                         ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 5 - Consultar por Código                        ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 6 - Relatório de Uso                            ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 7 - Remover Equipamento                         ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 0 - Sair                                        ║")
        print("╚═════════════════════════════════════════════════╝")
        
        opcao = input("Opção: ").strip()
        
        match opcao:
            case '1':
                listar()
            case '2':
                cadastrar()
            case '3':
                emprestar()
            case '4':
                devolver()
            case '5':
                consultar()
            case '6':
                relatorio()
            case '7':
                remover()
            case '0':
                print("\nEncerrando o programa. Até logo!")
                break
            case _:
                print("\nOpção inválida! Digite um número do menu.")
                
        print("\n" + "-" * 80)
        input("Pressione ENTER para continuar...")
        
    except Exception as erro:
        print(f"\nOcorreu um erro inesperado: {erro}")
