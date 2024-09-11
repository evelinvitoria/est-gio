import json

# Exemplo de estrutura JSON com dados fictícios
faturamento_mensal = json.loads("""
    [
        {"dia": 1, "valor": 1000.00},
        {"dia": 2, "valor": 500.00},
        {"dia": 3, "valor": 0.00},  # Final de semana ou feriado
        ...
    ]
""")

# Filtrar dias com faturamento
faturamentos = [dia["valor"] for dia in faturamento_mensal if dia["valor"] > 0]

# Menor e maior valor
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

# Média mensal
media_mensal = sum(faturamentos) / len(faturamentos)

# Dias com faturamento acima da média
dias_acima_da_media = [dia for dia in faturamentos if dia > media_mensal]

print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias acima da média: {len(dias_acima_da_media)}")
