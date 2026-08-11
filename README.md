# Chronos OSINT Crawler 🚀

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="600" alt="Chronos animation"/>
</p>

<p align="center">
  <a href="https://github.com/your-username/chronos-osint-crawler/stargazers"><img src="https://img.shields.io/github/stars/your-username/chronos-osint-crawler?style=social" alt="Stars"/></a>
  <a href="https://github.com/your-username/chronos-osint-crawler/network/members"><img src="https://img.shields.io/github/forks/your-username/chronos-osint-crawler?style=social" alt="Forks"/></a>
  <a href="https://github.com/your-username/chronos-osint-crawler/issues"><img src="https://img.shields.io/github/issues/your-username/chronos-osint-crawler" alt="Issues"/></a>
  <a href="https://github.com/your-username/chronos-osint-crawler/blob/main/LICENSE"><img src="https://img.shields.io/github/license/your-username/chronos-osint-crawler" alt="License"/></a>
</p>

---

## 🎯 What the heck is this?

> *"The Wayback Machine says **404**? That's adorable. Let me dig deeper."
>
> – Every frustrated researcher ever.

**Chronos OSINT Crawler** is a *time‑travelling web‑scraper* that resurrects URLs, forum ths, and hidden confessions that vanished from conventional archives. In short, it’s **your personal time machine for the internet**.

- **⚡ Asynchronous FastAPI back‑end** – zero‑lag UI updates.
- **🕸️ Multi‑engine dorking** – Common Crawl, DuckDuckGo (via `ddgs`), Google, Yahoo, Bing, GitHub, HackerNews.
- **🧩 20+ historical Spanish‑language data sources** (ForoCoches, TuSecreto, Mediavida, Taringa, Ask.fm, Tumblr…)
- **📸 Headless Playwright preview** – safe screenshots of resurrected pages.
- **💅 Glass‑morphism UI** – because aesthetics matter even when you’re digging up ghost posts.

> *If you can’t find it on Wayback, it probably exists somewhere else. And we’ll find it.*

---

## ✨ Features (A.k.a. Super‑powers)

| Feature | Why it matters |
|--------|----------------|
| **Common‑Crawl WARC** | Raw snapshots of the web, straight from the archive, no 404 nonsense. |
| **DuckDuckGo `ddgs` wrapper** | Bypasses the 403/202 blocking you saw in the plain HTML approach. |
| **Dynamic year‑filter dorks** | `after:YYYY-01-01 before:YYYY-12-31` – get *exactly* what happened in that year. |
| **Live preview** | Playwright renders the page in a sandbox; you never have to click a shady link. |
| **Bookmarkable results** | Click‑through URLs, timestamps, source tags – y for reporting or further analysis. |
| **Modular scraper architecture** | Add a new forum in a single Python file and PR it. |

---

## 📦 Installation (Zero‑to‑hero in 3 commands)

```powershell
# 1️⃣ Clone the repo (or create a folder if you aly have it)
git clone https://github.com/your-username/chronos-osint-crawler.git
cd chronos-osint-crawler

# 2️⃣ Install Python deps (Python 3.10+ required)
python -m pip install -r requirements.txt

# 3️⃣ Install Playwright browsers (needed for the sandbox preview)
python -m playwright install chromium

# 4️⃣ Fire it up!
python app.py
```

Open <http://127.0.0.1:8000> and prepare to be amazed.

---

## 👩‍💻 Contributing (Because nobody does it alone)

1. **Fork** the repo.
2. Create a **feature branch**:
   ```powershell
   git checkout -b feature/add‑new‑forum‑X
   ```
3. Make your changes (add a new entry to `TARGET_SITES` in `search_engines.py`).
4. Write/tests – we have a tiny test suite using `pytest`. Run it with:
   ```powershell
   pytest
   ```
5. Commit and push:
   ```powershell
   git add .
   git commit -m "feat: support Forum X"
   git push origin feature/add‑new‑forum‑X
   ```
6. Open a **Pull Request** – we’ll review, merge, and probably give you a badge.

> **Pro‑tip:** If you need a new Python dependency, add it to `requirements.txt` and bump the version number.

---

## 📜 License

MIT – do whatever you want, just keep the credit.

---

<p align="center">
  Made with ☕, sarcasm, and a relentless curiosity for the internet’s lost souls.
</p>
