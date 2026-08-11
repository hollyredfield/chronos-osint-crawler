from ddgs import DDGS
import urllib.parse
import asyncio

TARGET_SITES = [
    ("ForoCoches", "site:forocoches.com"),
    ("TuSecreto", "site:tusecreto.com"),
    ("MediaVida", "site:mediavida.com"),
    ("Taringa", "site:taringa.net"),
    ("Ask.fm", "site:ask.fm"),
    ("Tumblr", "site:tumblr.com"),
    ("Blogspot", "site:blogspot.com"),
    ("WordPress", "site:wordpress.com"),
    ("Doctoralia", "site:doctoralia.es"),
    ("Psicología Online", "site:psicologia-online.com"),
    ("20Minutos", "site:20minutos.es"),
    ("TodoExpertos", "site:todoexpertos.com"),
]

def run_ddgs_query(query, site_name, target_date):
    results = []
    try:
        ddgs = DDGS()
        raw_results = list(ddgs.text(query, max_results=10))
        for item in raw_results:
            results.append({
                "source": f"DuckDuckGo [{site_name}]" if site_name != "Búsqueda Libre Global" else "DuckDuckGo Global",
                "type": "mention",
                "url": item.get("href", "#"),
                "description": f"{item.get('title', '')}: {item.get('body', '')}",
                "timestamp": target_date
            })
    except Exception as e:
        print(f"Error DDGS {site_name}: {e}")
    return results

async def search_duckduckgo(url: str, target_date: str) -> list:
    results = []
    year = target_date[:4] if target_date else "2014"
    seen_urls = set()
    
    loop = asyncio.get_event_loop()
    tasks = []
    
    # 1. Búsqueda Libre Global
    q_global = f'"{url}"' if (url.startswith("http://") or url.startswith("https://")) else url
    tasks.append(loop.run_in_executor(None, run_ddgs_query, q_global, "Búsqueda Libre Global", target_date))
            
    # 2. Búsquedas por sitios específicos lanzadas en PARALELO
    if not (url.startswith("http://") or url.startswith("https://")):
        for site_name, site_dork in TARGET_SITES:
            query = f"{url} {site_dork}"
            tasks.append(loop.run_in_executor(None, run_ddgs_query, query, site_name, target_date))

    # Esperar a que terminen todas las búsquedas en paralelo
    all_site_results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for res_list in all_site_results:
        if isinstance(res_list, list):
            for item in res_list:
                if item["url"] not in seen_urls:
                    seen_urls.add(item["url"])
                    results.append(item)

    # 3. Enlaces directos a Google / Yahoo dorks con filtrado por año
    encoded_term = urllib.parse.quote(url)
    results.append({
        "source": f"Google Dorking {year} (Abrir en Google)",
        "type": "dork_link",
        "url": f"https://www.google.com/search?q={encoded_term}+after:{year}-01-01+before:{year}-12-31",
        "description": f"🔍 Búsqueda filtrada exactamente en Google para el año {year}.",
        "timestamp": target_date
    })
    results.append({
        "source": f"Yahoo Search {year} (Abrir en Yahoo)",
        "type": "dork_link",
        "url": f"https://search.yahoo.com/search?p={encoded_term}+{year}",
        "description": f"🔍 Búsqueda filtrada en Yahoo para el periodo {year}.",
        "timestamp": target_date
    })
    
    return results
