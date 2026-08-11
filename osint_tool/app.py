import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional

# Importar scrapers (se implementarán más adelante)
from scrapers.common_crawl import search_common_crawl
from scrapers.search_engines import search_duckduckgo
from scrapers.github_reddit import search_social
from utils.preview_generator import generate_preview

app = FastAPI(title="Chronos OSINT Crawler")

# Montar archivos estáticos para el frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

class SearchRequest(BaseModel):
    url: str
    target_date: str  # YYYY o YYYY-MM-DD
    modules: List[str]  # e.g., ["common_crawl", "search_engines", "social"]

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/api/search")
async def perform_search(request: SearchRequest):
    results = []
    
    # Ejecutar módulos en paralelo
    tasks = []
    if "common_crawl" in request.modules:
        tasks.append(search_common_crawl(request.url, request.target_date))
    if "search_engines" in request.modules:
        tasks.append(search_duckduckgo(request.url, request.target_date))
    if "social" in request.modules:
        tasks.append(search_social(request.url, request.target_date))
    
    # Esperar a que terminen todas las búsquedas
    gathered_results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for res in gathered_results:
        if isinstance(res, list):
            results.extend(res)
        elif isinstance(res, Exception):
            print(f"Error en módulo: {res}")
            
    # Intentar generar una preview si encontramos un HTML completo o un snapshot URL
    preview_url = None
    for res in results:
        if res.get("type") == "snapshot" and res.get("snapshot_url"):
            preview_url = await generate_preview(res["snapshot_url"])
            break
            
    return {
        "status": "success",
        "total_results": len(results),
        "data": results,
        "preview_image": preview_url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
