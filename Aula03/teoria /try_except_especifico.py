"""
Preciso instanciar um numerador, um denominador e ro resultado dessa divisão 

Erros:
Se não for valor escreva(Insira apenas números)

Se o denominador for 0, escreva um erro que não é possível dividir por zero

"""
try:
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    resultado = numerador / denominador
    print(f"O resultado é {resultado}")
except ValueError:
    #Erro de tipo
    print("Insira apenas números")
except ZeroDivisionError:
    # Erro de divisão por zero
    print("Não é possível dividir por zero.")