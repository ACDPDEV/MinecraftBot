from src.functions.log.maxCapacity import maxCapaityTitle, maxCapacityLines
from src.constants.COLORS import *

def inputCard(title: str, border_color: str = TEXT_CYAN, title_color: str = TEXT_CYAN, title_background_color: str = BLANK, symbol: str = "╮"):
    
    title = maxCapaityTitle(title)

    print(f"{border_color}╭────────── {title_background_color}{title_color}{title}{RESET} {border_color}───────────{symbol}{RESET}")
    message = input(f"{border_color}╰─>>{RESET} ")
    
    return message
