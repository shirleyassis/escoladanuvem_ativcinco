import re

def eh_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
    ignorando espaços, pontuação e diferenças entre maiúsculas e minúsculas).
    
    Parâmetros:
    texto (str): A palavra ou frase a ser verificada
    
    Retorna:
    str: "Sim" se for palíndromo, "Não" se não for
    """
    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = re.sub(r'[^a-zA-ZÀ-ÿ]', '', texto).lower()
    
    # Verifica se é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"
# Testando a função
print(eh_palindromo("radar"))          # Sim
print(eh_palindromo("ovo"))            # Sim
print(eh_palindromo("Python"))         # Não
print(eh_palindromo("A base do teto desaba"))  # Sim
print(eh_palindromo("Anotaram a data da maratona"))  # Sim
print(eh_palindromo("Hello, World!"))  # Não

#Com input

def verificar_palindromo():
    """
    Solicita uma palavra ou frase do usuário e verifica se é um palíndromo.
    """
    # Solicita input do usuário
    texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    
    # Remove espaços, pontuação, acentos e converte para minúsculas
    texto_limpo = re.sub(r'[^a-zA-Z]', '', texto).lower()
    
    # Verifica se é palíndromo
    if texto_limpo == texto_limpo[::-1]:
        print("Sim")
    else:
        print("Não")

# Executa o programa
if __name__ == "__main__":
    verificar_palindromo()