from string import Template
combustiveis = {
    "Gasolina": 5.00,
    "Etanol": 3.50,
    "Gasolina Aditivada": 6.99
}
print(Template("""
    [1] $combustível1
    [2] $combustível2
    [3] $combustível3
""").substitute(combustível1=list(combustiveis.keys())[0],
                combustível2=list(combustiveis.keys())[1],
                combustível3=list(combustiveis.keys())[2]))

escolha_combustivel = int(input("Qual combustivel você irá abastecer?: "))

if escolha_combustivel not in combustiveis:
    print("Opção inválida. Escolha um número entre 1 e 3.")
    exit()
 valor_total = litros * combustiveis[list(combustiveis.keys())[escolha_combustivel -1]]

print(f"O total a pagar é de R${valor_total:.2f}.")
