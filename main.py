import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    auth_router,
    cafe_locations_router,
    cities_router,
    order_router,
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
app.include_router(order_router.router)

origins = [
    "http://localhost:8000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
