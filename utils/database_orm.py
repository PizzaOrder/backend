from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin@localhost:5432/PizzaOrder"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
