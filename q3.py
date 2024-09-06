import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

menorValor = 999999999999999999999999999999999999999
diaMenorValor = maiorValor = diaMaiorValor  = maiorMedia = total = contador = 0

for i in dados:
    if(i['valor'] == 0.0):
        continue
    total += i['valor']
    contador += 1
    if(i['valor'] > maiorValor):
        maiorValor = i['valor']
        diaMaiorValor = i['dia']
    if(i['valor']< menorValor):
        menorValor = i['valor']
        diaMenorValor = i['dia']


mediaMes = round(total / contador)
for j in dados:
    if(j['valor'] > mediaMes):
        maiorMedia += 1

print(f"O menor faturamento do mês foi de {round(menorValor,2)} no dia {diaMenorValor}.\n")
print(f"O maior faturamento do mês foi de {round(maiorValor,2)} no dia {diaMaiorValor}.\n")
print(f"Houveram {maiorMedia} dias com um faturamento diário superior à média mensal.\n")