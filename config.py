from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv(".env")
load_dotenv(".ENV")


@dataclass(frozen=True)
class Settings:
    api_key: str | None = os.getenv("api_key")
    azure_endpoint: str | None = os.getenv("azure_endpoint")
    azure_key: str | None = os.getenv("azure_key")
    dbname: str | None = os.getenv("dbname")
    db_user: str | None = os.getenv("user")
    db_password: str | None = os.getenv("password")
    db_host: str | None = os.getenv("host")
    db_port: str | None = os.getenv("port")
    ocr_poll_timeout_seconds: int = int(os.getenv("OCR_POLL_TIMEOUT_SECONDS", "30"))
    ocr_request_timeout_seconds: int = int(os.getenv("OCR_REQUEST_TIMEOUT_SECONDS", "10"))
    max_upload_bytes: int = int(os.getenv("MAX_UPLOAD_BYTES", str(10 * 1024 * 1024)))

    def require_api_key(self) -> str:
        if not self.api_key:
            raise RuntimeError("API key is not configured")
        return self.api_key

    def require_azure(self) -> tuple[str, str]:
        if not self.azure_endpoint or not self.azure_key:
            raise RuntimeError("Azure OCR configuration is incomplete")
        return self.azure_endpoint.rstrip("/"), self.azure_key

    def require_database(self) -> dict[str, str | None]:
        values = {
            "dbname": self.dbname,
            "user": self.db_user,
            "password": self.db_password,
            "host": self.db_host,
            "port": self.db_port,
        }
        missing = [key for key, value in values.items() if not value]
        if missing:
            raise RuntimeError(f"Database configuration is incomplete: {', '.join(missing)}")
        return values


settings = Settings()
