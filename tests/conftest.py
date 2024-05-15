import pytest
from aioresponses import aioresponses

from aiohttp_oauth2_client.client import OAuth2Client
from .constants import TEST_URL, TOKENS


@pytest.fixture
def mock_token(request) -> dict:
    marker_refresh_token = request.node.get_closest_marker("refresh_token")
    refresh_token = marker_refresh_token.args[0] if marker_refresh_token else True
    token = TOKENS[0].copy()
    if not refresh_token:
        token.pop("refresh_token")
        token.pop("refresh_expires_in")
    return token


@pytest.fixture
def mock_token2(request) -> dict:
    marker_refresh_token = request.node.get_closest_marker("refresh_token")
    refresh_token = marker_refresh_token.args[0] if marker_refresh_token else True
    token = TOKENS[1].copy()
    if not refresh_token:
        token.pop("refresh_token")
        token.pop("refresh_expires_in")
    return token


@pytest.fixture
async def mock_responses() -> aioresponses:
    with aioresponses() as mock:
        yield mock


async def assert_request_with_access_token(
    client: OAuth2Client, token: dict, responses: aioresponses
):
    # add mock response
    responses.get(TEST_URL, status=200, body="Hello!")
    response = await client.get(TEST_URL)
    assert response.status == 200

    responses.assert_called_with(
        url=TEST_URL,
        method="GET",
        headers={"Authorization": f"Bearer {token['access_token']}"},
    )
