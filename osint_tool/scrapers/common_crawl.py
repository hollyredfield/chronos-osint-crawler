import httpx
import json

async def search_common_crawl(url: str, target_date: str) -> list:
    """
    Busca en el índice de Common Crawl (Index Server) capturas históricas de la URL.
    La API de Common Crawl CDX es similar a la de Wayback Machine pero independiente.
    """
    results = []
    
    # Common Crawl requiere una URL para buscar en su índice. Si es una búsqueda de texto, avisamos.
    if not url.startswith("http://") and not url.startswith("https://") and "/" not in url:
        return [{
            "source": "Common Crawl",
            "type": "info",
            "url": "#",
            "description": "Common Crawl requiere una URL o dominio válido para buscar. Se ha omitido para esta búsqueda de texto.",
            "timestamp": "N/A"
        }]

    # Usamos un índice reciente para buscar en todo el historial disponible en ese índice.
    # En un entorno real, iteraríamos por múltiples índices. Usamos uno como ejemplo poderoso.
    index_url = "https://index.commoncrawl.org/CC-MAIN-2023-50-index"
    
    params = {
        "url": url,
        "output": "json"
    }
    
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(index_url, params=params)
            
            if response.status_code == 200:
                # Cada línea es un objeto JSON
                for line in response.text.strip().split('\n'):
                    if not line:
                        continue
                    data = json.loads(line)
                    timestamp = data.get("timestamp", "")
                    # Filtrar por el año o fecha que el usuario introdujo
                    if target_date.replace("-", "") in timestamp:
                        results.append({
                            "source": "Common Crawl",
                            "type": "snapshot",
                            "timestamp": timestamp,
                            "url": data.get("url"),
                            "status": data.get("status"),
                            # La URL directa al WARC o una pasarela que la lea
                            "snapshot_url": f"https://index.commoncrawl.org/CC-MAIN-2023-50-index?url={url}&output=json",
                            "description": "Captura en bruto encontrada en los archivos WARC de Common Crawl."
                        })
    except Exception as e:
        print(f"Error en Common Crawl: {e}")
        
    return results
