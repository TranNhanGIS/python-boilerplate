"""
config.py

This module initializes and configures application settings using the Pydantic `BaseSettings` class.
It supports environment-specific configurations via `.env` files
Enhances debugging output with `rich`-styled tracebacks.
"""

import os
from pydantic_settings import BaseSettings
from rich.traceback import install as rich_installer

rich_installer()
# pylint: disable=R0903


class Settings(BaseSettings):
    """
    Manages application settings
    """

    debug: bool = False
    database_url: str = ""

    class Config:
        """
        Loading configurations from environment variables
        """

        env_file = f".env.{os.getenv('ENVIRONMENT', 'dev')}"
        env_file_encoding = "utf-8"


settings = Settings()
