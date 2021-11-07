# ORF-News #

Online ORF News Wrapper

[My Discord](https://discordapp.com/users/731128007388823592/ "Moritz⚜#6969")

## Instructions ##

### Install: ###

```py
pip install orf-news
```

### Information: ###

```py
news() takes one required and one optional argument
news([HEADLINE], [LIMIT])
HEADLINE = str
LIMIT = int
```

### Run Program: ###

```py
# import orfnews and asyncio
import asyncio
from orf_news import orfnews

# make def
async def bread():
    output = await orfnews.news("ausland", 2)
    print(output)

# run def
asyncio.run(bread())
```

### OUTPUT: ###
```py
# with 2 posts
["post1", "post2"]
# without n posts limitation
["post1", "post2", ....., "postn"]
```

## Ride the space skyway home to 80s Miami ##
