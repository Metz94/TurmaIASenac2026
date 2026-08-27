print("=" * 50)
print("      TESTE DE RACIOCÍNIO LÓGICO")
print("=" * 50)

pontos = 0

# Pergunta 1
resposta = input("\n1) Complete a sequência: 2, 4, 6, 8, ? ")
if resposta == "10":
    pontos += 1

# Pergunta 2
resposta = input("\n2) João tem 5 maçãs e ganha mais 3. Quantas maçãs ele tem agora? ")
if resposta == "8":
    pontos += 1

# Pergunta 3
resposta = input("\n3) Quanto é 15 + 10? ")
if resposta == "25":
    pontos += 1

# Pergunta 4
resposta = input("\n4) O que pesa mais: 1 kg de ferro ou 1 kg de algodão?\nResposta: ")
if resposta.lower() in ["iguais", "são iguais", "mesmo peso"]:
    pontos += 1

# Pergunta 5
resposta = input("\n5) Quanto é 9 x 4? ")
if resposta == "36":
    pontos += 1

# Resultado