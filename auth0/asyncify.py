import aiohttp

from auth0.rest_async import AsyncRestClient


def _gen_async(client, method):
    m = getattr(client, method)

    async def closure(*args, **kwargs):
        return await m(*args, **kwargs)

    return closure


def asyncify(cls):
    methods = [
        func
        for func in dir(cls)
        if callable(getattr(cls, func)) and not func.startswith("_")
    ]

    class AsyncClient(cls):
        def __init__(
            self,
            domain,
            token,
            telemetry=True,
            timeout=5.0,
            protocol="https",
            rest_options=None,
        ):
            if token is None:
                # Wrap the auth client
                super().__init__(domain, telemetry, timeout, protocol)
            else:
                # Wrap the mngtmt client
                super().__init__(
                    domain, token, telemetry, timeout, protocol, rest_options
                )
            self.client = AsyncRestClient(
                jwt=token, telemetry=telemetry, timeout=timeout, options=rest_options
            )

    class Wrapper(cls):
        def __init__(
            self,
            domain,
            token=None,
            telemetry=True,
            timeout=5.0,
            protocol="https",
            rest_options=None,
        ):
            if token is None:
                # Wrap the auth client
                super().__init__(domain, telemetry, timeout, protocol)
            else:
                # Wrap the mngtmt client
                super().__init__(
                    domain, token, telemetry, timeout, protocol, rest_options
                )

            self._async_client = AsyncClient(
                domain, token, telemetry, timeout, protocol, rest_options
            )
            for method in methods:
                setattr(
                    self,
                    f"{method}_async",
                    _gen_async(self._async_client, method),
                )

        def set_session(self, session):
            """Set Client Session to improve performance by reusing session.

            Args:
                session (aiohttp.ClientSession): The client session which should be closed
                    manually or within context manager.
            """
            self._session = session
            self._async_client.client.set_session(self._session)

        async def __aenter__(self):
            """Automatically create and set session within context manager."""
            self.set_session(aiohttp.ClientSession())
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            """Automatically close session within context manager."""
            await self._session.close()

    return Wrapper
