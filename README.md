# TempoÁgil

TempoÁgil é um sistema de agenda e produtividade desenvolvido em Django, com foco em organização pessoal e de equipes. O projeto possui autenticação de usuários, cadastro de tarefas, projetos, notas, calendário, tags e notificações, com interface moderna e responsiva.

## Funcionalidades

- Cadastro e autenticação de usuários (login e registro)
- Gerenciamento de tarefas
- Organização de projetos
- Criação de notas
- Visualização de calendário
- Sistema de tags
- Notificações
- Interface responsiva e moderna

## Estrutura dos Apps

- `base`: funcionalidades e utilitários comuns
- `users`: autenticação e gerenciamento de usuários
- `tasks`: gerenciamento de tarefas
- `projects`: organização de projetos
- `notes`: criação e edição de notas
- `calendar`: visualização de eventos e tarefas
- `tags`: sistema de tags para organização
- `notifications`: notificações do sistema

## Tecnologias Utilizadas

- Python 3
- Django 5
- SQLite (padrão, pode ser trocado por outro banco)
- HTML5, CSS3 (customizado e responsivo)
- JavaScript
- Font Awesome (ícones)

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd Agenda
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install django
   ```
4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
6. Acesse em [http://localhost:8000](http://localhost:8000)

## Estrutura de Pastas

```
Agenda/
├── Apps/
│   ├── base/
│   ├── users/
│   ├── tasks/
│   ├── projects/
│   ├── notes/
│   ├── calendar/
│   ├── tags/
│   └── notifications/
├── Core/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── users/
├── db.sqlite3
├── manage.py
└── README.md
```

## Licença

Este projeto está sob a licença MIT.
# Agenda