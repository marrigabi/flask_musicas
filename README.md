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

##  Como Executar

### 1. Instalar dependência

``
pip install flask
``
### 2. Executar o app
``
python app.py
``
### 3. Acessar app

Acesse em: http://localhost:5000
