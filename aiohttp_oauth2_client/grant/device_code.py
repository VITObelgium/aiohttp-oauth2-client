import asyncio
import time
from typing import Optional, Union
from yarl import URL

from aiohttp_oauth2_client.grant.common import OAuth2Grant
from aiohttp_oauth2_client.models.errors import OAuth2Error, AuthError
from aiohttp_oauth2_client.models.request import (
    DeviceAuthorizationRequest,
    DeviceAccessTokenRequest,
    DeviceAuthorizationRequestPKCE,
)
from aiohttp_oauth2_client.models.response import DeviceAuthorizationResponse
from aiohttp_oauth2_client.models.token import Token
from aiohttp_oauth2_client.pkce import PKCE


class DeviceCodeGrant(OAuth2Grant):
    def __init__(
        self,
        token_url: Union[str, URL],
        authorization_url: Union[str, URL],
        client_id: str,
        token: Optional[dict] = None,
        pkce: bool = False,
        **kwargs,
    ):
        super().__init__(token_url, token, **kwargs)
        self.authorization_url = URL(authorization_url)
        self.client_id = client_id
        self.pkce = PKCE() if pkce else None

    async def _fetch_token(self) -> Token:
        time_start = time.time()
        device_code_url = self.authorization_url / "device"

        if self.pkce:
            authorization_request = DeviceAuthorizationRequestPKCE(
                client_id=self.client_id,
                code_challenge=self.pkce.code_challenge,
                code_challenge_method=self.pkce.code_challenge_method,
                **self.kwargs,
            )
        else:
            authorization_request = DeviceAuthorizationRequest(
                client_id=self.client_id, **self.kwargs
            )

        async with self.session.post(
            url=device_code_url,
            data=authorization_request.model_dump(exclude_none=True),
        ) as response:
            response.raise_for_status()
            device_authorization = DeviceAuthorizationResponse.model_validate(
                await response.json()
            )
        token_request = DeviceAccessTokenRequest(
            device_code=device_authorization.device_code,
            client_id=self.client_id,
            **self.kwargs,
        )
        if self.pkce:
            token_request.code_verifier = str(self.pkce.code_verifier, "utf-8")

        _txt = (
            f"Visit {device_authorization.verification_uri_complete} to authenticate"
            if device_authorization.verification_uri_complete
            else f"Visit {device_authorization.verification_uri} and enter code {device_authorization.user_code} to authenticate."
        )
        print(_txt)

        while not time.time() > time_start + device_authorization.expires_in:
            await asyncio.sleep(device_authorization.interval)
            try:
                token = await self.execute_token_request(token_request)
                return token
            except OAuth2Error as e:
                if e.response.error == "authorization_pending":
                    pass
                elif e.response.error == "slow_down":
                    device_authorization.interval += 5
                else:
                    raise e
        raise AuthError("The device code has expired.")
