from aiohttp import ClientSession

__all__ = ("request",)

async def request(
    endpoint: str,
    *,
    authorisation_token: str,
) -> dict:
    async with ClientSession() as session:
        session.headers.add("Token", authorisation_token)
        session.headers.add("Content-Type", "application/json")
        async with session.request(
            "GET",
            "https://developer.sepush.co.za/business/2.0" + endpoint,
        ) as request:
            return await request.json()