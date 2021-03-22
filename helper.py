from pathlib import Path
from string import ascii_lowercase, ascii_uppercase
from textwrap import dedent


def generate_numbers_file():
    numbers_file = Path("src/packs/markers/numbers.yml")
    numbers_file.unlink(missing_ok=True)

    for n in range(1, 101):

        entry = dedent(f"""
    ---
    name: "{n:03}"
    type: "character"
    img: modules/markers/assets/images/numbers/{n:03}.png
    token:
      disposition: 0""")
        print(entry, file=open(numbers_file, "a"))


def generate_alphabet_files():
    alphabet_file = Path("src/packs/markers/alphabet_lower.yml")
    alphabet_file.unlink(missing_ok=True)
    for l in range(len(ascii_lowercase)):
        letter = ascii_lowercase[l]
        entry = dedent(f"""
    ---
    name: "{letter}"
    type: "character"
    img: modules/markers/assets/images/letters/lower_{letter}.png
    token:
      disposition: 0""")
        print(entry, file=open(alphabet_file, "a"))

    alphabet_file = Path("src/packs/markers/alphabet_upper.yml")
    alphabet_file.unlink(missing_ok=True)
    for l in range(len(ascii_uppercase)):
        letter = ascii_uppercase[l]
        entry = dedent(f"""
    ---
    name: "{letter}"
    type: "character"
    img: modules/markers/assets/images/letters/upper_{letter.lower()}.png
    token:
      disposition: 0""")
        print(entry, file=open(alphabet_file, "a"))


def generate_symbols_file():
    symbols_file = Path("src/packs/markers/symbols.yml")
    symbols_file.unlink(missing_ok=True)

    symbols = [
        "asterisk",
        "at",
        "backslash",
        "dollar",
        "equals",
        "exclamation",
        "forwardslash",
        "minus",
        "percent",
        "plus",
        "pound",
        "question"
    ]

    for s in range(len(symbols)):
        symbol = symbols[s]
        entry = dedent(f"""
    ---
    name: "{symbol.capitalize()}"
    type: "character"
    img: modules/markers/assets/images/symbols/symbol_{symbol}.png
    token:
      disposition: 0""")
        print(entry, file=open(symbols_file, "a"))


def main():
    generate_numbers_file()
    generate_alphabet_files()
    generate_symbols_file()


if __name__ == "__main__":
    main()
