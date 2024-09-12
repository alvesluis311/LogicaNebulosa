from LogicaNebulosa import LogicaNebulosa

logica = LogicaNebulosa()

# Entrada de dados do cliente
historico = float(input("Digite o histórico de crédito (0 a 10): "))
renda = float(input("Digite a renda mensal (0 a 100000): "))
divida = float(input("Digite a dívida atual (0 a 100000): "))

# Calculando o risco
risco = logica.calcular_risco(historico, renda, divida)

print(f"O risco calculado é: {risco}")
