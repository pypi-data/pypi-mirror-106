# <p align="center">AioTraceMoeAPI

<p align="center">A simple, but extensible Python implementation for the trace.moe API.


  * [Getting started.](#getting-started)
  * [Writing your first code](#writing-your-first-comments-bot)

## Getting started.
install from PyPi
```
$ python -m pip install aiotracemoeapi
```

## Writing your first code
```python
import os.path
import asyncio

from aiotracemoeapi import TraceMoe

api = TraceMoe()
# or api = TraceMoe(token="ABC")


async def search_anime(path):
    post = await bot.create_post('text', text=text, parse_mode='HTML')
    print(post.link)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(search_anime(""))
```
