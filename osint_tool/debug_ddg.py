import asyncio, httpx
from bs4 import BeautifulSoup

async def debug_site():
    async with httpx.AsyncClient(follow_redirects=True) as client:
        resp = await client.post("https://html.duckduckgo.com/html/", data={"q": "enamorado de mi hermana site:forocoches.com"}, headers={"User-Agent": "Mozilla/5.0"})
        print("SITE SEARCH STATUS:", resp.status_code)
        soup = BeautifulSoup(resp.text, 'html.parser')
        urls = soup.find_all('a', class_='result__url')
        print("URLS FOUND:", len(urls))
        for u in urls:
            print("URL:", u.get('href'))

if __name__ == "__main__":
    asyncio.run(debug_site())
