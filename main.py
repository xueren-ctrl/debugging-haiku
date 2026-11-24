"""Debugging Haiku — a 5-7-5 haiku about debugging (17 syllables total).

Syllable count per line:
  Line 1: "Breakpoint at midnight"             — 5  (break-point 2, at 1, mid-night 2)
  Line 2: "logs scroll past, red and endless"  — 7  (logs 1, scroll 1, past 1, red 1, and 1, end-less 2)
  Line 3: "it was a typo"                      — 5  (it 1, was 1, a 1, ty-po 2)
"""

# Each entry is a (line, syllable count) pair, so the 5-7-5 shape
# is part of the data instead of living only in the docstring.
HAIKU = [
    ("Breakpoint at midnight", 5),
    ("logs scroll past, red and endless", 7),
    ("it was a typo", 5),
]

def print_haiku():
    """Print the haiku, verifying each line's syllable count is 5-7-5."""
    expected = (5, 7, 5)
    for (line, syllables), want in zip(HAIKU, expected):
        assert syllables == want, (
            f"expected {want} syllables, got {syllables} for {line!r}"
        )
        print(line)


print_haiku()
