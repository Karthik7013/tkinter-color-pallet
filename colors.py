import random

HEX_PALETTE = "0123456789abcdef"
HEX_DIGITS = set(HEX_PALETTE)
MIN_HEX_LENGTH = 6
SHORTHAND_HEX_LENGTH = 3
LUMINANCE_THRESHOLD = 0.5
DEFAULT_COLOR = "#000000"


def luminance(hex_color: str) -> float:
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def best_contrast_color(hex_color: str) -> str:
    return "black" if luminance(hex_color) > LUMINANCE_THRESHOLD else "white"


def is_valid_hex(value: str) -> bool:
    cleaned = value.strip().lstrip("#").lower()
    if len(cleaned) not in (SHORTHAND_HEX_LENGTH, MIN_HEX_LENGTH):
        return False
    return all(c in HEX_DIGITS for c in cleaned)


def normalize_hex(value: str) -> str:
    cleaned = value.strip().lstrip("#").lower()
    if len(cleaned) == SHORTHAND_HEX_LENGTH:
        cleaned = "".join(ch * 2 for ch in cleaned)
    return f"#{cleaned}"


def random_hex_color() -> str:
    return f"#{''.join(random.choice(HEX_PALETTE) for _ in range(MIN_HEX_LENGTH))}"
