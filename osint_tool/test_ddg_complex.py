import asyncio, httpx
from bs4 import BeautifulSoup

async def test():
    async with httpx.AsyncClient() as client:
        # Simple query
        resp1 = await client.post('https://html.duckduckgo.com/html/', data={'q':'enamorado de mi hermana 2014'}, headers={'User-Agent': 'Mozilla/5.0'})
        soup1 = BeautifulSoup(resp1.text, 'html.parser')
        print('Simple query count:', len(soup1.find_all('a', class_='result__url')))
        
        # Complex query with OR and site:
        resp2 = await client.post('https://html.duckduckgo.com/html/', data={'q':'enamorado de mi hermana site:forocoches.com'}, headers={'User-Agent': 'Mozilla/5.0'})
        soup2 = BeautifulSoup(resp2.text, 'html.parser')
        print('Site query count:', len(soup2.find_all('a', class_='result__url')))

if __name__ == '__main__':
    asyncio.run(test())
