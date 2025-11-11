from pydantic_settings import BaseSettings, SettingsConfigDict

from project.core.constants import BASE_DIR


class Settings(BaseSettings):
    # Backend
    debug: bool = False
    secret_key: str
    sqlalchemy_record_queries: bool  # для отображения SQL-запросов в flask-debug-toolbar

    # Database
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    @property
    def postgresql_url(self) -> str:
        return (
            f'postgresql://'
            f'{self.postgres_user}:'
            f'{self.postgres_password}@'
            f'{self.postgres_host}:'
            f'{self.postgres_port}/'
            f'{self.postgres_db}'
        )

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


config: Settings = Settings()
