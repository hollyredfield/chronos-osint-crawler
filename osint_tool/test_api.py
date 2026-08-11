import asyncio
from scrapers.search_engines import search_duckduckgo

async def main():
    res = await search_duckduckgo("enamorado de mi hermana", "2014")
    print(f"TOTAL RESULTADOS ENCONTRADOS: {len(res)}")
    for r in res:
        print(f"[{r['source']}] -> {r['url']}")

if __name__ == "__main__":
    asyncio.run(main())
