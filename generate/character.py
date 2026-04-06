from dataclasses import dataclass, fields
from string import (ascii_lowercase as lowercase_,
                    ascii_uppercase as uppercase_,
                    ascii_letters as letters_,
                    digits as digits_,
                    hexdigits as hexdigits_,
                    punctuation as punctuation_,
                    printable as printable_)

__all__ = ['Character', 'Ambiguous', 'Unambiguous', 'Unicode', 'MesloNerdFont']

_printable_range = lambda start, end: ''.join(
    chr(c) for c in range(start, end) if chr(c).isprintable()
)


@dataclass
class Character:
    @classmethod
    def all_chars(cls) -> str:
        """Concatenate all string-type field defaults into a single character pool."""
        return ''.join(
            f.default for f in fields(cls)
            if isinstance(f.default, str)
        )


@dataclass
class Ambiguous(Character):
    lower:str = lowercase_
    upper:str = uppercase_
    number:str = digits_
    punctuation:str = punctuation_

@dataclass
class Unambiguous(Character):
    lower:str = lowercase_.replace('l', '')                  # "l"  ell
    upper:str = uppercase_.replace('I', '').replace('O', '') # "IO" capital i, capital o
    number:str = digits_[2:]                                 # "01" zero and one
    punctuation:str = punctuation_.replace('|', '')          # "|"  vertical bar


class Unicode:
    """Lazy-loaded Unicode character sets — computed only on first access."""
    _code_points: frozenset[int] | None = None
    _printable: frozenset[str] | None = None
    _unprintable: frozenset[str] | None = None

    @classmethod
    def code_points(cls) -> frozenset[int]:
        if cls._code_points is None:
            cls._code_points = frozenset(range(0x110000))
        return cls._code_points

    @classmethod
    def printable_unicode_chars(cls) -> frozenset[str]:
        if cls._printable is None:
            cls._printable = frozenset(
                chr(cp) for cp in cls.code_points() if chr(cp).isprintable()
            )
        return cls._printable

    @classmethod
    def unprintable_unicode_chars(cls) -> frozenset[str]:
        if cls._unprintable is None:
            cls._unprintable = frozenset(
                chr(cp) for cp in cls.code_points() if not chr(cp).isprintable()
            )
        return cls._unprintable


# ---------------------------------------------------------------------------
# MesloLGS NF — Nerd Fonts v3.3.0 glyph sets + base Meslo Unicode coverage
# Reference: https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points
# ---------------------------------------------------------------------------

@dataclass
class MesloNerdFont(Character):
    """All character sets displayable by MesloLGS NF on Ubuntu terminal."""

    # ── Standard ASCII ─────────────────────────────────────────────────────
    lower: str = lowercase_
    upper: str = uppercase_
    number: str = digits_
    punctuation: str = punctuation_

    # ── Latin extensions (base Meslo / DejaVu Sans Mono coverage) ──────────
    latin_supplement: str = _printable_range(0x00A1, 0x0100)
    latin_extended_a: str = _printable_range(0x0100, 0x0180)
    latin_extended_b: str = _printable_range(0x0180, 0x0250)

    # ── Greek & Cyrillic ──────────────────────────────────────────────────
    greek: str = _printable_range(0x0370, 0x0400)
    cyrillic: str = _printable_range(0x0400, 0x0500)

    # ── Common Unicode symbol blocks ──────────────────────────────────────
    general_punctuation: str = _printable_range(0x2000, 0x2070)
    superscripts_subscripts: str = _printable_range(0x2070, 0x20A0)
    currency_symbols: str = _printable_range(0x20A0, 0x20D0)
    letterlike_symbols: str = _printable_range(0x2100, 0x2150)
    number_forms: str = _printable_range(0x2150, 0x2190)
    arrows: str = _printable_range(0x2190, 0x2200)
    math_operators: str = _printable_range(0x2200, 0x2300)
    misc_technical: str = _printable_range(0x2300, 0x2400)
    enclosed_alphanumerics: str = _printable_range(0x2460, 0x2500)
    box_drawing: str = _printable_range(0x2500, 0x2580)
    block_elements: str = _printable_range(0x2580, 0x25A0)
    geometric_shapes: str = _printable_range(0x25A0, 0x2600)
    misc_symbols: str = _printable_range(0x2600, 0x2700)
    dingbats: str = _printable_range(0x2700, 0x27C0)
    braille: str = _printable_range(0x2800, 0x2900)

    # ── Nerd Font glyphs (Private Use Area) ─────────────────────────────
    # NOTE: PUA code points are NOT considered printable by Python, so
    #       these ranges intentionally skip the _printable_range helper.

    # ── Nerd Font — Pomicons (E000‑E00A) ──────────────────────────────────
    pomicons: str = ''.join(chr(c) for c in range(0xE000, 0xE00B))

    # ── Nerd Font — Powerline (E0A0‑E0A2, E0B0‑E0B3) ────────────────────
    powerline: str = ''.join(chr(c) for c in [
        *range(0xE0A0, 0xE0A3), *range(0xE0B0, 0xE0B4),
    ])

    # ── Nerd Font — Powerline Extra (E0A3, E0B4‑E0C8, E0CA, E0CC‑E0D7, 2630)
    powerline_extra: str = ''.join(chr(c) for c in [
        0xE0A3, *range(0xE0B4, 0xE0C9), 0xE0CA,
        *range(0xE0CC, 0xE0D8), 0x2630,
    ])

    # ── Nerd Font — IEC Power Symbols (23FB‑23FE, 2B58) ──────────────────
    iec_power: str = ''.join(chr(c) for c in [*range(0x23FB, 0x23FF), 0x2B58])

    # ── Nerd Font — Font Awesome Extension (E200‑E2A9) ───────────────────
    fa_extension: str = ''.join(chr(c) for c in range(0xE200, 0xE2AA))

    # ── Nerd Font — Weather Icons (E300‑E3E3) ────────────────────────────
    weather: str = ''.join(chr(c) for c in range(0xE300, 0xE3E4))

    # ── Nerd Font — Seti-UI + Custom (E5FA‑E6B7) ─────────────────────────
    seti_ui: str = ''.join(chr(c) for c in range(0xE5FA, 0xE6B8))

    # ── Nerd Font — Devicons (E700‑E8EF) ─────────────────────────────────
    devicons: str = ''.join(chr(c) for c in range(0xE700, 0xE8F0))

    # ── Nerd Font — Codicons (EA60‑EC1E) ─────────────────────────────────
    codicons: str = ''.join(chr(c) for c in range(0xEA60, 0xEC1F))

    # ── Nerd Font — Font Awesome (ED00‑EDFF, EE0C‑EFCE, F000‑F2FF) ──────
    font_awesome: str = ''.join(chr(c) for c in [
        *range(0xED00, 0xEE00),
        *range(0xEE0C, 0xEFCF),
        *range(0xF000, 0xF300),
    ])

    # ── Nerd Font — Progress indicators (EE00‑EE0B) ─────────────────────
    progress: str = ''.join(chr(c) for c in range(0xEE00, 0xEE0C))

    # ── Nerd Font — Font Logos (F300‑F381) ───────────────────────────────
    font_logos: str = ''.join(chr(c) for c in range(0xF300, 0xF382))

    # ── Nerd Font — Octicons (F400‑F533, 2665, 26A1) ────────────────────
    octicons: str = ''.join(chr(c) for c in [
        *range(0xF400, 0xF534), 0x2665, 0x26A1,
    ])

    # ── Nerd Font — Material Design Icons (F0001‑F1AF0) ─────────────────
    material_design: str = ''.join(chr(c) for c in range(0xF0001, 0xF1AF1))

    # ── Nerd Font — Heavy Angle Brackets (276C‑2771) ────────────────────
    heavy_angle_brackets: str = _printable_range(0x276C, 0x2772)
