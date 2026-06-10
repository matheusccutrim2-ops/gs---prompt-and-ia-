"""Interface CLI estilo Claude Code para o Mission Control AI."""

from __future__ import annotations

from datetime import datetime

import pyfiglet
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()
session = PromptSession(style=Style.from_dict({"prompt": "#06B6D4 bold"}))


def show_banner() -> None:
    """Exibe o banner principal da aplicação."""

    banner = pyfiglet.figlet_format("Mission Control AI", font="slant")
    console.print(Text(banner, style="bold cyan"))

    console.print(Panel.fit(
        "EnviroSat Guard — Monitoramento ambiental com IA generativa\n"
        "Modelo: gpt-oss:120b via Ollama Cloud\n"
        "Use /help para ver comandos · /exit para sair",
        title="◆ MISSION CONTROL",
        border_style="cyan",
    ))


def show_help() -> None:
    """Mostra comandos disponíveis."""

    tabela = Table(title="Comandos disponíveis")
    tabela.add_column("Comando", style="cyan", no_wrap=True)
    tabela.add_column("Descrição")

    tabela.add_row("/status", "Mostra telemetria atual sem chamar a IA.")
    tabela.add_row("/about", "Explica objetivo, trilha e persona do projeto.")
    tabela.add_row("/clear", "Limpa o terminal e mostra o banner novamente.")
    tabela.add_row("/exit", "Encerra a aplicação.")

    tabela.add_row("Analise a missão atual", "Chama a IA com cenário normal.")
    tabela.add_row("Simule um incêndio crítico", "Chama a IA com cenário crítico de focos térmicos.")
    tabela.add_row("Verifique perda de comunicação", "Chama a IA com falha de sinal/downlink.")
    tabela.add_row("Existe risco de temperatura crítica?", "Chama a IA com superaquecimento do sensor.")
    tabela.add_row("Simule multicrise", "Chama a IA com múltiplas anomalias simultâneas.")

    console.print(tabela)


def show_about() -> None:
    """Mostra informações do projeto."""

    texto = (
        "Projeto: Mission Control AI — EnviroSat Guard\n"
        "Integrante: Matheus Costa Cutrim — RM: 568087\n"
        "Modalidade: Individual\n\n"
        "Trilha: EnviroSat — Observação Ambiental\n"
        "Persona: Operador de centro de controle ambiental\n\n"
        "O sistema simula telemetria de um satélite ambiental, gera alertas por regras em Python "
        "e usa IA generativa para explicar diagnóstico, severidade, impacto terrestre e ações recomendadas."
    )
    show_response(texto)


def show_response(texto: str) -> None:
    """Renderiza uma resposta em painel."""

    agora = datetime.now().strftime("%H:%M")
    console.print(Panel(
        texto,
        title="◆ Mission Control AI",
        subtitle=agora,
        border_style="cyan",
    ))


def run_cli(engine) -> None:
    """Loop principal da interface."""

    show_banner()

    if engine.is_ready():
        console.print("Engine status: FUNCIONANDO ✓\n", style="green")
    else:
        console.print("Engine status: AGUARDANDO IMPLEMENTAÇÃO ✗\n", style="yellow")

    while True:
        try:
            entrada = session.prompt("❯ ").strip()
        except (KeyboardInterrupt, EOFError):
            break

        if not entrada:
            continue

        if entrada == "/exit":
            console.print("Encerrando Mission Control AI...", style="cyan")
            break

        if entrada == "/help":
            show_help()
            continue

        if entrada == "/about":
            show_about()
            continue

        if entrada == "/clear":
            console.clear()
            show_banner()
            continue

        if entrada == "/status":
            show_response(engine.status_snapshot())
            continue

        with console.status("[cyan]Consultando IA via Ollama Cloud...[/cyan]", spinner="dots"):
            resposta = engine.analyze(entrada)

        show_response(resposta)
