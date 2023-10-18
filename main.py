import uvicorn
from fastapi import Depends, FastAPI
from routers import pizza_router
from utils.get_db import get_db

app = FastAPI()
app.include_router(pizza_router.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
