# CM-CLI - Contacts Manager - Command Line interface

> Sistema de gerenciamento de contatos via terminal utilizando Python + Rich.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

CM-CLI é um projeto de terminal desenvolvido para gerenciamento simples e organizado de contatos diretamente pela CLI.  
Mesmo sendo um sistema executado no terminal, a utilização da biblioteca `rich` torna toda a experiência muito mais visual, intuitiva e agradável.

O projeto foi desenvolvido com foco em:
- organização visual
- simplicidade
- persistência de dados
- experiência agradável em terminal

---

# Funcionalidades

Atualmente o sistema possui as seguintes funcionalidades:

- ➕ Adicionar contatos
- ❌ Remover contatos
- 📝 Atualizar contatos
- 📑 Ver contatos
- 🛑 Finalizar aplicação

Todos os dados são armazenados automaticamente no arquivo:
```text
saved_data.json
```
permitindo que os contatos permaneçam salvos entre sessões.

---

# Preview



```bash
👥 Gerenciar Contatos-CLI

[1] ➕ Adicionar Contato
[2] ❌ Remover Contato
[3] 📝 Atualizar Contato
[4] 📑 Ver Contatos
[5] 🛑 Finalizar
```

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/zcypis/CM-CLI
```

Entre na pasta do projeto:

```bash
cd CM-CLI
```

Criar e ativar venv (ambiente virtual)

```bash
python -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Como usar

Execute o projeto com:

```bash
python main.py
```

Cada função:
- [1] - ➕ Adicionar Contato
> Cria um contato com as informações que forem passadas: nome, telefone, email.

- [2] - ❌ Remover Contato
> Pede nome do contato e remove ele dos dados da sessão atual.

- [3] - 📝 Atualizar Contato
> Permite mudar dados de contatos já salvos.

- [4] - 📑 Ver Contatos
> Mostra uma tabela com nome, telefone e email de todos os contatos salvos.

- [5] - 🛑 Finalizar
> Salva os dados em JSON e finaliza o script.

obs: dados só são salvos em JSON apos finalizar o script pela opção 5.

---

# Tecnologias utilizadas

- Python 3.13
- re
- pathlib
- time
- typing
- Rich
- JSON

---

# Estrutura do projeto

```text
CM-CLI/
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── helpers.py
│   ├── main.py
│   ├── processors.py
│   └── validators.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── saved_data.json
```

---

# Interface

O projeto utiliza diversos recursos visuais da biblioteca `rich`, incluindo:

- tables
- panels
- cores
- emojis
- organização visual
- separação de informações

Tudo foi pensado para tornar o terminal menos poluído e mais intuitivo.

---

# Versão

```text
0.1.0-alpha
```

---

# Roadmap

Funcionalidades planejadas futuramente:

- [ ] Sistema de busca
- [ ] Sistema de favoritos
- [ ] Sistema de logs
- [ ] Sistema de backup

---

## Autor


**Guilherme Xavier**

[![GitHub](https://img.shields.io/badge/GitHub-zcypis-181717?logo=github)](https://github.com/zcypis)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Guilherme-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/guilherme-xavier-dev)
[![Email](https://img.shields.io/badge/Email-guilhermexavie3%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:guilhermexavie3@gmail.com)
