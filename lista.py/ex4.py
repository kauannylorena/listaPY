# méda aritmética de uma lista com 10 números
numeros = [12, 18, 24, 30, 40, 50, 60, 70, 80, 90]

soma = 0

for num in numeros:
    soma += num  

# Calculando a média
media = soma / len(numeros) 

print("A média aritmética é:", media)
