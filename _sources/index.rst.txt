.. aiohttp-oauth2-client documentation master file, created by
   sphinx-quickstart on Tue May 21 16:32:43 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``aiohttp-oauth2-client``: OAuth2 support for ``aiohttp`` client
================================================================
This package adds support for OAuth 2.0 authorization to the :obj:`~aiohttp.ClientSession` class of the ``aiohttp`` library.
It handles retrieving access tokens and injects them in the *Authorization* header of HTTP requests as a Bearer token.

**Features**:

* Ease of use
* Supported OAuth2 grants:

  * `Resource Owner Password Credentials <https://datatracker.ietf.org/doc/html/rfc6749#section-4.3>`_
  * `Client Credentials <https://datatracker.ietf.org/doc/html/rfc6749#section-4.4>`_
  * `Authorization Code (+ PKCE) <https://datatracker.ietf.org/doc/html/rfc6749#section-4.1>`_
  * `Device Code (+ PKCE) <https://datatracker.ietf.org/doc/html/rfc8628>`_
* Automatic (lazy) refresh of tokens
* Extensible code architecture

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
