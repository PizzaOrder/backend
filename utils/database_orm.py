from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URL = settings.database_dsn_psycopg2

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
