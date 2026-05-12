# 🤖 YLLWSMKs BOT (Python)
Este é um projeto inicial de bot para Discord desenvolvido em Python. O objetivo deste repositório é servir como base sólida para a criação de bots mais complexos, focando em boas práticas de programação, segurança de dados sensíveis e modularidade.</br>

# ⚠️ Pré-requisito Obrigatório — Discord Developer Portal
Antes de qualquer coisa, você precisará criar o seu próprio bot no Discord Developer Portal. O token gerado lá é obrigatório para rodar o projeto — cada pessoa precisa do seu próprio token e do seu próprio bot cadastrado no Discord.</br>
Passo a passo:</br>

Acesse discord.com/developers/applications</br>
Clique em New Application e dê um nome ao seu bot</br>

No menu lateral, clique em Bot</br>
Clique em Reset Token e copie o token gerado — guarde-o, ele não será exibido novamente</br>
Ainda na página Bot, role até Privileged Gateway Intents e ative os três toggles:</br>

- [x] Presence Intent</br>
- [x] Server Members Intent</br>
- [x] Message Content Intent</br>



Clique em Save Changes</br>
Para convidar o bot ao seu servidor, vá em OAuth2 → URL Generator, marque o scope bot, selecione as permissões necessárias e acesse a URL gerada</br>


O token gerado é a "senha" do seu bot. Nunca o compartilhe nem suba para o GitHub — é por isso que usamos o arquivo .env.</br>


## 🚀 Funcionalidades Atuais
O bot utiliza o prefixo ! para comandos:</br>
### Geral

!ping — Responde com o tempo de latência do bot em milissegundos.</br>
!ola — Uma resposta personalizada e amigável (ou nem tanto 💀) para o usuário.</br>
!help — Exibe o menu de comandos disponíveis.</br>

### Sistema de XP

!xp [@usuário] — Exibe o nível atual, XP total e barra de progresso para o próximo nível. Pode ser usado sem mencionar ninguém (mostra o seu próprio) ou mencionando outro membro.</br>
!rank — Exibe o Top 10 de membros mais ativos do servidor, ordenados por XP.</br>


## ⚙️ Como o Sistema de XP Funciona

Cada mensagem enviada no servidor concede entre 15 e 25 XP de forma aleatória.</br>
Há um cooldown de 60 segundos por usuário para evitar farm de XP por spam.</br>
A fórmula de nível é progressiva — fica cada vez mais difícil subir: XP necessário = 5 × (nível²) + 50 × nível + 100</br>
Ao subir de nível, o bot anuncia automaticamente no canal com um embed comemorativo.</br>
Os dados são armazenados localmente em um banco SQLite (database.db), separado por servidor.</br>


## 🛠️ Tecnologias e Bibliotecas
1. discord.py</br>
Biblioteca fundamental que permite a comunicação entre o script Python e a API do Discord. Lida com eventos e execução de comandos.</br>
2. python-dotenv</br>
Permite que o bot leia variáveis do arquivo .env, mantendo o token fora do código-fonte e protegido de exposição acidental no GitHub.</br>
3. sqlite3</br>
Biblioteca nativa do Python para gerenciar o banco de dados local. Armazena XP, nível e progresso de cada usuário por servidor, sem necessidade de instalar um banco externo.</br>

## 📁 Estrutura do Projeto
YLLWSMKs-BOT/
├── bot.py          # Arquivo principal — inicializa o bot e carrega os módulos</br>
├── database.db     # Banco de dados SQLite (gerado automaticamente)</br>
├── .env            # Token do bot (não versionar)</br>
├── .gitignore      # Arquivos ignorados pelo Git</br>
└── cogs/</br>
&nbsp;&nbsp;&nbsp;├── help.py     # Comando !help</br>
&nbsp;&nbsp;&nbsp;└── xp.py       # Sistema de XP, níveis e ranking</br>

## 📦 Como Instalar e Rodar
1. Clone o repositório</br>
git clone https://github.com/DevJapalane/Fundamentos_BotPY.git</br>
cd Fundamentos_BotPY</br>
2. Configure o Ambiente Virtual (Recomendado)</br>
python -m venv venv</br>

# Windows:
.\venv\Scripts\activate

# Linux/Mac:</br>
source venv/bin/activate</br>
3. Instale as dependências</br>
pip install discord.py python-dotenv</br>
4. Configure o arquivo .env</br>
Crie um arquivo chamado .env na raiz do projeto e adicione o token gerado no Discord Developer Portal:</br>
DISCORD_TOKEN=COLE_AQUI_SEU_TOKEN</br>

Certifique-se de que .env está no .gitignore antes de qualquer commit.</br>

5. Execute o Bot</br>
python bot.py</br>

## 🛡️ Segurança (.gitignore)
Este projeto está configurado para ignorar arquivos sensíveis e temporários:</br>

.env — Protege suas credenciais.</br>
database.db — Protege os dados dos usuários.</br>
venv/ — Evita o upload desnecessário de bibliotecas do ambiente local.</br>
__pycache__/ — Arquivos de compilação do Python.</br>


## 📈 Evolução do Projeto

- [x] Sistema de XP e Níveis com ranking por servidor.
- [ ] Bot de Música com integração Lavalink.
- [ ] Integração com banco de dados PostgreSQL.


🔗 Repositório
github.com/DevJapalane/Fundamentos_BotPY</br>

Desenvolvido por: Kalane Maciel — Estudante e CLT
