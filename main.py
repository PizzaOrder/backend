import uvicorn
from fastapi import FastAPI

from routers import (
    pizza_router,
    cities_router,
    promo_code_router,
    cafe_locations_router,
    users_router,
)

app = FastAPI()
app.include_router(pizza_router.router)
app.include_router(cities_router.router)
app.include_router(promo_code_router.router)
app.include_router(cafe_locations_router.router)
app.include_router(users_router.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
