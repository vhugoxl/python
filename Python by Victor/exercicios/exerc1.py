co = float(input("Digite o valor da base do catetto oposto: ").replace(",","."))
ca = float(input("Digite o valor do cateto adjacente: ").replace(",","."))

r = (ca*co)/2


print("\n**************************\n")

print(f"O valor da base de um triângulo retângulo é: {r:.2f}m²")