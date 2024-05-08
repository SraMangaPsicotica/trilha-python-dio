import textwrap

def menu():
  menu = """
  [1] Depositar

  [2] Sacar

  [3] Extrato

  [4] Nova Conta

  [5] Novo Usuário

  [6] Sair
  => """

  return input(menu)

def depositar(valor, saldo, extrato, /):
  if valor > 0:
    saldo += valor
    extrato += f'Depósito de R${valor:.2f}\n'
    print('=== Depósito efetuado ===')
  else:
    print('@@@ Depósito indeferido @@@')

  return saldo, extrato


def sacar(*, saldo, valor, extrato, numero_saques, limite, limite_saques,):
  
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= limite_saques

  if excedeu_saldo:
    print('@@@ Saldo insuficiente @@@')

  elif excedeu_limite:
    print('@@@ Seu limite não permite este saque @@@')

  elif excedeu_saques:
    print('@@@ Limite de saques diários excedido @@@')

  elif valor > 0:
    saldo -= valor
    extrato += f'Saque de R${valor:.2f}\n'
    numero_saques += 1
    print('\n=== Saque efetuado ===')

  else:
    print('@@@ Saque indeferido @@@')

  return saldo, extrato
    

def mostrar_extrato(saldo, /, *, extrato):
  print('\n========= EXTRATO ==========')
  print('Não foram realizadas movimentações') if not extrato else print(extrato)
  print(f'\nSaldo: \t\tR${saldo:.2f}')
  print('============================')


def criar_usuario(usuarios):
  cpf = input('Informe o CPF (Apenas números): ')

  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print('@@@ CPF já cadastrado @@@')
    return

  nome = input('Informe o nome completo: ')
  data_nasc = input('Informe a data de nascimento (DD/MM/AAAA): ')
  endereco = input('Informe o endereço (Logradouro nro, Bairro, Cidade, UF): ')

  usuarios.append({'cpf': cpf, 'nome': nome, 'data_nasc': data_nasc, 'endereco': endereco,})

  print('=== Usuário cadastrado com sucesso ===')


def filtrar_usuario(cpf, usuarios):
  usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
  return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
  cpf = input('Digite o CPF de um usuário existente: ')
  usuario = filtrar_usuario(cpf, usuarios)


  if usuario:
    print('=== Conta criada com sucesso ===')
    return {'Agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

  print('\n@@@ Usuário não encontrado @@@')


def listar_contas(contas):
  for conta in contas:
    linha = f"""\ 
    Agência: \t{conta['agencia']}
    C/C: \t\t{conta['numero_conta']}
    Titular: \t{conta['usuario']['nome']}
    """
    print('='*20)
    print(textwrap.dedent(linha))
def main():
  LIMITE_DE_SAQUES = 3
  AGENCIA = '0001'

  saldo = 0
  limite = 500
  numero_saques = 0
  extrato = ''

  usuarios = []
  contas = []
  while True:
    opcao = menu()
  
    if opcao == '1':
      valor = float(input('Informe o valor à ser depositado:'))
  
      saldo, extrato = depositar(valor, saldo, extrato)
  
    elif opcao == '2':
      valor = float(input('Informe o valor à ser sacado:'))
  
      saldo, extrato = sacar(
        valor = valor,
        saldo = saldo,
        extrato = extrato,
        limite = limite,
        numero_saques = numero_saques,
        limite_saques = LIMITE_DE_SAQUES
      )
    
    elif opcao == '3':
      mostrar_extrato(saldo, extrato = extrato)


    elif opcao == '4':
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
        contas.append(conta)
        

    elif opcao == '5':
      criar_usuario(usuarios)

    elif opcao == '6':
      listar_contas(contas)

    elif opcao == '7':
      print('=== Atendimento encerrado ===')
      break


main()