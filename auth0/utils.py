def is_async_available():
    try:
        import asyncio

        import aiohttp

        return True
    except ImportError:  # pragma: no cover
        pass

    return False
