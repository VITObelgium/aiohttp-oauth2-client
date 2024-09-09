Usage
=====

Getting started
---------------

Begin by importing the relevant modules, like the OAuth2 client and grant. Also import ``asyncio`` for running async code::

    import asyncio
    from aiohttp_oauth2_client.client import OAuth2Client
    from aiohttp_oauth2_client.grant.device_code import DeviceCodeGrant


Then create an :obj:`~aiohttp_oauth2_client.grant.common.OAuth2Grant` and :obj:`~aiohttp_oauth2_client.client.OAuth2Client` object and perform a HTTP request to a protected resource. We use the
Device Code grant in this example::

    async def main():
        async with DeviceCodeGrant(
                token_url=TOKEN_URL,
                device_authorization_url=DEVICE_AUTHORIZATION_URL,
                client_id=CLIENT_ID,
                pkce=True
        ) as grant, OAuth2Client(grant) as client:
            async with client.get(PROTECTED_ENDPOINT) as response:
                assert response.ok
                print(await response.text())


    asyncio.run(main())


The client and grant objects can be used as async context managers. This ensures the proper setup and cleanup of
associated resources.


Grant configuration
-------------------
Each grant type has specific configuration options associated with it.
Extra parameters can be provided, which will then be used in the authorization process.

* :obj:`~aiohttp_oauth2_client.grant.authorization_code.AuthorizationCodeGrant`
* :obj:`~aiohttp_oauth2_client.grant.client_credentials.ClientCredentialsGrant`
* :obj:`~aiohttp_oauth2_client.grant.resource_owner_password_credentials.ResourceOwnerPasswordCredentialsGrant`
* :obj:`~aiohttp_oauth2_client.grant.device_code.DeviceCodeGrant`

