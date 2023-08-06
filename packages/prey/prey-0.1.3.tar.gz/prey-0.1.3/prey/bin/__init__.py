#!/usr/bin/env python
import sys
import asyncio
from prey import x, cd


def main():
    from aiohttp_requests import requests
    import colorama

    colorama.init()

    globals()["x"] = x
    globals()["cd"] = cd
    globals()["request"] = requests.session.request
    globals()["colorama"] = colorama

    if len(sys.argv) == 1:
        print("usage: prey <script_file>")
        exit(2)

    filepath = sys.argv[1]

    script = None
    try:
        script = open(filepath).read()
    except FileNotFoundError:
        return print(f"No such file or directory: {filepath}")

    ldict = {}

    exec(script, globals(), ldict)

    loop = None
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()

    loop.run_until_complete(ldict["main"]())
