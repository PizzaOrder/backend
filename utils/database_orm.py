from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin:root@localhost:5432/PizzaOrder"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
