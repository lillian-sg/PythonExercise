preco = 1000 #valor do produto 
desconto = 15 #valor do desconto

valor_final = preco - (preco * desconto / 100) #formula do desconto

#o f dentro do print indica uma f-string, é usada para inserir variáveis ou expressões diretamente dentro da string.
print(f"\nO preço do celular de Maria com {desconto}% de desconto é R$ {valor_final}")