import tkinter as tk
from tkinter import font as tkfont
import random
import string


# ── Colour palette ──────────────────────────────────────────────────────────
BG        = "#1a1a2e"   # deep navy background
PANEL     = "#16213e"   # slightly lighter panel
ACCENT    = "#0f3460"   # card background
HIGHLIGHT = "#e94560"   # vivid red-pink accent
FG        = "#eaeaea"   # main text
FG_DIM    = "#8892a4"   # dimmed text
BTN_HOVER = "#c73652"   # button hover colour
COPY_OK   = "#39d353"   # green flash for "Copied!"


def generate_password(length: int) -> str:
    """Return a cryptographically-style random password of *length* characters."""
    if length <= 0:
        return ""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    guaranteed = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    if length <= 4:
        password = guaranteed[:length]
    else:
        rest = [random.choice(alphabet) for _ in range(length - 4)]
        password = guaranteed + rest
    random.shuffle(password)
    return "".join(password)


class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.resizable(False, False)
        self.configure(bg=BG)

        self._title_font  = tkfont.Font(family="Segoe UI", size=22, weight="bold")
        self._label_font  = tkfont.Font(family="Segoe UI", size=11)
        self._input_font  = tkfont.Font(family="Segoe UI", size=13)
        self._pass_font   = tkfont.Font(family="Consolas",  size=15, weight="bold")
        self._btn_font    = tkfont.Font(family="Segoe UI", size=13, weight="bold")
        self._small_font  = tkfont.Font(family="Segoe UI", size=9)

        self._build_ui()
        self._centre_window(520, 480)

    def _build_ui(self):
        outer = tk.Frame(self, bg=BG, padx=32, pady=28)
        outer.pack(fill="both", expand=True)

        tk.Label(outer, text="Password Generator",
                 font=self._title_font, bg=BG, fg=HIGHLIGHT).pack(pady=(0, 4))
        tk.Label(outer, text="Create strong, random passwords instantly",
                 font=self._small_font, bg=BG, fg=FG_DIM).pack(pady=(0, 24))

        # Password display
        display_frame = tk.Frame(outer, bg=ACCENT, padx=16, pady=14,
                                 highlightbackground=HIGHLIGHT, highlightthickness=1)
        display_frame.pack(fill="x", pady=(0, 6))
        tk.Label(display_frame, text="Generated Password",
                 font=self._small_font, bg=ACCENT, fg=FG_DIM).pack(anchor="w")

        self._password_var = tk.StringVar(value="Your password will appear here")
        self._pass_label = tk.Label(display_frame, textvariable=self._password_var,
                                    font=self._pass_font, bg=ACCENT, fg=FG,
                                    wraplength=420, justify="left")
        self._pass_label.pack(anchor="w", pady=(6, 0))

        self._copy_btn = tk.Button(display_frame, text="Copy",
                                   font=self._small_font, bg=PANEL, fg=FG_DIM,
                                   relief="flat", cursor="hand2",
                                   activebackground=ACCENT, activeforeground=FG,
                                   command=self._copy_to_clipboard, padx=8, pady=3)
        self._copy_btn.pack(anchor="e", pady=(8, 0))

        # Length input
        input_frame = tk.Frame(outer, bg=BG)
        input_frame.pack(fill="x", pady=(20, 0))
        tk.Label(input_frame, text="Number of characters",
                 font=self._label_font, bg=BG, fg=FG).pack(anchor="w")

        entry_wrap = tk.Frame(input_frame, bg=ACCENT,
                              highlightbackground=FG_DIM, highlightthickness=1)
        entry_wrap.pack(fill="x", pady=(6, 0))
        self._length_var = tk.StringVar(value="16")
        self._entry = tk.Entry(entry_wrap, textvariable=self._length_var,
                               font=self._input_font, bg=ACCENT, fg=FG,
                               insertbackground=HIGHLIGHT, relief="flat", justify="center")
        self._entry.pack(fill="x", ipady=10, padx=12)
        self._entry.bind("<FocusIn>",  lambda _: entry_wrap.config(highlightbackground=HIGHLIGHT))
        self._entry.bind("<FocusOut>", lambda _: entry_wrap.config(highlightbackground=FG_DIM))
        self._entry.bind("<Return>", lambda _: self._generate())

        self._hint_var = tk.StringVar(value="")
        self._hint_label = tk.Label(input_frame, textvariable=self._hint_var,
                                    font=self._small_font, bg=BG, fg=FG_DIM)
        self._hint_label.pack(anchor="w", pady=(4, 0))

        # Generate button
        self._gen_btn = tk.Button(outer, text="Generate", font=self._btn_font,
                                  bg=HIGHLIGHT, fg="#ffffff",
                                  activebackground=BTN_HOVER, activeforeground="#ffffff",
                                  relief="flat", cursor="hand2",
                                  command=self._generate, padx=20, pady=12)
        self._gen_btn.pack(fill="x", pady=(24, 0))
        self._gen_btn.bind("<Enter>", lambda _: self._gen_btn.config(bg=BTN_HOVER))
        self._gen_btn.bind("<Leave>", lambda _: self._gen_btn.config(bg=HIGHLIGHT))

        tk.Label(outer, text="Tip: press Enter to generate quickly",
                 font=self._small_font, bg=BG, fg=FG_DIM).pack(pady=(12, 0))

    def _generate(self):
        raw = self._length_var.get().strip()
        try:
            length = int(raw)
            if length < 1:
                raise ValueError
        except ValueError:
            self._password_var.set("Enter a valid number (min 1)")
            self._pass_label.config(fg="#e9c46a")
            self._hint_var.set("")
            return

        password = generate_password(length)
        self._password_var.set(password)
        self._pass_label.config(fg=FG)
        self._copy_btn.config(text="Copy", fg=FG_DIM)
        self._update_strength_hint(length)

    def _update_strength_hint(self, length: int):
        if length < 8:
            hint, colour = "Weak - use at least 8 characters", "#e9c46a"
        elif length < 12:
            hint, colour = "Fair", "#90be6d"
        elif length < 20:
            hint, colour = "Strong", "#43aa8b"
        else:
            hint, colour = "Very Strong", COPY_OK
        self._hint_var.set(hint)
        self._hint_label.config(fg=colour)

    def _copy_to_clipboard(self):
        pw = self._password_var.get()
        if not pw or pw.startswith("Your password") or pw.startswith("Enter"):
            return
        self.clipboard_clear()
        self.clipboard_append(pw)
        self._copy_btn.config(text="Copied!", fg=COPY_OK)
        self.after(2000, lambda: self._copy_btn.config(text="Copy", fg=FG_DIM))

    def _centre_window(self, w: int, h: int):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x  = (sw - w) // 2
        y  = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
