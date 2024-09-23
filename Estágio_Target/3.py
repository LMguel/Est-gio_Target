import json

# Exemplo de dados em formato JSON
faturamento_json = '''
{
    "dias": [1200.50, 1350.00, 800.00, 0, 2100.00, 3000.00, 0, 900.00, 1100.00, 2300.00, 0, 0, 1500.00]
}
'''

dados = json.loads(faturamento_json)["dias"]

# Remove os dias sem faturamento
dias_com_faturamento = [dia for dia in dados if dia > 0]

# Cálculos
menor_faturamento = min(dias_com_faturamento)
maior_faturamento = max(dias_com_faturamento)
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_media = len([dia for dia in dias_com_faturamento if dia > media_faturamento])

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
