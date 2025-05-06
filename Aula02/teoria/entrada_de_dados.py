nome = input("Digite o seu nome: ")
#input mostra que eu preciso de uma entrada no terminal
idade = input("Digite sua idade: ")
idade_int = int(idade)
#o + fora da string está fazendo a concatenação
print("Olá, " + nome + "!")
print("Daqui a 5 anos você terá", idade_int + 5, "anos.")