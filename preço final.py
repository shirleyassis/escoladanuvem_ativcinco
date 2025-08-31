def calcular_desconto():
    """
    Programa que calcula o preço final de um produto após aplicar desconto.
    """
    print("=" * 50)
    print("CALCULADORA DE DESCONTO")
    print("=" * 50)
    
    try:
        # Solicita os dados do usuário
        preco_original = float(input("Digite o preço original do produto: R$ "))
        percentual_desconto = float(input("Digite o percentual de desconto (%): "))
        
        # Verifica se os valores são válidos
        if preco_original <= 0:
            print("❌ O preço do produto deve ser maior que zero.")
            return
        
        if percentual_desconto < 0 or percentual_desconto > 100:
            print("❌ O percentual de desconto deve estar entre 0 e 100.")
            return
        
        # Calcula o valor do desconto e o preço final
        valor_desconto = preco_original * (percentual_desconto / 100)
        preco_final = preco_original - valor_desconto
        
        # Exibe os resultados
        print("\n" + "=" * 50)
        print("RESULTADO DO CÁLCULO")
        print("=" * 50)
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto: {percentual_desconto:.1f}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
        print("=" * 50)
        
    except ValueError:
        print("❌ Erro: Digite valores numéricos válidos.")

# Executa o programa
if __name__ == "__main__":
    calcular_desconto()