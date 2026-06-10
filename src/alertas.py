"""Regras de alerta e tomada de decisão da missão EnviroSat.

A lógica crítica fica em Python para cumprir o requisito do projeto:
a IA interpreta e comunica, mas as regras operacionais não dependem
somente do prompt.
"""

from __future__ import annotations

from typing import Any, Dict, List


def avaliar(dados: Dict[str, Any]) -> Dict[str, List[Dict[str, str]]]:
    """Avalia a telemetria e gera alertas e ações automáticas."""

    alertas: List[Dict[str, str]] = []
    acoes: List[Dict[str, str]] = []

    if dados["temperatura_sensor_c"] > 60:
        alertas.append({
            "nivel": "CRÍTICO",
            "tipo": "Superaquecimento do sensor térmico",
            "mensagem": "Temperatura acima do limite seguro para operação contínua."
        })
        acoes.append({
            "acao": "Ativar proteção térmica",
            "descricao": "Reduzir frequência de captura e colocar o payload óptico em modo seguro parcial."
        })

    if dados["energia_disponivel_pct"] < 20:
        alertas.append({
            "nivel": "CRÍTICO",
            "tipo": "Energia disponível baixa",
            "mensagem": "Energia insuficiente para manter todos os subsistemas em operação plena."
        })
        acoes.append({
            "acao": "Ativar modo economia",
            "descricao": "Priorizar comunicação com a base, telemetria essencial e preservação dos dados críticos."
        })

    if dados["sinal_comunicacao_pct"] < 30:
        alertas.append({
            "nivel": "ALTO",
            "tipo": "Perda parcial de comunicação",
            "mensagem": "Sinal abaixo do necessário para downlink confiável."
        })
        acoes.append({
            "acao": "Reagendar downlink",
            "descricao": "Armazenar imagens no buffer e tentar nova janela de transmissão."
        })

    if dados["buffer_imagens_pct"] > 85:
        alertas.append({
            "nivel": "ALTO",
            "tipo": "Buffer de imagens quase cheio",
            "mensagem": "Risco de perda de imagens ambientais ainda não transmitidas."
        })
        acoes.append({
            "acao": "Priorizar transmissão",
            "descricao": "Enviar primeiro imagens de regiões com focos térmicos ou áreas protegidas."
        })

    if dados["precisao_geolocalizacao_m"] > 15:
        alertas.append({
            "nivel": "MÉDIO",
            "tipo": "Baixa precisão geográfica",
            "mensagem": "A localização das imagens pode comprometer a análise ambiental."
        })
        acoes.append({
            "acao": "Recalibrar georreferenciamento",
            "descricao": "Recalibrar referência orbital antes do próximo ciclo de coleta."
        })

    if dados["focos_termicos_detectados"] >= 20:
        alertas.append({
            "nivel": "CRÍTICO",
            "tipo": "Possível evento de incêndio",
            "mensagem": "Quantidade elevada de focos térmicos detectados na área monitorada."
        })
        acoes.append({
            "acao": "Notificar equipe ambiental",
            "descricao": "Priorizar imagens da região e sinalizar possível emergência para brigadas e órgãos ambientais."
        })

    if not alertas:
        alertas.append({
            "nivel": "NORMAL",
            "tipo": "Operação nominal",
            "mensagem": "Todos os parâmetros estão dentro da faixa operacional esperada."
        })
        acoes.append({
            "acao": "Manter monitoramento padrão",
            "descricao": "Continuar a coleta e transmissão regular dos dados ambientais."
        })

    return {
        "alertas": alertas,
        "acoes_automaticas": acoes,
    }


def maior_severidade(alertas: List[Dict[str, str]]) -> str:
    """Retorna a maior severidade presente nos alertas."""

    pesos = {"NORMAL": 0, "MÉDIO": 1, "ALTO": 2, "CRÍTICO": 3}
    severidade = "NORMAL"

    for alerta in alertas:
        nivel = alerta.get("nivel", "NORMAL")
        if pesos.get(nivel, 0) > pesos.get(severidade, 0):
            severidade = nivel

    return severidade
