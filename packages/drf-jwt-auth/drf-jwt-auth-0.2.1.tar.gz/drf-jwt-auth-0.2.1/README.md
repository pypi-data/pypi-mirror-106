# DRF JWT Auth

Django REST Framework JWT Authentication package enables to authenticate to Django REST Framework's API Views and ViewSets by using JWT (in header or as query param).

In difference with other packages, this package offers the following features:

- The user autheticated is based on the payload info, so **no user is loaded from database**.
- So that, the user model that you will find on every `request.user` will be an instance of `drfjwtauth.user.JWTUser`, a class that keeps the same API that `django.contrib.auth.models.User` but is not loaded from database and no write operations can be made over that user (due to it's not a model).
- Provides a view (in `drfjwtauth.views.VerifyJWTView`) to verify a token using a POST request.
- **NO login or token renew views are provided**

## Installation

```bash
$ pip install drf-jwt-auth
```

## Setup

### Authentication class

You can setup DRF JWT Auth as authentication class in two ways:

1) As default authentication class adding to the `DEFAULT_AUTHENTICATION_CLASSES` key in the the global DRF settings:

```python
REST_FRAMEWORK = {
    [...]
    'DEFAULT_AUTHENTICATION_CLASSES': ['...', 'drfjwtauth.auth.JWTAuth',  '...'],
    [...]
}
```

2) In every APIView/ViewSet/view function:

```python
from rest_framework.views import APIView
from drfjwtauth.auth import JWTAuth

class ExampleView(APIView):
    authentication_classes = [JWTAuth]

@authentication_classes([JWTAuth])
def example_view(request, format=None):
    [...]
```

### Token Verify View

In your project's `urls.py`:

```python
from django.urls import path

from drfjwtauth.views import VerifyJWTView

urlpatterns = [
    [...],
    path('token/verify/', VerifyJWTView.as_view(), name='token-verify')
    [...],
]
```

### Available settings and defaults

In your Django project's settings you can setup the following dict and keys:

```python
DRF_JWT_AUTH = {
    'ALGORITHM': JWT algorithm to sign tokens (HS256 by default).
    'SIGNING_KEY': Secret key to sign tokens (same value as Django SECRET_KEY settings by default).
    'AUTH_HEADER': Value before the token in the HTTP Authorization header (Bearer by default).
    'QUERY_PARAM_NAME': Value before the query param name for HTTP GET requests (jwt by default).
}
```
