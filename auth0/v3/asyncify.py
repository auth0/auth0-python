import aiohttp

from auth0.v3.rest_async import AsyncRestClient


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
                super(AsyncClient, self).__init__(domain, telemetry, timeout, protocol)
            else:
                # Wrap the mngtmt client
                super(AsyncClient, self).__init__(
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
                super(Wrapper, self).__init__(domain, telemetry, timeout, protocol)
            else:
                # Wrap the mngtmt client
                super(Wrapper, self).__init__(
                    domain, token, telemetry, timeout, protocol, rest_options
                )

            self._async_client = AsyncClient(
                domain, token, telemetry, timeout, protocol, rest_options
            )
            for method in methods:
                setattr(
                    self,
                    "{}_async".format(method),
                    _gen_async(self._async_client, method),
                )

        async def __aenter__(self):
            """Automatically create and set session within context manager."""
            async_rest_client = self._async_client.client
            self._session = aiohttp.ClientSession()
            async_rest_client.set_session(self._session)
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            """Automatically close session within context manager."""
            await self._session.close()

    return Wrapper
