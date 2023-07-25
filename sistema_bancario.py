operacoes = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(operacoes)

    if opcao == "d":
        print("Depósito")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        if valor_deposito <= 0:
            print("O valor depositado não pode ser negativo ou igual a 0")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: +{valor_deposito}\n"

    elif opcao =="s":
        print("Saque")
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if numero_saques == LIMITE_SAQUES:
            print("O limite de saques foi atingido.")
        elif saldo == 0:
            print("Não há nenhum valor disponível para saque.")
        elif valor_saque > limite:
            print("Não é possível realizar o saque, pois o valor extrapola o limite.")
        elif valor_saque < 0:
            print("Não é possível sacar valores negativos.")
        else:
            numero_saques += 1
            saldo -= valor_saque
            extrato += f"Saque: -{valor_saque}\n"

    elif opcao == "e":
        if extrato == "":
            print("Não há movimentação na conta.")
        else:
            print(extrato + "O seu saldo final é de : " + str(saldo))

    elif opcao == "q":
        break

    else:
        print("Operação inválida")