from passlib.context import CryptContext
from fastapi import Request
from starlette.datastructures import URL
crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from graphql import GraphQLError

def hashed_verify(plain_text, hashed_text) -> bool:
    return crypt_context.verify(plain_text, hashed_text)
def hash_make(plain_text):
    return crypt_context.hash(plain_text)
def request_url(request: Request, graphql_app, url: str = 'graphql'):
    request._url = URL(url)
    return graphql_app.handle_graphql(request=request)
def req_auth(request: Request, graphql_app, auth):
    request.state.auth = auth
    return graphql_app.handle_graphql(request=request)

def require_auth(func):
    def wrap(*args, **kwargs):
        _, info = args
        if "request" in info.context and info.context["request"].state.auth:
            auth = info.context["request"].state.auth
            kwargs["auth"] = auth
            return func(*args, **kwargs)
        raise GraphQLError('authenticate required')