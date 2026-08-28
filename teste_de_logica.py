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
resposta = input("\n4) O que pesa mais: 1 kg de ferro ou 1 kg de algodão? ")

if resposta.lower() in [
    "iguais",
    "são iguais",
    "mesmo peso",
    "peso igual",
    "os dois pesam igual"
]:
    pontos += 1

# Pergunta 5
resposta = input("\n5) Quanto é 9 x 4? ")
if resposta == "36":
    pontos += 1

# Resultado final
print("\n" + "=" * 50)
print("RESULTADO FINAL")
print("=" * 50)

print(f"Você acertou {pontos} de 5 questões.")

if pontos == 5:
    print("Excelente! Você acertou todas as questões!")
elif pontos >= 3:
    print("Muito bom! Você foi aprovado.")
else:
    print("Você precisa praticar mais. Continue estudando!")

print("=" * 50)