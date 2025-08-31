from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias baseada no ano de nascimento.
    
    Parâmetros:
    ano_nascimento (int): O ano de nascimento da pessoa
    
    Retorna:
    int: A idade em dias
    """
    # Obtém a data atual
    data_atual = datetime.now()
    
    # Calcula a idade em anos
    idade_anos = data_atual.year - ano_nascimento
    
    # Calcula quantos dias se passaram desde o nascimento
    # Considera que cada ano tem aproximadamente 365.25 dias (incluindo anos bissextos)
    idade_dias = int(idade_anos * 365.25)
    
    return idade_dias

# Versão com input para o usuário
def calcular_idade_interativo():
    """
    Versão interativa que solicita o ano de nascimento do usuário.
    """
    print("=" * 50)
    print("CALCULADORA DE IDADE EM DIAS")
    print("=" * 50)
    
    try:
        # Solicita o ano de nascimento
        ano_nascimento = int(input("Digite o ano de nascimento (ex: 1990): "))
        ano_atual = datetime.now().year
        
        # Validação do ano
        if ano_nascimento > ano_atual:
            print("Erro: O ano de nascimento não pode ser maior que o ano atual.")
            return
        
        if ano_nascimento < 1900:
            print("Erro: Por favor, digite um ano válido (a partir de 1900).")
            return
        
        # Calcula a idade em dias
        idade_dias = calcular_idade_em_dias(ano_nascimento)
        
        # Exibe o resultado
        print(f"\nAno de nascimento: {ano_nascimento}")
        print(f"Ano atual: {ano_atual}")
        print(f"Idade aproximada em dias: {idade_dias} dias")
        

