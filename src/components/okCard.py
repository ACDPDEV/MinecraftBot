from src.functions.log.card import card
from src.constants.COLORS import *

def okCard(title: str, content: list[str]):
    card(
        title=title,
        content=content,

        border_color=TEXT_GREEN,
        title_color=TEXT_BLACK,
        title_background_color=BG_GREEN,
        content_color=TEXT_CYAN,
        symbol="✨"
    )
