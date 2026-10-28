TIPOS = ("carro", "moto")
VAGAS = {"carro": 5, "moto": 3}
PRECO_HORA = {"carro": 6.00, "moto": 3.50}
MENSALISTAS = {"ABC1D23", "MOT0R99"}
patio = [
 {"placa": "QWE4R56", "tipo": "carro", "entrada": 8},
 {"placa": "MOT0R99", "tipo": "moto", "entrada": 9},
 {"placa": "ZXC7V89", "tipo": "carro", "entrada": 10},
]


saida_relatorio = 0
saida_mensalista = 0
faturamento_do_dia = 0
maior_valor_cobrado = 0

def listar():
    '''Mostra os veículos estacionados, com placa, tipo e hora de entrada.'''
    
    
    for vc in patio:
        veiculos = f"{vc['placa']:<10} | {vc['tipo']:<15} | Hora da entrada: {vc['entrada']:<30}"
        print(veiculos)       



def cadastrar_entrada():
    '''Registra a chegada de um veículo: placa, tipo e hora de entrada.'''
    
    while True:
        try:
            placa = input("Placa: ").upper()
            if not placa:
                print("A placa não pode estar em branco")
            else:
                break
        except Exception:
            print(f"\nOcorreu um erro inesperado")


    for vc in patio:
        if vc['placa'] == placa:
            print("Este veiculo já está estacionado")
            return

        
    tipo = input("Tipo: ").lower()

    
    mapa_tipos = {
            "carro": "carro",
            "moto": "moto",
        }
        
        
    if tipo == 'carro' and VAGAS['carro'] == 0:
        print("Sem vagas para carros")
        return
    if tipo == 'moto' and VAGAS['moto'] == 0:
            print("Sem vagas para moto")
            return  
      
    
    if tipo not in mapa_tipos:
        print("\n Erro: Tipo inválido! Deve ser um carro ou uma moto.")
        return


    hora_entrada = int(input("Hora da entrada: "))

    
    if tipo == 'carro':
        VAGAS['carro'] -=1
    if tipo == 'moto':
        VAGAS['moto'] -=1


    novo = {"placa": placa,"tipo": tipo,"entrada": hora_entrada}


    patio.append(novo)



def saida():
    """Pede a hora de saída, calcula o valor, mostra ao cliente e tira o veículo do pátio."""

    while True:
            try:
                placa_remover = input("Placa do veiculo que está saindo: ").upper()
                if not placa_remover:
                    print("A placa não pode estar em branco")
                else:
                    break
            except Exception:
                print(f"\nOcorreu um erro inesperado")

    
    veiculo_encontrado = None


    for vc in patio:
        if vc["placa"] == placa_remover:
            veiculo_encontrado = vc
            break


    if not veiculo_encontrado:
        print("\nErro: Veículo não encontrado no pátio!")
        return

            
    while True:
        try:
            hora_saida = float(input("Hora de saida: ")) 
            if hora_saida <0 or hora_saida >23:
                print("Hora invalida, digite novamente")
            else:
                break
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

    
    horas_estacionado = hora_saida - veiculo_encontrado["entrada"]


    if horas_estacionado <=1:
        horas_estacionado =1


    tipo_veiculo = veiculo_encontrado["tipo"]

    
    if placa_remover in MENSALISTAS:
        valor_pago = 0.0
        status_mensalista = 'SIM'
        print('\n"Cliente mensalista"')
    else:
        valor_pago = horas_estacionado * PRECO_HORA[tipo_veiculo]
        status_mensalista = 'NÃO'


    print(f"\nTempo total: {horas_estacionado}h")
    print(f"Valor a pagar: R$ {valor_pago:.2f}")

        
    patio.remove(veiculo_encontrado)


    VAGAS[tipo_veiculo] +=1


    incremento_relatorio(status_mensalista,valor_pago)



def consultar():
    '''Mostra os dados de um veículo do pátio a partir da placa e diz se é mensalista.'''

    buscar_placa = input("Consultar Placa: ").upper()


    veiculo_encontrado = None


    for vc in patio:
        if vc["placa"] == buscar_placa:
            veiculo_encontrado = vc
            break


    if veiculo_encontrado:
        if buscar_placa in MENSALISTAS:
            status_mensalista = "SIM"
        else:
            status_mensalista = "NÃO"

        print(f"Placa: {veiculo_encontrado['placa']}\nTipo: {veiculo_encontrado['tipo']}\nHora entrada: {veiculo_encontrado['entrada']}\nMensalista: {status_mensalista}")
    else:
        print(f"O veiculo com a placa {buscar_placa} não está no patio")       



def vagas():
    '''Mostra quantas vagas livres há para carros e para motos.'''

    print(f"\n{VAGAS['carro']} vagas livres para carros\n{VAGAS['moto']} vagas livres para motos.")
    



def incremento_relatorio(status_mensalista, valor_pago):
    global saida_relatorio,saida_mensalista, faturamento_do_dia, maior_valor_cobrado #global é para a função alterar uma variavel externa a função, variavel global
    saida_relatorio +=1
    if status_mensalista == 'SIM':
        saida_mensalista +=1


    faturamento_do_dia += valor_pago


    if maior_valor_cobrado < valor_pago:
        maior_valor_cobrado = valor_pago



def exibir_relatorio():
    '''Mostra quantos veículos estão no pátio, quantas saídas houve, quantas 
foram de mensalistas, o faturamento do dia e o maior valor cobrado.
'''
    print(f"Hoje teve um total de {saida_relatorio} saidas no patio, destes {saida_mensalista} eram mensalistas.")
    print(f"O faturamento do dia foi de R${faturamento_do_dia:.2f}")
    print(f"O maior alor cobrado foi de R${maior_valor_cobrado:.2f}")



def cancelamento():
    """Tira do pátio uma entrada registrada por engano, sem cobrar nada."""

    while True:
            try:
                placa_remover = input("Placa do veiculo que está sendo cancelado: ").upper()
                if not placa_remover:
                    print("A placa não pode estar em branco")
                else:
                    break
            except Exception:
                print(f"\nOcorreu um erro inesperado")

    
    veiculo_encontrado = None


    for vc in patio:
        if vc["placa"] == placa_remover:
            veiculo_encontrado = vc
            patio.remove(veiculo_encontrado)
            print(f"Foi cancelado o estacionamento do veiculo placa {placa_remover}")
            VAGAS[veiculo_encontrado["tipo"]] += 1
            break


    if not veiculo_encontrado:
        print("\nErro: Veículo não encontrado no pátio!")
        return



def cadastrar_mensalista():
    '''Cadastra um novo mensalista'''
    print("\nAdicionar Mensalista\n")
    while True:
            try:
                placa = input("Placa: ").upper()
                if not placa:
                    print("A placa não pode estar em branco")
                elif placa in MENSALISTAS:
                    print("Esta placa já foi cadastrada como mensalista")
                    return
                else:
                    MENSALISTAS.add(placa)
                    print(f"A placa {placa} foi cadastrada como mensalista")
                    break
            except Exception:
                print(f"\nOcorreu um erro inesperado")


def remover_mensalista():
    while True:
        try:
            placa_remover = input("Placa do mensalista a ser removido: ").upper()
            if not placa_remover:
                print("A placa não pode estar em branco")
            elif placa_remover not in MENSALISTAS:
                print("Está placa não está cadastrada como mensalista")
                return
            else:
                MENSALISTAS.remove(placa_remover)
                print(f"A placa {placa_remover} foi removida com sucesso")
                break
        except Exception:
            print(f"\nOcorreu um erro inesperado")

     
def listar_mensalista():
    for numero, placa in enumerate(MENSALISTAS, start=1): #enumerate entrega primeiro o índice e depois o item "for indice,item in ..."; start = 1 evita começar do zero
        print(f"  {numero}. Placa: {placa}")
   




while True:
    try:
        print("\n╔═════════════════════════════════════════════════╗")
        print("║                     MENU                        ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 1 - Listar Todos                                ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 2 - Cadastrar Entrada                           ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 3 - Saída                                       ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 4 - Consultar                                   ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 5 - Exibir vagas livres                         ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 6 - Relatório                                   ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 7 - Cancelamento                                ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 8 - Mensalistas - Mais opções                   ║")
        print("╠═════════════════════════════════════════════════╣")
        print("║ 0 - Sair                                        ║")
        print("╚═════════════════════════════════════════════════╝")

        
        opcao = input("Opção: ").strip()

        
        match opcao:
            case '1':
                listar()
            case '2':
                cadastrar_entrada()
            case '3':
                saida()
            case '4':
                consultar()
            case '5':
                vagas()
            case '6':
                exibir_relatorio()
            case '7':
                cancelamento()
            case '8':
                while True:
                    try:
                        print("\n╔═════════════════════════════════════════════════╗")
                        print("║ 1 - Cadastrar Mensalista                        ║")
                        print("╠═════════════════════════════════════════════════╣")
                        print("║ 2 - Remover Mensalista                          ║")
                        print("╠═════════════════════════════════════════════════╣")
                        print("║ 3 - Listar Mensalistas                          ║")
                        print("╠═════════════════════════════════════════════════╣")
                        print("║ 0 - Sair                                        ║")
                        print("╚═════════════════════════════════════════════════╝")
                        opcao = input("Opção: ").strip()


                        match opcao:
                            case '1':
                                cadastrar_mensalista()
                            case '2':
                                remover_mensalista()
                            case '3':
                                listar_mensalista()
                            case '0':
                                    print("\nEncerrando opções de mensalistas!")
                                    break
                            case _:
                                    print("\nOpção inválida! Digite um número do menu.")


                        print("\n" + "-" * 80)
                        input("Pressione ENTER para continuar...")


                    except Exception as erro:
                        print(f"\nOcorreu um erro inesperado: {erro}")


            case '0':
                print("\nEncerrando o programa. Até logo!")
                break
            case _:
                print("\nOpção inválida! Digite um número do menu.")

                
        print("\n" + "-" * 80)
        input("Pressione ENTER para continuar...")

        
    except Exception as erro:
        print(f"\nOcorreu um erro inesperado: {erro}")
