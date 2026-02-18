idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("criança")
elif idade >= 12 and idade <= 17:
    print("adolescente")
elif idade > 18:
    print("adulto")