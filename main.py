import tkinter as tk

from colors import (
    DEFAULT_COLOR,
    best_contrast_color,
    is_valid_hex,
    normalize_hex,
    random_hex_color,
)

ERROR_MESSAGE_DURATION_MS = 900

WINDOW_TITLE = "Cool Colors"
WINDOW_GEOMETRY = "500x500"
WINDOW_BG = "grey"

TITLE_FONT = ("rockwell", 20, "bold")
TITLE_FG = "snow"
LABEL_FONT = ("", 15, "italic", "bold")
LABEL_FG_DEFAULT = "white"
ENTRY_FONT = ("", 15, "bold")
ENTRY_WIDTH = 10
GENERATE_BTN_TEXT = "Generate"
GENERATE_BTN_FG = "white"
GENERATE_BTN_BG = "green"
SEARCH_BTN_TEXT = "Search"
SEARCH_BTN_FG = "white"
SEARCH_BTN_BG = "orange"
ERROR_FG = "red"


class ColorPallet:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self._configure_root()
        self.color = DEFAULT_COLOR
        self._build_widgets()
        self.set_color(random_hex_color())

    def _configure_root(self) -> None:
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_GEOMETRY)
        self.root.resizable(False, False)
        self.root.configure(bg=WINDOW_BG)

    def _build_widgets(self) -> None:
        tk.Label(
            self.root,
            text="Cool ColorPallet",
            font=TITLE_FONT,
            bg=WINDOW_BG,
            fg=TITLE_FG,
        ).pack(pady=(20, 0))

        self.color_frame = tk.Frame(self.root, background=self.color)
        self.color_frame.pack(pady=30, ipadx=200, ipady=100)

        self.color_label = tk.Label(self.color_frame, text=self.color)
        self.color_label.pack(side="bottom")

        entry_frame = tk.Frame(self.root)
        entry_frame.pack()

        self.hex_entry = tk.Entry(
            entry_frame, font=ENTRY_FONT, width=ENTRY_WIDTH, justify="center"
        )
        self.hex_entry.pack()
        self.hex_entry.insert(0, self.color)

        button_frame = tk.Frame(self.root, bg=WINDOW_BG)
        button_frame.pack(pady=30)

        tk.Button(
            button_frame,
            text=GENERATE_BTN_TEXT,
            command=self.generate_color,
            fg=GENERATE_BTN_FG,
            bg=GENERATE_BTN_BG,
        ).pack(side="right", padx=(25, 0))

        tk.Button(
            button_frame,
            text=SEARCH_BTN_TEXT,
            command=self.apply_color,
            fg=SEARCH_BTN_FG,
            bg=SEARCH_BTN_BG,
        ).pack(side="left", padx=(0, 40))

        self.error_label = tk.Label(
            self.root,
            text="",
            bg=WINDOW_BG,
            font=LABEL_FONT,
            fg=LABEL_FG_DEFAULT,
        )
        self.error_label.pack()

    def set_color(self, hex_color: str) -> None:
        self.color = hex_color
        self.color_frame.configure(background=hex_color)
        contrast = best_contrast_color(hex_color)
        self.color_label.configure(text=hex_color, fg=contrast, bg=hex_color)
        self.hex_entry.delete(0, tk.END)
        self.hex_entry.insert(0, hex_color)
        self.hex_entry.focus()

    def generate_color(self) -> None:
        self.set_color(random_hex_color())

    def apply_color(self) -> None:
        entry_value = self.hex_entry.get()
        if not is_valid_hex(entry_value):
            self._show_error("Invalid Color Code...")
            return
        self.set_color(normalize_hex(entry_value))

    def _show_error(self, message: str) -> None:
        self.error_label.configure(text=message, fg=ERROR_FG)
        self.error_label.after(
            ERROR_MESSAGE_DURATION_MS,
            lambda: self.error_label.configure(text="", fg=LABEL_FG_DEFAULT),
        )


def main() -> None:
    root = tk.Tk()
    ColorPallet(root)
    root.mainloop()


if __name__ == "__main__":
    main()
