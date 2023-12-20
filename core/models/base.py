from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

    def __repr__(self):
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"<{self.__class__.__name__} {', '.join(cols)}"
