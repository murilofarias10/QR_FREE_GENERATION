# ⬛ QR Free Generation

A QR code generator, no API keys, no external services, no database — just run and go.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

---

## ✨ Features

- Generate QR codes for any **text or URL** instantly
- Choose **size** (64 px → 1024 px)
- Set **error correction level** (L / M / Q / H)
- Pick custom **foreground & background colors**
- **Download** as PNG or **copy** to clipboard
- Fully client-side rendering — zero server-side QR processing
- Dark, modern UI — no frameworks, no build step

---

## 📁 Project Structure

```
QR_FREE_GENERATION/
├── qr_app.py           # Flask entry point
├── requirements.txt    # Dependencies (Flask only)
└── templates/
    └── qr_generator.html   # Full UI + QR logic (qrcode.js via CDN)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/QR_FREE_GENERATION.git
cd QR_FREE_GENERATION
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
py qr_app.py
```

Open your browser at → **http://127.0.0.1:7011**

---

## 🛠 Tech Stack

| Layer      | Technology                                          |
|------------|-----------------------------------------------------|
| Backend    | [Flask](https://flask.palletsprojects.com/) (Python)|
| QR Engine  | [qrcode.js](https://github.com/davidshimjs/qrcodejs) (CDN, client-side) |
| Styling    | Vanilla CSS — dark glassmorphism theme              |
| Fonts      | [Inter](https://fonts.google.com/specimen/Inter) via Google Fonts |

---

## 📦 Dependencies

```
flask
```

That's it. The QR code generation happens entirely in the browser via `qrcode.js` — no Python QR library needed.

---

## 📄 License

MIT — free to use, modify, and distribute.
