numero = input("Digite um número para ver a tabuada: ")
numero = int(numero)
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("--------------------------------")
print("Fim do programa")
print("--------------------------------")
