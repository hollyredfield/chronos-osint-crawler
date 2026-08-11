import httpx
import urllib.parse

async def search_social(url: str, target_date: str) -> list:
    """
    Busca menciones de la URL en GitHub y HackerNews.
    (Reddit Pushshift está mayormente desactivado, por lo que usamos HackerNews como proxy de comunidad).
    """
    results = []
    
    # 1. HackerNews (Algolia API)
    hn_url = "https://hn.algolia.com/api/v1/search"
    # Buscamos la URL
    params = {
        "query": url,
        "hitsPerPage": 10
    }
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(hn_url, params=params)
            if response.status_code == 200:
                data = response.json()
                for hit in data.get("hits", []):
                    created_at = hit.get("created_at", "")
                    if target_date[:4] in created_at:
                        results.append({
                            "source": "HackerNews",
                            "type": "forum",
                            "url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                            "description": f"Mención en HN: {hit.get('title', 'Comentario')}",
                            "timestamp": created_at
                        })
    except Exception as e:
        print(f"Error en HackerNews: {e}")
        
    # 2. GitHub API (Code Search)
    # Si es una URL, extraemos el dominio. Si es texto, lo usamos directo.
    if url.startswith("http://") or url.startswith("https://") or "/" in url:
        domain = urllib.parse.urlparse(url).netloc or url
        gh_query = f"{domain} in:file"
    else:
        gh_query = f"{url} in:file"

    gh_url = "https://api.github.com/search/code"
    gh_params = {
        "q": gh_query
    }
    gh_headers = {
        "User-Agent": "Chronos-OSINT-Crawler",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(gh_url, params=gh_params, headers=gh_headers)
            if response.status_code == 200:
                data = response.json()
                for item in data.get("items", [])[:5]: # limit to 5
                    results.append({
                        "source": "GitHub",
                        "type": "code",
                        "url": item.get("html_url"),
                        "description": f"Encontrado en repo: {item.get('repository', {}).get('full_name')} - Archivo: {item.get('name')}",
                        "timestamp": "N/A"
                    })
    except Exception as e:
        print(f"Error en GitHub: {e}")
        
    return results
