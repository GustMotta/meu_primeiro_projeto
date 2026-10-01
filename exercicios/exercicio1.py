# Exercício 1: média do aluno

# 1. As notas
nota1 = 8
nota2 = 6.5
nota3 = 7

# 2. O cálculo 
media =  (nota1 + nota2 + nota3) / 3

# 3. A decisão
if media >= 7:
   situacao = "Aprovado"
elif media >= 5:
   situacao = "Recuperação"
else:
   situacao = "Reprovado"

# 4. O resultado
print("Média:", media)
print("Situação:", situacao)
print("Fim do programa")
print("--------------------------------")
