from src.functions.log.card import card
from src.constants.COLORS import *

def errorCard(title: str, content: list[str]):
    card(
        title=title,
        content=content,

        border_color=TEXT_RED,
        title_color=TEXT_WHITE,
        title_background_color=BG_RED,
        content_color=TEXT_MAGENTA,
        symbol="⚠️"
    )
