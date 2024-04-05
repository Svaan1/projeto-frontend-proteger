from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from os import getenv

Base = declarative_base()
url_object = URL.create(
    drivername='postgresql+psycopg2',
    host=getenv('DATABASE_HOST'),
    username=getenv('DATABASE_USER'),
    password=getenv('DATABASE_PASSWORD'),
    database=getenv('DATABASE_NAME')
)
engine = create_engine(url_object)
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