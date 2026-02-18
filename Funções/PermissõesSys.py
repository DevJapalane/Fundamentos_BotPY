# Sistema de permissões

# Função tem_permissao(cargo)
# Retorne True se cargo for:

# "admin"

# "moderador"

# Caso contrário, False.
cargo = input("Digite seu cargo: ")
def permission(cargo):
    if cargo == "admin" or cargo == "moderador":
        return True
    else:
        return False
    
print(permission(cargo))