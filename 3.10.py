# Intereses de una cuenta bancaria
def calcular_intereses(saldo):
    if saldo < 10000.00:
        saldo *= 1.03
    else:
        saldo *= 1.04
    return saldo

saldo_actual = float(input('Dame saldo actual: '))
saldo_final = calcular_intereses(saldo_actual)
print(f"Saldo final es {saldo_final:.2f}")
