import json

def calcular_faturamento(dados):
    valores = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]

    menor_faturamento = min(valores)
    maior_faturamento = max(valores)

    media_faturamento = sum(valores) / len(valores)

    dias_acima_media = 0
    for valor in valores:
        if valor > media_faturamento:
            dias_acima_media += 1

    return menor_faturamento, maior_faturamento, dias_acima_media

with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)

menor_valor, maior_valor, dias_acima_da_media = calcular_faturamento(dados)

print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
