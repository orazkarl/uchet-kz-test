import secrets
from typing import Optional, List, Union, Dict, Any

from pydantic import BaseSettings, PostgresDsn, AnyHttpUrl, validator
from pydantic.env_settings import DotenvType


class Settings(BaseSettings):
    PROJECT_NAME: str = "UCHET.KZ"
    DEBUG = True
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    AWS_ACCESS_KEY_ID: str = 'AKIASWS6LY5OWNZXB7SL'
    AWS_SECRET_ACCESS_KEY: str = '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'
    AWS_REGION: str = 'eu-north-1'
    S3_BUCKET: str = 'orazkarl'
    S3_KEY: str = 'SSE-S3'

    class Config:
        env_file: Optional[DotenvType] = "./.env"


settings = Settings()
