"""Gerador auxiliar de banner ASCII para o projeto Mission Control AI."""

import argparse
import pyfiglet
from rich.console import Console
from rich.align import Align
from rich.text import Text

console = Console()


def mostrar_banner(texto: str, fonte: str) -> None:
    """Renderiza um banner ASCII no terminal."""
    banner = pyfiglet.figlet_format(texto, font=fonte)
    console.print(Align.center(Text(banner, style="bold cyan")))
    console.print(Align.center(
        Text("Global Solution 2026.1 · Prompt Engineering and AI · FIAP", style="italic")
    ))


def listar_fontes() -> None:
    """Lista fontes disponíveis no PyFiglet."""
    for fonte in pyfiglet.FigletFont.getFonts():
        console.print(fonte)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Banner ASCII da Mission Control AI")
    parser.add_argument("-text", default="Mission Control AI", help="Texto do banner")
    parser.add_argument("-font", default="slant", help="Fonte PyFiglet")
    parser.add_argument("-fonts", action="store_true", help="Lista fontes disponíveis")
    args = parser.parse_args()

    if args.fonts:
        listar_fontes()
    else:
        mostrar_banner(args.text, args.font)
