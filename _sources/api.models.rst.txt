Models
======

The **models** package contains several data models and exceptions that are internally used throughout the code.
End-users shouldn't have to deal with these classes, except for error handling.


Errors
------

All exceptions raised in the `aiohttp-oauth2-client` package inherit from the :obj:`aiohttp_oauth2_client.models.errors.AuthError` exception.
This can be useful for catching auth errors in your code.

.. automodule:: aiohttp_oauth2_client.models.errors
   :members:
   :undoc-members:
   :show-inheritance:

Grant types
-----------

.. automodule:: aiohttp_oauth2_client.models.grant
   :members:
   :undoc-members:
   :show-inheritance:

Proof Key for Code Exchange (PKCE)
----------------------------------

.. automodule:: aiohttp_oauth2_client.models.pkce
   :members:
   :undoc-members:
   :show-inheritance:

Request
---------------------------------------------

.. automodule:: aiohttp_oauth2_client.models.request
   :members:
   :undoc-members:
   :show-inheritance:

Response
----------------------------------------------

.. automodule:: aiohttp_oauth2_client.models.response
   :members:
   :undoc-members:
   :show-inheritance:

Token
-------------------------------------------

.. automodule:: aiohttp_oauth2_client.models.token
   :members:
   :undoc-members:
   :show-inheritance:
