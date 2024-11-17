
salario_minimo = 850

contador = 0


for i in range(5):
    salario = float(input(f"Digite o salário da {i+1}ª pessoa: R$ "))
    
    if salario < salario_minimo:
        contador += 1 

print(f"\n{contador} pessoa(s) recebem menos que 1 salário mínimo.")
