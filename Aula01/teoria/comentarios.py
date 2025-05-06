#esse é um comentário em linha 

"""
Esse é um comentário de múltiplas linhas 

E é um comentário que é ultilizado para explicar o código

"""
def calcular_media(numeros):
    """ Esta é uma docstring que explica a função. 
    Calcula a média aritmética de uma lista de números
    Args: 
        numeros: Uma lista(array) de valores numericos 
    Return: (Resultado)
        A média dos valores
    """
    return sum(numeros)/len(numeros)