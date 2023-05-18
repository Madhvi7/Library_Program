import uvicorn as uvicorn
from fastapi import FastAPI

from Script.core.Services.Library_service import book_router

app = FastAPI()
app.include_router(book_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
