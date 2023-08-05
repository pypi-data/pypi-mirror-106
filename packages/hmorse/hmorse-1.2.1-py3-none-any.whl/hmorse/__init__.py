_to_morse = {
    "!": "HhHhHH",
    "'": "hHHHHh",
    '"': "hHhhHh",
    "$": "hhhHhhH",
    "&": "hHhhh",
    "(": "HhHHh",
    ")": "HhHHhH",
    "+": "hHhHh",
    ",": "HHhhHH",
    "-": "HhhhhH",
    ".": "hHhHhH",
    "/": "HhhHh",
    "0": "HHHHH",
    "1": "hHHHH",
    "2": "hhHHH",
    "3": "hhhHH",
    "4": "hhhhH",
    "5": "hhhhh",
    "6": "Hhhhh",
    "7": "HHhhh",
    "8": "HHHhh",
    "9": "HHHHh",
    ":": "HHHhhh",
    ";": "HhHhHh",
    "=": "HhhhH",
    "?": "hhHHhh",
    "@": "hHHhHh",
    "A": "hH",
    "B": "Hhhh",
    "C": "HhHh",
    "D": "Hhh",
    "E": "h",
    "F": "hhHh",
    "G": "HHh",
    "H": "hhhh",
    "I": "hh",
    "J": "hHHH",
    "K": "HhH",
    "L": "hHhh",
    "M": "HH",
    "N": "Hh",
    "O": "HHH",
    "P": "hHHh",
    "Q": "HHhH",
    "R": "hHh",
    "S": "hhh",
    "T": "H",
    "U": "hhH",
    "V": "hhhH",
    "W": "hHH",
    "X": "HhhH",
    "Y": "HhHH",
    "Z": "HHhh",
    "_": "hhHHhH",
}

_from_morse = {v: k for k, v in _to_morse.items()}


def encode(text: str, csep: str = " ", wsep: str = "/") -> str:
    words = text.split()

    output_words = []

    for word in words:
        output = ""
        for i, letter in enumerate(word):
            output += _to_morse.get(letter.upper(), letter.upper())
            output += csep if i < len(word) - 1 else ""
        output_words.append(output.strip())

    return f"{wsep}".join(output_words)

def decode(text: str, csep: str = " ", wsep: str = "/") -> str:
    words = [word.strip() for word in text.split(wsep)]

    output = ""

    for word in words:
        for letter in word.split(csep):
            output += _from_morse.get(letter, letter)
        output += " "

    return output

__all__ = (
    encode,
    decode,
)
