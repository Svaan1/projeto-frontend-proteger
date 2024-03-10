from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine(
    'postgresql+psycopg2://postgres:123@localhost:5433/proteger')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables(_args=None):
    """
    Creates the tables specified in src.db.models

    Args:
        _args: Arguments parsed from the command line when used from the cli
    """
    # Needed for the models to be discovered
    from src.db.models import User  # noqa F401

    print(f"Creating database at: {engine.url}")
    Base.metadata.create_all(bind=engine)


def get_session():
    with SessionLocal() as s:
        yield s
