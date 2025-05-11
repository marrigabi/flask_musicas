# 🎵 MusicApp Flask - Gerenciador de Músicas com Login

## 📌 Descrição

Aplicação web feita com **Flask** que permite aos usuários autenticados **gerenciar suas músicas favoritas**. 

---

##  Funcionalidades

- ✅ Autenticação de usuários (login fictício com dados no código)
- ✅ Sessão de login com controle via `Flask.session`
- ✅ Dashboard com saudação e opções
- ✅ Gerenciamento de músicas por usuário:
  - Adicionar
  - Remover
  - Editar
  - Listar
- ✅ Logout para encerrar a sessão

---

##  Páginas

| Rota         | Descrição                            |
|--------------|--------------------------------------|
| `/`          | Página inicial (boas-vindas)         |
| `/login`     | Tela de login                        |
| `/dashboard` | Painel do usuário logado             |
| `/musicas`   | Gerenciamento de músicas favoritas   |
| `/logout`    | Finaliza a sessão e redireciona      |

---

##  Estilo e Interface

- Layout moderno com **HTML5 + CSS3**
- Responsivo e centralizado
- Cores suaves com degradê (roxo-azul)
- Botões estilizados e alertas visuais
- Formulários com UX melhorado

---

##  Estrutura de Diretórios

flask_musicas/

├── app.py

├── static/

│ └── style.css

└── templates/

├── index.html

├── login.html

├── dashboard.html

└── musicas.html


---


##  Como rodar o projeto

###  1. Clonar o repositório

``
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
``
### 2. Criar o ambiente virtual

``
python -m venv .venv
``

### 3. Ativar o ambiente virtual

``
.venv\\Scripts\\activate
``

### 4. Instalar dependências

``
pip install -r requirements.txt
``

### 5. Rodar servidor Flask

``
python app.py
``

### 6. Acessar app

Acesse em: http://localhost:5000
