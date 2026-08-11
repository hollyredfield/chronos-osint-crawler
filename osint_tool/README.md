# ⌛ Chronos OSINT Crawler

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=for-the-badge&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/OSINT-Time--Machine-red?style=for-the-badge" alt="OSINT" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
</p>

<p align="center">
  <b>Because Wayback Machine's 404 is just a suggestion, not a fact.</b><br>
  <i>Excavating deleted URLs, hidden forum confessions, and historical web remnants since... well, whenever you need them.</i>
</p>

---

## 🧐 What is Chronos?

Ever encountered that soul-crushing message: *"The Wayback Machine has not archived that URL"*? Yeah, we hate it too. 

**Chronos OSINT Crawler** is a high-powered, asynchronous historical web recovery dashboard. When mainstream archives fail, Chronos deploys multi-thed OSINT dorking agents across **Common Crawl (WARC binaries)**, **DuckDuckGo Deep Scraping**, **HackerNews**, **GitHub Code Commits**, and **20+ historical Spanish & Global forums/blogs** (from ForoCoches to TuSecreto, Ask.fm, Tumblr, and old Blogspot rings).

It even renders a **headless Playwright sandbox preview** of rescued content so you don't have to risk visiting sketchy legacy sites directly.

---

## ⚡ Key Features

* 🕰️ **Bypass Wayback Limits:** Queries Common Crawl indices directly for raw WARC snapshots.
* 🕵️ **Text & URL Modes:** Don't have the exact link? Search by exact phrases, forum th titles, or taboo keywords.
* 💬 **Multi-Forum OSINT Engine:** Automatically targets 2010s goldmines:
  * **Confession Platforms:** *TuSecreto, Confesiones.com, SecretosAnónimos, NoLoDigan*
  * **Legacy Forums:** *ForoCoches, MediaVida, Taringa!, El Rincón del Vago, TodoExpertos*
  * **Micro-blogs & Networks:** *Ask.fm, Tumblr, Blogspot, WordPress, MetroFlog, Fotolog*
  * **Health & Psychology:** *Doctoralia, Psicología-Online, EnPlenitud*
* 📸 **Sandboxed Headless Previews:** Uses Playwright to screenshot and reconstruct found snapshots safely server-side.
* 🔗 **Auto-Generated Time Filters:** Generates direct Google/Yahoo/Bing dork strings scoped strictly to your selected year (`after:YYYY-01-01 before:YYYY-12-31`).

---

## 🛠️ Tech Stack

* **Backend:** Python 3.12, FastAPI, Uvicorn (Asynchronous API core)
* **Scrapers & Engines:** `ddgs` (DuckDuckGo API wrapper), `httpx`, `BeautifulSoup4`
* **Headless Renderer:** `Playwright` (Chromium engine)
* **Frontend:** HTML5, CSS3 Glassmorphism UI, Modern Vanilla JS

---

## 🚀 Quick Start

### 1. Prerequisites

Make sure you have Python 3.10+ installed.

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/chronos-osint-crawler.git
cd chronos-osint-crawler

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
python -m playwright install chromium
```

### 3. Run the Engine

```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

---

## 📂 Project Structure

```
osint_tool/
├── app.py                     # FastAPI application entrypoint
├── scrapers/
│   ├── common_crawl.py        # Common Crawl WARC index query engine
│   ├── search_engines.py      # DDGS & Multi-site OSINT Dorking module
│   └── github_reddit.py       # HackerNews & GitHub API connector
├── utils/
│   └── preview_generator.py   # Headless Playwright renderer
├── static/
│   ├── index.html             # Glassmorphism Dashboard
│   ├── style.css              # Cyber-dark OSINT styling
│   └── app.js                 # Frontend API handler
├── requirements.txt           # Python dependencies
└── ME.md                  # You are here!
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 

Got a new legacy forum or obscure confession platform from 2012 that needs dorking? 
1. **Fork** the project.
2. Create your feature branch (`git checkout -b feature/awesome-dork`).
3. Commit your changes (`git commit -m 'Add support for OldForumX'`).
4. Push to the branch (`git push origin feature/awesome-dork`).
5. Open a **Pull Request**.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

<p align="center">
  Made with ☕ and a deep obsession with uncovering forgotten web history.
</p>
