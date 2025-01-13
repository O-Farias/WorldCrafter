# WorldCrafter

🌍 **WorldCrafter** é um sistema backend inovador que permite criar mundos fictícios completos com cidades, raças e culturas únicas. Desenvolvido com Python, o WorldCrafter é uma ferramenta indispensável para quem deseja gerar universos ricos e detalhados para RPGs, histórias, ou projetos criativos.

---

## 🚀 Funcionalidades

- **Criação de Mundos**
  - Gere nomes, culturas, climas e populações automaticamente.
- **Criação de Cidades**
  - Crie cidades únicas com nomes, populações e descrições vibrantes.
- **Criação de Raças**
  - Desenvolva raças com habilidades especiais e características marcantes.
- **Geração de Universos Completos**
  - Combine mundos, cidades e raças de forma integrada com um único comando.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **SQLAlchemy** para modelagem de dados.
- **pytest** para testes automatizados.
- **Faker** para geração de dados fictícios.
- **Colorama** para uma interface colorida no terminal.

---

## 📂 Estrutura do Projeto

```
WorldCrafter/
├── app/
│   ├── __init__.py
│   ├── cli.py               # Interface de linha de comando
│   ├── database.py          # Configuração do banco de dados
│   ├── models.py            # Modelos de dados (Mundo, Cidade, Raça)
│   ├── services/            # Serviços de lógica de negócio
│   │   ├── __init__.py
│   │   ├── city_service.py  # Serviço de cidades
│   │   ├── race_service.py  # Serviço de raças
│   │   ├── world_service.py # Serviço de mundos
├── migrations/              # Migrações do banco de dados
├── tests/                   # Testes automatizados
│   ├── __init__.py
│   ├── test_city_service.py
│   ├── test_race_service.py
│   ├── test_world_service.py
├── .env                     # Variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
├── LICENSE                  # Licença do projeto
├── README.md                # Documentação
└── requirements.txt         # Dependências do projeto
```

---

## 🔧 Como Rodar o Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/SEU_USUARIO/WorldCrafter.git
cd WorldCrafter
```

### 2. Crie um Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados
Crie o banco de dados com o seguinte comando:
```bash
python -m app.database init
```

### 5. Execute a Aplicação
```bash
PYTHONPATH=. python app/cli.py
```

---

## ✅ Testes Automatizados
Garanta que tudo está funcionando como esperado:
```bash
pytest tests/
```

---

## 🌟 Exemplos de Uso

### 1. Criar um Mundo
```bash
Escolha uma opção: 1
🌍 Mundo Gerado:
Nome: Eldoria
Cultura: Uma sociedade avançada tecnologicamente, mas socialmente instável.
Clima: Tropical
População: 4.568.123
```

### 2. Criar uma Cidade
```bash
Escolha uma opção: 2
🏙️ Cidade Criada:
Nome: Newfield
População: 291.054
Descrição: Uma cidade vibrante cheia de comerciantes e exploradores.
```

### 3. Criar uma Raça
```bash
Escolha uma opção: 3
🧝 Raça Criada:
Nome: Elflings
Habilidade Especial: Velocidade sobre-humana.
Característica: Orelhas pontudas e uma afinidade com a música.
```

### 4. Criar um Universo Completo
```bash
Escolha uma opção: 4
🌀 Criando um Universo Completo...
🌍 Mundo Gerado:
...
🏙️ Cidade Criada:
...
🧝 Raça Criada:
...
```

---

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuições
Contribuições são bem-vindas! Siga os passos abaixo:

1. Fork o projeto
2. Crie sua feature branch: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'Minha nova feature'`
4. Faça o push para o branch: `git push origin minha-feature`
5. Abra um Pull Request

---

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.15-red?style=for-the-badge&logo=alchemy&logoColor=white)
![Faker](https://img.shields.io/badge/Faker-Library-green?style=for-the-badge)
