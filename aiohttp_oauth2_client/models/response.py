from typing import Optional

from pydantic import BaseModel


class DeviceAuthorizationResponse(BaseModel):
    """
    The Device Authorization Response model.

    https://datatracker.ietf.org/doc/html/rfc8628#section-3.2

    :ivar device_code: The device verification code.
    :ivar user_code: The end-user verification code.
    :ivar verification_uri: The end-user verification URI on the authorization server.
    :ivar verification_uri_complete: A verification URI that includes the "user_code" which is designed for non-textual transmission.
    :ivar expires_in: The lifetime in seconds of the "device_code" and "user_code".
    :ivar interval: The minimum amount of time in seconds that the client SHOULD wait between polling requests to the token endpoint.
    """

    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: Optional[str] = None
    expires_in: int
    interval: int = 5


class ErrorResponse(BaseModel):
    """
    OAuth2 Error Response model.

    https://datatracker.ietf.org/doc/html/rfc6749#section-5.2

    :ivar error: A single ASCII error code.
    :ivar error_description: Human-readable ASCII text providing additional information, used to assist the client developer in understanding the error that occurred.
    :ivar error_uri: A URI identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error.
    """

    error: str
    error_description: Optional[str] = None
    error_uri: Optional[str] = None
