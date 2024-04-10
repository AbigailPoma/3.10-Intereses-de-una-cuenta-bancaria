#Intereses de una cuenta bancaria
print('Dame saldo actual:')
Saldo = float(input( ))

if (Saldo < 10000.00):
    Saldo = Saldo*(1 + 0.03)
else:
    Saldo = Saldo*(1 + 0.04)

print("Saldo final es %5.2f"%Saldo)