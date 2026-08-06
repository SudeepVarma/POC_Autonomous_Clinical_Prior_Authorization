"""
This launches a Uvicorn ASGI web server to run a web application located at app.main:app, using dynamically configured host, port, and auto-reload settings imported from a central configuration file.

Created on: 2026-08-05
Author: Sudeep Varma K
"""

import uvicorn

from app.config import settings


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )