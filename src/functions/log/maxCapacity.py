from src.functions.log.adjustLine import splitString, addSpacesString, cutString

def maxCapacityLines(lines: list, max_length: int = 49):
    new_lines = []
    for line in lines:
        parts = splitString(line, max_length)
        for part in parts:
            new_part = addSpacesString(part, max_length)
            new_lines.append(new_part)
    
    return new_lines

def maxCapaityTitle(title: str, max_length: int = 30):
    if len(title) > max_length:
        title = cutString(title, max_length)
    elif len(title) < max_length:
        title = addSpacesString(title, max_length)
    
    return title
