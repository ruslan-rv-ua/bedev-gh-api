import uvicorn
from fastapi import FastAPI

from .endpoints import router
from .settings import settings

app = FastAPI(title="bedev-gh-api")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
