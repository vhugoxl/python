peso = float(input("Digite o valor do seu peso: "))
altura = float(input("Digite o valor da sua altura: "))

r = (peso/altura**2)

print("\n**************************\n")

print(f"O valor do seu IMC: {r:.1f} ")