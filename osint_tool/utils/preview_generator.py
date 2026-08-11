import os
from playwright.async_api import async_playwright
import time

async def generate_preview(url: str) -> str:
    """
    Renderiza la URL (que puede ser un snapshot de Common Crawl o un caché) 
    y genera una captura de pantalla completa para evitar que el usuario tenga que entrar.
    """
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page(
                viewport={'width': 1280, 'height': 800},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )
            
            # Navegar a la URL
            await page.goto(url, timeout=30000, wait_until="domcontentloaded")
            
            # Opcional: Esperar a que se carguen algunas imágenes
            await page.wait_for_timeout(2000)
            
            # Guardar screenshot
            filename = f"preview_{int(time.time())}.png"
            filepath = os.path.join("static", filename)
            
            await page.screenshot(path=filepath, full_page=True)
            await browser.close()
            
            return f"/static/{filename}"
    except Exception as e:
        print(f"Error generando preview con Playwright: {e}")
        return None
