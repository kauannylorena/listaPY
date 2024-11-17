
mais_nova_nome = ""
mais_nova_idade = float('inf')  
mais_velha_nome = ""
mais_velha_idade = -1  
soma_idades = 0  

for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))

    soma_idades += idade

    if idade < mais_nova_idade:
        mais_nova_idade = idade
        mais_nova_nome = nome

    if idade > mais_velha_idade:
        mais_velha_idade = idade
        mais_velha_nome = nome

media_idades = soma_idades / 10

print(f"\nA pessoa mais nova é {mais_nova_nome}, com {mais_nova_idade} anos.")
print(f"A pessoa mais velha é {mais_velha_nome}, com {mais_velha_idade} anos.")
print(f"A média das idades é {media_idades:.2f}.")
