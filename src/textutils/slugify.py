"""
Funktioner for att omvandla text till URL-sakra strangar (slugs).
"""

import re


def slugify(text: str) -> str:
    """Omvandlar en text till en URL-saker slug.

    Exempel:
        "Hello World!" -> "hello-world"
        "  Spaces  " -> "spaces"
        "Cafe au lait" -> "cafe-au-lait"

    Args:
        text: Texten som skall omvandlas.

    Returns:
        En gemener-slug dar mellanslag och specialtecken ersatts med bindestreck.

    Raises:
        TypeError: Om text inte ar en strang.
        ValueError: Om text ar en tom strang.
    """
    if not isinstance(text, str):
        raise TypeError(f"Forvantade en strang, fick {type(text).__name__}.")
    if not text.strip():
        raise ValueError("Text far inte vara tom eller bara bestaa av mellanslag.")

    # Ga till gemener
    text = text.lower()

    # Ersatt svenska tecken
    replacements = {
        "ä": "a",
        "å": "a",
        "ö": "o",
        "Å": "a",
        "Ä": "a",
        "Ö": "o",
    }
    for original, replacement in replacements.items():
        text = text.replace(original, replacement)

    # Ersatt allt som inte ar bokstav, siffra eller bindestreck med bindestreck
    text = re.sub(r"[^a-z0-9]+", "-", text)

    # Ta bort inledande och avslutande bindestreck
    text = text.strip("-")

    return text


def truncate_slug(slug: str, max_length: int = 50) -> str:
    """Kortar ned en slug till ett maximalt antal tecken.

    Kapar vid ord-gransen (bindestreck) sa att slugen inte avslutas mitt i ett ord.

    Args:
        slug: En giltig slug (gemener, bindestreck, siffror).
        max_length: Max antal tecken. Standard ar 50.

    Returns:
        En kortad slug som inte avslutas med bindestreck.

    Raises:
        ValueError: Om max_length ar mindre an 1.
    """
    if max_length < 1:
        raise ValueError("max_length maste vara minst 1.")

    if len(slug) <= max_length:
        return slug

    kortad = slug[:max_length]
    # Kapa vid sista bindestreck om slugen avslutas mitt i ett ord
    if "-" in kortad:
        kortad = kortad.rsplit("-", 1)[0]

    return kortad.strip("-")
