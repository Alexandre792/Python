quantidade = int(input(f"digite a quantidade de notas: "))

soma_notas = 0

for i in range(quantidade):
   
    nota = float(input(f"digite a nota {i+1}: "))

    soma_notas += nota

media = soma_notas / quantidade

print(f"sua média é:{media:.2f}")

if media  >=7:
    print(f"aprovado")
else:
    print(f"reprovado")


