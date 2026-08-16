"""
Funktioner for att analysera och sammanfatta textstatistik.
"""

import re


def word_count(text: str) -> int:
    """Raknar antalet ord i en text.

    Ord definieras som sekvenser av icke-mellanslags-tecken.
    En tom strang returnerar 0.

    Args:
        text: Texten som skall analyseras.

    Returns:
        Antalet ord.

    Raises:
        TypeError: Om text inte ar en strang.
    """
    if not isinstance(text, str):
        raise TypeError(f"Forvantade en strang, fick {type(text).__name__}.")

    return len(text.split())


def sentence_count(text: str) -> int:
    """Raknar antalet meningar i en text.

    En mening raknas som en sekvens som avslutas med punkt, utropstecken
    eller frageTecken. Flera avslutande tecken i rad (t.ex. '...') raknas
    som ett avslut.

    Args:
        text: Texten som skall analyseras.

    Returns:
        Antalet meningar. Returnerar 0 for en tom strang.

    Raises:
        TypeError: Om text inte ar en strang.
    """
    if not isinstance(text, str):
        raise TypeError(f"Forvantade en strang, fick {type(text).__name__}.")

    if not text.strip():
        return 0

    meningar = re.split(r"[.!?]+", text)
    # Filtrera bort tomma element som uppstar efter sista skiljetecknet
    return len([m for m in meningar if m.strip()])


def average_word_length(text: str) -> float:
    """Beraknar genomsnittlig ordlangd i en text.

    Args:
        text: Texten som skall analyseras.

    Returns:
        Genomsnittligt antal tecken per ord, avrundat till tva decimaler.
        Returnerar 0.0 om texten inte innehaller nagra ord.

    Raises:
        TypeError: Om text inte ar en strang.
    """
    if not isinstance(text, str):
        raise TypeError(f"Forvantade en strang, fick {type(text).__name__}.")

    ord_lista = text.split()
    if not ord_lista:
        return 0.0

    total = sum(len(ord) for ord in ord_lista)
    return round(total / len(ord_lista), 2)


def summarize(text: str) -> dict:
    """Returnerar en sammanstalld textanalys som en ordbok.

    Args:
        text: Texten som skall analyseras.

    Returns:
        En ordbok med nycklarna:
            - "ord": antal ord (int)
            - "meningar": antal meningar (int)
            - "tecken": antal tecken inklusive mellanslag (int)
            - "genomsnittlig_ordlangd": genomsnittlig ordlangd (float)

    Raises:
        TypeError: Om text inte ar en strang.
    """
    if not isinstance(text, str):
        raise TypeError(f"Forvantade en strang, fick {type(text).__name__}.")

    return {
        "ord": word_count(text),
        "meningar": sentence_count(text),
        "tecken": len(text),
        "genomsnittlig_ordlangd": average_word_length(text),
    }
