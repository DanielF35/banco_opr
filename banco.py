menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair
"""

saldo = 1000
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    operacao = input(menu)

    if operacao.lower() in ["d", "depositar"]:
        deposito = float(input("Quantidade para depósito: "))
        if deposito > 0:
            saldo += deposito
            print(f"Depósito de R$ {deposito:.2f} realizado. Saldo atual: R$ {saldo:.2f}")
            extrato += f"Depósito de R${deposito:.2f}\n"
        else:
            print("O valor do depósito deve ser positivo.")

    elif operacao.lower() in ["s", "sacar"]:
        saque = float(input("Quantidade a sacar: "))
        
        if saque > saldo:
            print("Você não tem dinheiro suficiente.")
        
        elif saque <= 0:
            print("Valor inválido")        

        elif saque > limite:
            print("Limite de saque alcançado.")
        elif numero_saque == limite_saque:
            print("Limite diário de saques alcançado.")
        else:
            saldo -= saque
            numero_saque += 1
            print(f"Saque de R$ {saque:.2f} efetuado. Saldo atual: R$ {saldo:.2f}")
            extrato += f"Saque de R$ {saque:.2f}\n"

    elif operacao.lower() in ["e", "extrato"]:
        if extrato:
            print("Extrato:")
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Nenhuma movimentação realizada.")

    elif operacao.lower() == "q":
        break

print("Sistema encerrado.")
