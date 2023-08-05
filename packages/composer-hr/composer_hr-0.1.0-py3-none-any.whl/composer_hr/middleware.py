from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware


middleware = [
    Middleware(SessionMiddleware, ),
]