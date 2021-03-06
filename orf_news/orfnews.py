import aiohttp
from errors import Empty
from lxml import html

async def news(category, count = None):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://orf.at") as r:
            data = await r.read()
            tree = html.fromstring(data)
            news = tree.xpath(f"//div[@class='ticker-ressort {category}']//*[@class='ticker-story-headline']//a/text()")
            
            news_list = []
            for i in news[:count]:
                news_list.append(i.strip())

    if news == [] or news == "":
        raise Empty("No matches found for category.")

    return news_list
