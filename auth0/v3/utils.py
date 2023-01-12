import sys


def is_async_available():
    if sys.version_info >= (3, 6):
        try:
            import asyncio

            import aiohttp

            return True
        except ImportError:  # pragma: no cover
            pass

    return False
