"""Geração de telemetria simulada para a trilha EnviroSat.

Este módulo cria dados plausíveis de operação para um satélite ambiental.
Os valores são simulados, mas representam parâmetros importantes de uma
missão de observação da Terra.
"""

from __future__ import annotations

import random
from datetime import datetime
from typing import Any, Dict


CENARIOS_SUPORTADOS = {
    "normal",
    "temperatura",
    "energia",
    "comunicacao",
    "incendio",
    "geolocalizacao",
    "multicrise",
}


def coletar(cenario: str = "normal") -> Dict[str, Any]:
    """Gera dados simulados de telemetria.

    Args:
        cenario: normal, temperatura, energia, comunicacao, incendio,
        geolocalizacao ou multicrise.

    Returns:
        Dicionário com a telemetria do ciclo atual.
    """

    if cenario not in CENARIOS_SUPORTADOS:
        cenario = "normal"

    dados = {
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "satelite": "EnviroSat Guard-01",
        "orbita": "LEO - órbita baixa terrestre",
        "trilha": "EnviroSat - Observação Ambiental",
        "cenario_simulado": cenario,
        "temperatura_sensor_c": round(random.uniform(28.0, 44.5), 1),
        "energia_disponivel_pct": round(random.uniform(58.0, 96.0), 1),
        "buffer_imagens_pct": round(random.uniform(12.0, 62.0), 1),
        "sinal_comunicacao_pct": round(random.uniform(76.0, 99.0), 1),
        "precisao_geolocalizacao_m": round(random.uniform(3.0, 11.5), 1),
        "focos_termicos_detectados": random.randint(0, 6),
        "area_monitorada": random.choice([
            "Amazônia Legal",
            "Cerrado brasileiro",
            "Pantanal",
            "Área de proteção ambiental costeira",
            "Reserva ambiental estadual",
        ]),
    }

    if cenario == "temperatura":
        dados["temperatura_sensor_c"] = round(random.uniform(62.0, 76.0), 1)

    elif cenario == "energia":
        dados["energia_disponivel_pct"] = round(random.uniform(7.0, 18.5), 1)

    elif cenario == "comunicacao":
        dados["sinal_comunicacao_pct"] = round(random.uniform(7.0, 25.0), 1)
        dados["buffer_imagens_pct"] = round(random.uniform(86.0, 98.0), 1)

    elif cenario == "incendio":
        dados["focos_termicos_detectados"] = random.randint(24, 47)
        dados["temperatura_sensor_c"] = round(random.uniform(48.0, 59.0), 1)

    elif cenario == "geolocalizacao":
        dados["precisao_geolocalizacao_m"] = round(random.uniform(16.0, 29.0), 1)

    elif cenario == "multicrise":
        dados["temperatura_sensor_c"] = round(random.uniform(63.0, 78.0), 1)
        dados["energia_disponivel_pct"] = round(random.uniform(8.0, 19.0), 1)
        dados["sinal_comunicacao_pct"] = round(random.uniform(8.0, 24.0), 1)
        dados["buffer_imagens_pct"] = round(random.uniform(88.0, 99.0), 1)
        dados["focos_termicos_detectados"] = random.randint(28, 55)

    return dados
