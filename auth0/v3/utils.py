import sys


def is_async_available():
    if sys.version_info >= (3, 6):
        try:
            import asyncio

            import aiohttp
            import async_timeout

            return True
        except ImportError:
            pass

    return False
