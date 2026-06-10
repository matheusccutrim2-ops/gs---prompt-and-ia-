"""Motor de análise da Mission Control AI.

Este arquivo integra:
1. coleta de telemetria simulada;
2. avaliação de alertas via Python;
3. montagem dinâmica do prompt;
4. chamada ao modelo gpt-oss:120b via Ollama Cloud.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv
from ollama import Client

from src.alertas import avaliar, maior_severidade
from src.telemetria import coletar

load_dotenv()

TRILHA = "EnviroSat"

client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.environ.get("OLLAMA_API_KEY", "")},
)


def carregar_system_prompt() -> str:
    """Carrega o system prompt usado pela IA."""

    caminho = Path("prompts/system_prompt.md")

    if caminho.exists():
        return caminho.read_text(encoding="utf-8")

    return "Você é uma IA operacional de missão espacial."


def llm(prompt: str, system: str | None = None, max_tokens: int = 800, temperature: float = 0.3) -> str:
    """Consulta o modelo gpt-oss:120b via Ollama Cloud."""

    mensagens: List[Dict[str, str]] = []

    if system:
        mensagens.append({"role": "system", "content": system})

    mensagens.append({"role": "user", "content": prompt})

    try:
        resposta = client.chat(
            model="gpt-oss:120b",
            messages=mensagens,
            options={
                "num_predict": max_tokens,
                "temperature": temperature,
            },
            stream=False,
        )

        return resposta["message"]["content"].strip()

    except Exception as erro:
        return (
            "⚠️ Não foi possível consultar a IA neste momento.\n\n"
            f"Detalhe técnico: {erro}\n\n"
            "Verifique se o arquivo .env existe, se a variável OLLAMA_API_KEY está preenchida "
            "e se há conexão com a internet."
        )


class MissionEngine:
    """Motor principal do projeto Mission Control AI."""

    def __init__(self) -> None:
        self.trilha = TRILHA
        self.system_prompt = carregar_system_prompt()
        self.historico: List[Dict[str, Any]] = []

    def is_ready(self) -> bool:
        """Indica que o motor foi implementado."""

        return True

    def detectar_cenario(self, entrada: str) -> str:
        """Detecta qual cenário simular a partir da pergunta do operador."""

        texto = entrada.lower()

        if "multicrise" in texto or "múltipla" in texto or "multipla" in texto:
            return "multicrise"

        if "temperatura" in texto or "superaquecimento" in texto or "aquecimento" in texto:
            return "temperatura"

        if "energia" in texto or "bateria" in texto:
            return "energia"

        if "comunicação" in texto or "comunicacao" in texto or "sinal" in texto or "downlink" in texto:
            return "comunicacao"

        if "incêndio" in texto or "incendio" in texto or "fogo" in texto or "queimada" in texto:
            return "incendio"

        if "geolocalização" in texto or "geolocalizacao" in texto or "precisão" in texto or "precisao" in texto:
            return "geolocalizacao"

        return "normal"

    def _registrar_historico(self, dados: Dict[str, Any], resultado: Dict[str, Any]) -> None:
        """Mantém um histórico curto dos últimos ciclos."""

        self.historico.append({
            "timestamp": dados["timestamp"],
            "cenario": dados["cenario_simulado"],
            "severidade": maior_severidade(resultado["alertas"]),
        })

        self.historico = self.historico[-5:]

    def status_snapshot(self) -> str:
        """Retorna um resumo legível da telemetria atual sem chamar IA."""

        dados = coletar("normal")
        resultado = avaliar(dados)
        self._registrar_historico(dados, resultado)

        linhas = [
            f"🛰️ MISSÃO: {dados['satelite']}",
            f"🌎 TRILHA: {dados['trilha']}",
            f"📍 ÁREA MONITORADA: {dados['area_monitorada']}",
            f"🕒 HORÁRIO: {dados['timestamp']}",
            "",
            "TELEMETRIA ATUAL:",
            f"- Temperatura do sensor: {dados['temperatura_sensor_c']} °C",
            f"- Energia disponível: {dados['energia_disponivel_pct']}%",
            f"- Buffer de imagens: {dados['buffer_imagens_pct']}%",
            f"- Sinal de comunicação: {dados['sinal_comunicacao_pct']}%",
            f"- Precisão de geolocalização: {dados['precisao_geolocalizacao_m']} m",
            f"- Focos térmicos detectados: {dados['focos_termicos_detectados']}",
            "",
            "ALERTAS GERADOS PELO PYTHON:",
        ]

        for alerta in resultado["alertas"]:
            linhas.append(f"- [{alerta['nivel']}] {alerta['tipo']}: {alerta['mensagem']}")

        linhas.append("")
        linhas.append("AÇÕES AUTOMÁTICAS:")
        for acao in resultado["acoes_automaticas"]:
            linhas.append(f"- {acao['acao']}: {acao['descricao']}")

        return "\n".join(linhas)

    def analyze(self, pergunta_usuario: str) -> str:
        """Analisa a pergunta do operador usando telemetria + alertas + IA."""

        cenario = self.detectar_cenario(pergunta_usuario)
        dados = coletar(cenario)
        resultado = avaliar(dados)
        severidade = maior_severidade(resultado["alertas"])
        self._registrar_historico(dados, resultado)

        prompt = f"""
Pergunta do operador:
{pergunta_usuario}

Trilha do projeto:
EnviroSat — Observação Ambiental.

Persona atendida:
Operador de centro de controle ambiental.

Dados simulados da telemetria deste ciclo:
{dados}

Alertas gerados pelo código Python:
{resultado["alertas"]}

Ações automáticas recomendadas pelo sistema:
{resultado["acoes_automaticas"]}

Maior severidade identificada:
{severidade}

Histórico resumido dos últimos ciclos:
{self.historico}

Tarefa:
Gere uma resposta operacional em português brasileiro contendo:
1. Diagnóstico técnico.
2. Severidade.
3. Impacto terrestre.
4. Ações recomendadas.
5. Resumo final objetivo para o operador.

Regras:
- Não invente dados fora da telemetria.
- Use os alertas Python como fonte principal de decisão.
- Explique como a situação afeta sustentabilidade, combate a incêndios, monitoramento ambiental ou áreas protegidas.
- Seja claro, direto e profissional.
"""

        return llm(
            prompt=prompt,
            system=self.system_prompt,
            max_tokens=850,
            temperature=0.3,
        )
