
menor_numero = float('inf')  
numero = [1,2,3,4,5,6,7,8,9,0]

for i in range(10):
    
    numero[i] = int(input("Digite o número: "))
    
    if numero[i] < menor_numero:
        menor_numero = numero[i]  


print(f"O menor número digitado foi: {menor_numero}")
