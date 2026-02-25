Lista = [("Ana", 100), ("Leo", 8110), ("Dio", 5110)]

maior = Lista[0]
for i in Lista:
    if i[1] > maior[1]:
        maior = i

print(f"O maior nivel da lista é: {maior}")