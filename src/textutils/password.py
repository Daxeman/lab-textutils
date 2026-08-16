"""
Funktioner for att kontrollera och betygsatta losenordsstyrka.
"""

import re


# Styrkenivåer
WEAK = "svagt"
MEDIUM = "medium"
STRONG = "starkt"
VERY_STRONG = "mycket starkt"


def check_strength(password: str) -> str:
    """Bedomt styrkan pa ett losenord.

    Bedomningen baseras pa langd och teckenvariation:
        - Svagt:          kortare an 8 tecken, eller bara en teckenklass
        - Medium:         minst 8 tecken och tva teckrenklasser
        - Starkt:         minst 10 tecken och tre teckrenklasser
        - Mycket starkt:  minst 12 tecken och alla fyra teckrenklasserna

    Teckrenklasserna ar:
        1. Gemener (a-z)
        2. Versaler (A-Z)
        3. Siffror (0-9)
        4. Specialtecken (!@#$ osv.)

    Args:
        password: Losenordet som skall bedommas.

    Returns:
        En av konstanterna WEAK, MEDIUM, STRONG eller VERY_STRONG.

    Raises:
        TypeError: Om password inte ar en strang.
    """
    if not isinstance(password, str):
        raise TypeError(f"Forvantade en strang, fick {type(password).__name__}.")

    langd = len(password)
    klasser = _rakna_teckrenklasser(password)

    if langd >= 12 and klasser == 4:
        return VERY_STRONG
    if langd >= 10 and klasser >= 3:
        return STRONG
    if langd >= 8 and klasser >= 2:
        return MEDIUM
    return WEAK


def has_common_pattern(password: str) -> bool:
    """Kontrollerar om losenordet innehaller vanliga, ossakra monster.

    Kontrollerar efter:
        - Upprepade tecken (aaa, 111)
        - Enkla sekvenser (abc, 123, qwerty)

    Args:
        password: Losenordet som skall kontrolleras.

    Returns:
        True om ett vanligt monster hittades, annars False.
    """
    if not isinstance(password, str):
        raise TypeError(f"Forvantade en strang, fick {type(password).__name__}.")

    lowered = password.lower()

    # Upprepade tecken (tre eller fler i rad)
    if re.search(r"(.)\1{2,}", lowered):
        return True

    # Vanliga sekvenser
    sequences = [
        "abcdef", "bcdefg", "cdefgh", "defghi",
        "123456", "234567", "345678", "456789",
        "qwerty", "asdfgh", "zxcvbn",
    ]
    for seq in sequences:
        if seq in lowered:
            return True

    return False


def _rakna_teckrenklasser(password: str) -> int:
    """Raknar hur manga teckrenklasser som finns representerade i losenordet.

    Intern hjalp-funktion. Anvands av check_strength.

    Args:
        password: Losenordet.

    Returns:
        Antal teckrenklasser (0-4).
    """
    klasser = 0
    if re.search(r"[a-z]", password):
        klasser += 1
    if re.search(r"[A-Z]", password):
        klasser += 1
    if re.search(r"[0-9]", password):
        klasser += 1
    if re.search(r"[^a-zA-Z0-9]", password):
        klasser += 1
    return klasser
