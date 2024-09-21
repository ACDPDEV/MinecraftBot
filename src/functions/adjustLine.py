def splitString(string: str, max_length: int = 49):
    parts = []
    
    for i in range(0, len(string), max_length):
        parts.append(string[i:i + max_length])
    
    return parts

def addSpacesString(string: str, max_length: int = 49):
    count_spaces = max_length  - len(string)
    spaces = " " * count_spaces
    new_string = string + spaces
    return new_string

def cutString(string: str, max_length: int = 30):
    cut_string = string[0:max_length-3]
    new_string = cut_string + "..."
    return new_string
