inputo = input("Digite os números que quer somar: ")
msg = inputo.split()
somatotal = 0
for i in msg:
    somatotal += int(i)

print(somatotal)