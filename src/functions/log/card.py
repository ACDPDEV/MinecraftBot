from src.functions.log.maxCapacity import maxCapaityTitle, maxCapacityLines
from src.constants.COLORS import *

def card(title: str, content: list[str], border_color: str = TEXT_CYAN, title_color: str = TEXT_CYAN, content_color: str = TEXT_WHITE, title_background_color: str = BLANK, content_background_color: str = BLANK, symbol: str = "╮"):
    
    title = maxCapaityTitle(title)
    content = maxCapacityLines(content)

    print(f"{border_color}╭────────── {title_background_color}{title_color}{title}{RESET} {border_color}───────────{symbol}{RESET}")
    print(f"{border_color}│                                                     │{RESET}")
    for line in content:
        print(f"{border_color}│  {content_background_color}{content_color}{line}{RESET}  {border_color}│{RESET}")
    print(f"{border_color}│                                                     │{RESET}")
    print(f"{border_color}╰─────────────────────────────────────────────────────╯{RESET}")
