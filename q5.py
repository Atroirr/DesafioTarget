entrada = input("Digite a string a ser invertida: \n")

novaString = ""

# Itera sobre a string de trás para frente
for i in range(len(entrada)):
    novaString += entrada[-(i + 1)]

print(novaString)