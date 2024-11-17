# Laço para ler 15 números
for i in range(15):
    # Lê o número digitado pelo usuário
    numero = int(input(f"Digite o {i+1}º número: "))
    
    # Verifica se o número é par
    if numero % 2 == 0:
        print(f"O número {numero} é par.")  # Exibe o número se ele for par

