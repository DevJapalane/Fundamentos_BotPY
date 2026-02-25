Lista = [("Ana", 100), ("Leo", 8110), ("Dio", 5110)]

maior = Lista[0]
for i in Lista:
    if i[1] > maior[1]:
        maior = i

print(f"O maior nivel da lista é: {maior}")

# Índice [0]: Contém o Nome (String).
# Índice [1]: Contém o Nível (Número).