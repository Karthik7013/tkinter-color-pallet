# Color Pallet

A Tkinter color palette generator. Generates random hex colors, lets you search
any valid hex color code, and auto-switches label text to black/white based on
background luminance for readability.

## Technologies

![Python](https://ik.imagekit.io/ybyfbcvb8/python.png?updatedAt=1692968478421)

## Project structure

```
main.py        # Tkinter UI (entry point: python3 main.py)
colors.py      # Pure color logic (no GUI dependency, unit-testable)
tests/         # Unit tests for colors.py
pyproject.toml # Packaging metadata + test config
```

## How to run the application

- Make sure Python 3.8+ is installed with Tkinter support (`python3 -c "import tkinter"`)
- Run the GUI:

```bash
python3 main.py
```

## Development

Install dev dependencies (optional, for packaging/pytest):

```bash
pip install -e ".[dev]"
```

Run the tests (uses the standard library `unittest`; no install required):

```bash
python3 -m unittest discover -s tests
# or, with pytest:
pytest
```

## Screenshots

![Cool Colors](https://github.com/Karthik7013/tkinter-color-pallet/assets/113322353/6227d90f-3e75-495a-bdad-a145f11e0aaa)
