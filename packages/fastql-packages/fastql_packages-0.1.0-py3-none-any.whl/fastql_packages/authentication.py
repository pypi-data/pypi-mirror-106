from typing import Optional, Generic, TypeVar
from datetime import datetime, timedelta
from jose import ExpiredSignatureError, jwt, JWTError

class Auth:
    def __init__(self, configs):
        auth_config = configs['auth']
        self.default_auth = auth_config['default']
        self.provider = self.default_auth['provider']
        self.driver = self.provider['driver']

    def access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        self.plain_data = data.copy()
        plain_data = data.copy()
        if expires_delta:
            self.expire = datetime.utcnow() + expires_delta
        else:
            self.expire = datetime.utcnow() + timedelta(minutes=30)
        plain_data.update({"exp": self.expire, "ref": "token"})
        self.token_encoded = jwt.encode(plain_data, self.default_auth["secret_key"], algorithm=self.default_auth["algorithm"])

    def with_refresh_token(self):
        if self.token_encoded:
            plain_data = self.plain_data.copy()
            expire = self.expire + timedelta(minutes=10)
            plain_data.update({"exp": expire, "ref": "refresh"})
            self.refresh_token_encode = jwt.encode(plain_data, self.default_auth["secret_key"], algorithm=self.default_auth["algorithm"])

    def create(self):
        if self.token_encoded:
            jwt_token = {"token": self.token_encoded}
            if self.refresh_token_encode:
                jwt_token.update({"refresh": self.refresh_token_encode})
            return jwt_token
        return None
    