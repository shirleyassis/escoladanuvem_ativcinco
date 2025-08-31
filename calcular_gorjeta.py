def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    
    Parâmetros:
    valor_conta (float): O valor total da conta
    porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
    
    Retorna:
    float: O valor da gorjeta calculada
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta
# Exemplo 1: Gorjeta de 15% sobre R$ 100,00
gorjeta1 = calcular_gorjeta(100.00, 15)
print(f"Gorjeta: R$ {gorjeta1:.2f}")  # Resultado: R$ 15.00

# Exemplo 2: Gorjeta de 20% sobre R$ 75,50
gorjeta2 = calcular_gorjeta(75.50, 20)
print(f"Gorjeta: R$ {gorjeta2:.2f}")  # Resultado: R$ 15.10

# Exemplo 3: Gorjeta de 10% sobre R$ 45,80
gorjeta3 = calcular_gorjeta(45.80, 10)
print(f"Gorjeta: R$ {gorjeta3:.2f}")  # Resultado: R$ 4.58