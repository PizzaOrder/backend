import uvicorn
from fastapi import FastAPI

from routers import (
    auth_router,
    cafe_locations_router,
    cities_router,
    pizza_router,
    promo_code_router,
    users_router,
)

app = FastAPI()
app.include_router(pizza_router.router)
app.include_router(cities_router.router)
app.include_router(promo_code_router.router)
app.include_router(cafe_locations_router.router)
app.include_router(users_router.router)
app.include_router(auth_router.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
