# 
maiores_de_idade = 0

for i in range(20):
    
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    
    if idade >= 18:
        maiores_de_idade += 1 

print(f"Quantidade de pessoas maiores de idade: {maiores_de_idade}")
