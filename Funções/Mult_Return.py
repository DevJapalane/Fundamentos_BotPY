# Função analisar_mensagem(msg) que retorne:

# quantidade de caracteres

# quantidade de palavras

# se contém link (True/False)

# def analisar_mensagem(msg):
#     print msg.len

def analisar_mensagem(msg):
    qtd_char = len(msg)
    qtd_wrds = len(msg.split) # .split faz todos espaço na frase virar uma virgula para a lista python, sendo assim 2 palavras separadas por um espaço vira dois itens na lista
    haslink = "https" in msg

    print(f"a mensagem cont~em {qtd_char} caracteres.")