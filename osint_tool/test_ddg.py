import asyncio, httpx
from bs4 import BeautifulSoup

async def test():
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            'https://html.duckduckgo.com/html/', 
            data={'q':'enamorado de mi hermana 2014'}, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        print(f"Status: {resp.status_code}")
        soup = BeautifulSoup(resp.text, 'html.parser')
        results = soup.find_all('a', class_='result__url')
        print(f"Found: {len(results)}")
        
if __name__ == "__main__":
    asyncio.run(test())
