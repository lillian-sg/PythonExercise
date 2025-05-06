import unicodedata
#Quero saber se um dia é útil ou não

#meu código deu problema então estou usando um removedor de acentos.
def remover_acento(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

dia = input("Digite o dia da semana: ").lower()
dia = remover_acento(dia)
# linha de apoio pra ver o que está sendo lido
print(f"[DEBUG] Dia tratado: {dia}")

if dia == "sabado" or dia == "domingo":
    print("É fim de semana! Uhuuuuu!!")
elif dia in ["segunda", "terca", "quarta", "quinta", "sexta"]:
    print("É dia útil")
else: 
    print("Dia inválido. Tente novamente.")