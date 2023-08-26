def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print(f"Saldo apos o deposito, {saldo}")

def depositar(valor):
    saldo = 500
    saldo += valor
    print(f"Depositado o valor de {valor}, seu saldo agora é de {saldo}")

sacar(100)
depositar(200)