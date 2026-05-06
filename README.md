# 🤖 Discord Bot Base (Python)

Este é um projeto inicial de bot para Discord desenvolvido em Python. O objetivo deste repositório é servir como base sólida para a criação de bots mais complexos, focando em boas práticas de programação, segurança de dados sensíveis e modularidade.

# 🚀 Funcionalidades Atuais
O bot utiliza o prefixo ! para comandos:

!ping: Responde com o tempo de latência do bot em milissegundos.

!ola: Uma resposta personalizada e amigável (ou nem tanto 💀) para o usuário.

# 🛠️ Tecnologias e Bibliotecas
Para rodar este projeto, as seguintes bibliotecas são essenciais:

## 1. discord.py
É a biblioteca fundamental que permite a comunicação entre o seu script Python e a API do Discord. Ela lida com os eventos (como o bot ligar) e a execução dos comandos enviados pelos usuários.

## 2. python-dotenv
Esta biblioteca é crucial para a segurança. Ela permite que o bot leia variáveis de um arquivo externo chamado .env. Isso evita que o seu DISCORD_TOKEN (sua chave secreta) seja exposto diretamente no código-fonte e enviado acidentalmente para o GitHub.


## 📦 Como Instalar e Rodar
### 1. Clone o repositório
git clone https://github.com/DevJapalane/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
### 2. Configure o Ambiente Virtual (Recomendado)
Para manter seu sistema limpo e evitar conflitos de versões:

python -m venv venv
No Windows:
.\venv\Scripts\activate

### 3. Instale as dependências
pip install discord.py python-dotenv
### 4. Configure o arquivo .env
Crie um arquivo chamado .env na raiz do projeto e adicione seu token:
DISCORD_TOKEN=COLE_AQUI_SEU_TOKEN

Nota: Certifique-se de que o arquivo .env está listado no seu .gitignore.

## 5. Execute o Bot
python main.py

# 🛡️ Segurança (.gitignore)
Este projeto está configurado para ignorar arquivos sensíveis e temporários:

.env: Protege suas credenciais.

venv/: Evita o upload desnecessário de bibliotecas do ambiente local.

__pycache__/: Arquivos de compilação do Python.

# 📈 Evolução do Projeto
Este bot é o ponto de partida para um ecossistema maior que incluirá:

[ ] Sistema de Economia e XP.
[ ] Bot de Música com integração Lavalink.
[ ] Integração com banco de dados PostgreSQL.

Desenvolvido por: Kalane Maciel, Estudante e CLT
