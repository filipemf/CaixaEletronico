import os
import time
import re

from tempfile import mkstemp
from shutil import move, copymode

print("Bem-vindo!")

class Proj:
  def init(req):

    while True:
      
      os.system("cls")

      def selecionar_todos_os_clientes():
        try:
          lista = []
          dirname = os.path.dirname(__file__)
          filename = os.path.join(dirname, 'clientes.txt')
      
          with open(filename) as arquivo:
            for linha in arquivo.readlines():  # armazena em linha a o valor da linha
              coluna = linha.split("#")  # coluna recebe agora um vetor
              cliente = {
                "email": coluna[1],
                "nome": coluna[0],
                "saldo": coluna[2]
              }
              lista.append(cliente)
              
          arquivo.close()
          return lista

        except FileNotFoundError:
          print("Arquivo não existe - Criar....")

      lista = selecionar_todos_os_clientes()

      dirname = os.path.dirname(__file__)
      filename = os.path.join(dirname, '..', 'clienteAtivo.txt')

      arquivo = open(filename, 'r')
      usuarioAtivo = arquivo.read()
      
      print("Olá, "+usuarioAtivo)
      arquivo.close()

      dados = next((item for item in lista if item['email'] == usuarioAtivo), None)
      
      print("Seus dados são: ", end='')
      print(dados)
 

      
      print("1 - Realizar saque")
      
      print("2 - Realiazar depósito")
      
      print("3 - Efeturar pagamento")

      print (" ")

      selecionado = int(input("Digite o opção desejada: "))

      if selecionado == 1:
        req.saqueCliente(dados)

      elif selecionado == 2:
        req.depositoCliente(dados)

      elif selecionado == 3:
        req.pagamentoCliente(dados)
    pass

  def saqueCliente(req, dados):
    dadosAntigos = dados['saldo']

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'dinheiroNaMaquina.txt')
    arquivo = open(filename, 'r')
    quantidadeNoCaixa = arquivo.read()
    print("Quantidade disponível no caixa: "+quantidadeNoCaixa)
    arquivo.close()

    intQuantidade = int(float(quantidadeNoCaixa))
    saldo = dados['saldo']
    
    dinheiro = int(input("Informe o quanto gostaria de sacar: "))

    if dinheiro <= int(dados['saldo']):
      if dinheiro<=int(float(quantidadeNoCaixa)):
        arquivoEscrita = open(filename, 'w')
        #arquivoEscrita.seek(0)
        quantidade = int(float(quantidadeNoCaixa))-dinheiro
        arquivoEscrita.write(str(quantidade))
        #arquivoEscrita.truncate()
        arquivoEscrita.close()
        print("Operação concluida com sucesso. Você sacou: "+"R$"+str(dinheiro))
        dados['saldo']=int(dados['saldo'])-dinheiro
      else:
        print("Quantidade não disponível. Por favor, insira manualmente mais dinheiro, ou tente novamente mais tarde")
    else:
      print("Você não possui saldo suficiente. Deposite mais para continuar.")

    

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'clientes.txt')


    
    def replace(file_path, pattern, subst):
      #Create temp file
      fh, abs_path = mkstemp()
      with os.fdopen(fh,'w') as new_file:
          with open(file_path) as old_file:
              for line in old_file:
                  new_file.write(line.replace(str(pattern), str(subst)+"\n"))
      #Copy the file permissions from the old file to the new file
      copymode(file_path, abs_path)
      #Remove original file
      os.remove(file_path)
      #Move new file
      move(abs_path, file_path)

    
    replace(filename, dadosAntigos, dados['saldo'])

    time.sleep(4)
    pass

  def depositoCliente(req, dados):
    dadosAntigos = dados['saldo']

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'dinheiroNaMaquina.txt')
    arquivo = open(filename, 'r')
    quantidadeNoCaixa = arquivo.read()
    arquivo.close()

    intQuantidade = int(float(quantidadeNoCaixa))
    saldo = dados['saldo']
    dinheiro = int(input("Informe a quantia que gostaria de depositar: "))

    arquivoEscrita = open(filename, 'w')
    #arquivoEscrita.seek(0)
    quantidade = int(float(quantidadeNoCaixa))+dinheiro
    arquivoEscrita.write(str(quantidade))
    #arquivoEscrita.truncate()
    arquivoEscrita.close()
    print("Operação concluida com sucesso. Você depositou: "+"R$"+str(dinheiro))
    dados['saldo'] = int(dados['saldo'])+dinheiro

    #teste#teste@email.com#100
    #test23e#teste23@email.com#230


    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'clientes.txt')
    
    def replace(file_path, pattern, subst):
      #Create temp file
      fh, abs_path = mkstemp()
      with os.fdopen(fh,'w') as new_file:
          with open(file_path) as old_file:
              for line in old_file:
                  new_file.write(line.replace(str(pattern), str(subst)+"\n"))
      #Copy the file permissions from the old file to the new file
      copymode(file_path, abs_path)
      #Remove original file
      os.remove(file_path)
      #Move new file
      move(abs_path, file_path)

    
    replace(filename, dadosAntigos, dados['saldo'])

    time.sleep(4)
    pass

  def pagamentoCliente(req, dados):
    quantidade = int(input("Informe o quanto será pago: "))
    novaConta =  input("Informe o email para onde o pagamento irá: ")

    dadosAGORAVAIFAMLIA = dados
    dadosUserAtivo = dados
    
    
    def selecionar_todos_os_clientes():
      try:
        lista = []
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'clientes.txt')
      
        with open(filename) as arquivo:
          for linha in arquivo.readlines():  # armazena em linha a o valor da linha
            coluna = linha.split("#")  # coluna recebe agora um vetor
            cliente = {
              "email": coluna[1],
              "nome": coluna[0],
              "saldo": coluna[2]
            }
            lista.append(cliente)
              
        arquivo.close()
        return lista

      except FileNotFoundError:
        print("Arquivo não existe - Criar....")

    lista = selecionar_todos_os_clientes()

    dados = next((item for item in lista if item['email'] == novaConta), None)
    dadosAntigosNovaConta = dados

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '..', 'clienteAtivo.txt')
    arquivo = open(filename, 'r')
    usuarioAtivo = arquivo.read()
    arquivo.close()

    dadosUserAtivo = next((item for item in lista if item['email'] == usuarioAtivo), None)
    dadosDoPassadoUserAtivo = dadosUserAtivo


    if int(dadosUserAtivo['saldo'])>=quantidade:
      dados['saldo'] = int(dados['saldo'])+quantidade
      dadosUserAtivo['saldo'] = int(dadosUserAtivo['saldo'])-quantidade

    def replace(file_path, pattern, subst):
      #Create temp file
      fh, abs_path = mkstemp()
      with os.fdopen(fh,'w') as new_file:
          with open(file_path) as old_file:
              for line in old_file:
                  new_file.write(line.replace(str(pattern), str(subst)+"\n"))
      #Copy the file permissions from the old file to the new file
      copymode(file_path, abs_path)
      #Remove original file
      os.remove(file_path)
      #Move new file
      move(abs_path, file_path)

    print("Os seus dados atualizados são: ", end='')
    print(dadosUserAtivo)


    replace(filename, dadosAGORAVAIFAMLIA['saldo'], dados['saldo'])

    replace(filename, dadosDoPassadoUserAtivo['saldo'], dadosUserAtivo['saldo'])

    
    
    time.sleep(25)
    pass
    

  


