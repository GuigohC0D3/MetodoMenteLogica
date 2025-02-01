# Passo 1: Criar uma função para calcular a média
def calcular_media(numeros):
    # Passo 2: Verificar se a lista está vazia
    if len(numeros) == 0:
        return 0  # Retorna 0 para evitar erro de divisão por zero
    
    # Passo 3: Somar todos os números da lista
    soma = 0  # Começamos com soma igual a zero
    for numero in numeros:
        soma += numero  # Adicionamos cada número à soma
    
    # Passo 4: Calcular a média (soma dividida pela quantidade de números)
    media = soma / len(numeros)
    
    # Passo 5: Retornar o resultado
    return media

# Passo 6: Criar uma lista de números
numeros = [10, 20, 30, 40, 50]

# Passo 7: Chamar a função e armazenar o resultado
resultado = calcular_media(numeros)

# Passo 8: Mostrar o resultado na tela
print(f"A média dos números é: {resultado}")
