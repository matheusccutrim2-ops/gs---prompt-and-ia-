# 🚀 Mission Control AI — EnviroSat Guard

## 📚 Integrante

- **Matheus Costa Cutrim** — RM: **568087** — Turma: **[CCPR]**

**Modalidade:** Individual

---

# 🌍 O que o projeto faz

O **Mission Control AI – EnviroSat Guard** é um sistema inteligente de monitoramento de missão espacial que simula a operação de um satélite ambiental. A aplicação gera dados de telemetria, identifica anomalias por meio de regras em Python e utiliza Inteligência Artificial Generativa para produzir análises contextualizadas em linguagem natural.

A IA é integrada via **Ollama Cloud**, utilizando o modelo **gpt-oss:120b**, e recebe dinamicamente os dados da missão, os alertas gerados pelo código e a pergunta do operador.

---

# 👤 Persona atendida

A persona principal é o **Operador de Centro de Controle Ambiental**, responsável por acompanhar missões de observação da Terra e tomar decisões rápidas diante de eventos como queimadas, desmatamento, falhas de comunicação e perda de qualidade dos dados ambientais.

Essa persona precisa de respostas objetivas e acionáveis, pois atrasos na interpretação de dados orbitais podem impactar diretamente o combate a incêndios, a fiscalização ambiental e a proteção de áreas sensíveis.

---

# 🛰️ Trilha escolhida

**Trilha 2 — EnviroSat (Observação Ambiental)**

O projeto simula um satélite ambiental semelhante a sistemas de observação da Terra usados para monitoramento climático, focos de calor, áreas protegidas e possíveis eventos de desmatamento.

---

# ⚙️ Tecnologias utilizadas

- Python 3.10+
- Ollama Cloud API
- Modelo `gpt-oss:120b`
- Bibliotecas:
  - `ollama`
  - `python-dotenv`
  - `rich`
  - `prompt-toolkit`
  - `pyfiglet`

---

# 📂 Estrutura do projeto

```txt
mission-control-ai/
│
├── README.md
├── main.py
├── banner_ascii.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── ui.py
│   ├── engine.py
│   ├── telemetria.py
│   └── alertas.py
│
├── prompts/
│   └── system_prompt.md
│
├── data/
│   └── cenarios.json
│
└── assets/
    ├── screenshot_normal.png
    └── screenshot_alerta.png
```

---

# 📊 Parâmetros monitorados

O sistema monitora os seguintes dados simulados:

- Temperatura do sensor térmico;
- Energia disponível;
- Buffer de imagens;
- Sinal de comunicação;
- Precisão de geolocalização;
- Focos térmicos detectados;
- Área ambiental monitorada.

---

# 🚨 Regras de alerta

As regras são implementadas diretamente em Python no arquivo `src/alertas.py`.

O sistema identifica:

- Superaquecimento do sensor térmico;
- Energia baixa;
- Perda parcial de comunicação;
- Buffer de imagens quase cheio;
- Baixa precisão de geolocalização;
- Possível evento de incêndio;
- Cenário de multicrise.

---

# 🤖 Integração com IA

A integração com IA está centralizada no arquivo `src/engine.py`.

Fluxo da análise:

1. O operador digita uma pergunta no terminal;
2. O sistema identifica o cenário simulado;
3. A telemetria é gerada dinamicamente;
4. As regras de alerta são aplicadas em Python;
5. Os dados, alertas e ações são injetados no prompt;
6. O modelo `gpt-oss:120b` gera a análise;
7. A resposta é exibida de forma organizada no terminal.

---

# ▶️ Como executar

## 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/mission-control-ai
cd mission-control-ai
```

## 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

## 3. Ative o ambiente virtual

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

## 5. Configure a variável de ambiente

Crie um arquivo `.env` na raiz do projeto:

```txt
OLLAMA_API_KEY=sua_chave_aqui
```

## 6. Execute o sistema

```bash
python main.py
```

---

# 🧪 Comandos para demonstração

Dentro do terminal da aplicação:

```txt
/status
```

```txt
Analise a missão atual
```

```txt
Simule um incêndio crítico
```

```txt
Verifique perda de comunicação
```

```txt
Existe risco de temperatura crítica?
```

```txt
Simule multicrise
```

---


# 📝 System Prompt

O system prompt usado pela IA está localizado em:

```txt
prompts/system_prompt.md
```

Ele orienta o modelo a atuar como uma IA operacional especializada na trilha EnviroSat, conectando telemetria espacial com impacto ambiental terrestre.

---

# 🌎 Impacto terrestre

O projeto demonstra como tecnologias espaciais podem apoiar decisões reais na Terra. A análise de telemetria de um satélite ambiental pode contribuir para:

- combate mais rápido a incêndios;
- preservação de áreas protegidas;
- fiscalização ambiental;
- monitoramento de desmatamento;
- redução de danos ambientais;
- apoio a órgãos públicos e equipes de campo.

---

# 💼 Proposta de valor / modelo de negócio

O **EnviroSat Guard** poderia evoluir para uma plataforma SaaS de apoio a operações ambientais. Órgãos públicos, empresas de compliance ambiental, seguradoras, institutos de pesquisa e brigadas de incêndio poderiam utilizar a solução para receber alertas automáticos e análises inteligentes sobre riscos ambientais monitorados por satélite.

A proposta de valor está em transformar dados orbitais complexos em decisões operacionais rápidas, claras e acionáveis.

---

# 🧪 Cenários de teste demonstrados

1. Operação normal — todos os parâmetros dentro da faixa esperada.
2. Temperatura crítica — superaquecimento do sensor térmico.
3. Energia baixa — ativação de modo economia.
4. Perda de comunicação — falha parcial no downlink.
5. Incêndio — grande quantidade de focos térmicos detectados.
6. Multicrise — múltiplas anomalias simultâneas.

---

# ⚠️ Limitações conhecidas

- Os dados são simulados.
- O sistema não se conecta a satélites reais.
- A análise depende da disponibilidade da Ollama Cloud.
- Não há dashboard web.
- Não há banco de dados persistente.
- A IA não substitui especialistas humanos.
- Os prints em `assets/` devem ser substituídos por capturas reais feitas durante a execução.

---

# 🎬 Vídeo de demonstração

🔗 https://youtu.be/sObImwCZqfw?si=0VFpbppeVJgwXmux 

> Configurado como **Não listado** no YouTube.

---

# ✅ Checklist de requisitos atendidos

- ✅ Projeto Python 3.10+
- ✅ Estrutura modular organizada
- ✅ README completo
- ✅ `requirements.txt` com versões fixadas
- ✅ `.env.example` presente
- ✅ `.gitignore` configurado
- ✅ System prompt customizado
- ✅ Dados simulados de telemetria
- ✅ Alertas implementados em Python
- ✅ IA via Ollama Cloud
- ✅ Modelo `gpt-oss:120b`
- ✅ Persona definida
- ✅ Impacto terrestre explicado
- ✅ Cenários críticos demonstráveis
- ✅ Arquivo `.txt` de entrega incluído

---

# 📄 Licença

Projeto acadêmico desenvolvido para a **Global Solution 2026.1 — FIAP — Ciência da Computação**.
