import os
import time
from datetime import datetime

def Alimentacao():
    os.system("cls")

    AlimentacaoVal = float(input("Digite o valor alimentado: "))
    
    data_atual = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    print("O Valor de R$ {} foi cadastrado com sucesso!\n".format(AlimentacaoVal))

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'ValorMaq.txt')

    dado1 = "\n" + str(data_atual) + "\n" + str(AlimentacaoVal)
    arquivoEscrita = open(filename, 'a')
    arquivoEscrita.write(dado1)
    arquivoEscrita.close()

    time.sleep(3)   

def Sangria():
    os.system("cls")

    SanVal = float(input("Digite o valor retirado: "))
    
    data_atual = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    print("O Valor de R$ {} foi cadastrado com sucesso!\n".format(SanVal))

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SanVal.txt')

    dado2 = "\n" + str(data_atual) + "\n" + str(SanVal)
    arquivoEscrita = open(filename, 'a')
    arquivoEscrita.write(dado2)
    arquivoEscrita.close()

    time.sleep(3) 

def Relatorio():
    print("==Relatório Alimentação==")

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'ValorMaq.txt')
    arquivo = open(filename, 'r')
    RelMaq = arquivo.read()
    print("Quantidade Alimentada: "+RelMaq)
    arquivo.close()

    print("==Relatório Sangria==")

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'SanVal.txt')
    arquivo = open(filename, 'r')
    RelSan = arquivo.read()
    print("Quantidade Retirada: "+RelSan)
    arquivo.close()

    time.sleep(10)

def Principal():
    ##lista = carregar_cliente() # inicializa a lista de clientes
    while True:
        time.sleep(2)
        os.system("cls")
        print("===Banco Digital===")
        print("1 - Alimentação")
        print("2 - Sangria")
        print("3 - Emissão de Relatório")
        print("4 - Sair do sistema Banco")
        opcao = int(input("Digite o opção desejada:"))

        if opcao == 1:
           Alimentacao()

        elif opcao == 2:
            Sangria()

        elif opcao == 3:
            Relatorio()

        elif opcao == 4:
            print("Saindo do programa...")
            time.sleep(2)
            os.system("cls")
            break
        else:
            print("Opcão incorreta, por favor digite novamente...")
            time.sleep(2)
            os.system("cls")

Principal()