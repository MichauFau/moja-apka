# Password Generator

A lightweight desktop application for generating strong, random passwords — built with Python and Tkinter (no extra libraries needed).

---

## Features

- Enter how many characters you want (any number >= 1)
- Click **Generate** (or press **Enter**) to instantly create a password
- Password always contains uppercase, lowercase, digits, and symbols
- Strength indicator updates as you change the length
- **Copy** button copies the password to your clipboard with one click
- Fully dark-themed UI

---

## Requirements

| Requirement | Version |
|------------|---------|
| Python     | 3.8 or newer |
| Tkinter    | Included with Python on Windows |

> **No pip installs required.** Tkinter ships with the standard Python installer on Windows.

---

## How to Run

### 1. Make sure Python is installed

Open a terminal (PowerShell or Command Prompt) and run:

```
python --version
```

If you see `Python 3.x.x` you are good to go.
If not, download Python from https://www.python.org/downloads/ and install it (check "Add Python to PATH" during setup).

### 2. Navigate to the project folder

```
cd "c:\Users\Michał Iwan\Documents\2.1-generator-4tc-2-michal-i"
```

### 3. Run the app

```
python password_generator.py
```

A window will open immediately.

---

## Usage

1. Type the desired **number of characters** into the input box.
2. Click the **Generate** button (or press **Enter**).
3. Your new password appears in the display area at the top.
4. Click **Copy** to copy the password to your clipboard.

---

## Files

```
2.1-generator-4tc-2-michal-i/
├── password_generator.py   ← main application (run this)
└── README.md               ← this file
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` not recognised | Re-install Python and check "Add Python to PATH" |
| Window does not open | Ensure Tkinter is available: `python -m tkinter` should open a small test window |
| Text looks blurry | Right-click `password_generator.py` → Properties → Compatibility → "Override high DPI scaling behaviour" → Application |
