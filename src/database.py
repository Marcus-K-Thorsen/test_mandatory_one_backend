import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from contextlib import contextmanager

load_dotenv()

# Define the SQLAlchemy base
Base = declarative_base()


# Configure database connection
def get_db_connection_string() -> str:
    """
    Creates a database engine using individual environment variables.
    """
    
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    connection_string = f'mysql+mysqldb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    return connection_string

# Session factory
# Create engine and session
def get_engine() -> Engine:
    connection_string = get_db_connection_string()
    engine = create_engine(connection_string)
    return engine

# Session factory
session_local = sessionmaker(autocommit=False, autoflush=False)

@contextmanager
def get_db() -> Session:
    engine = get_engine()
    session = session_local(bind=engine)

    try:
        yield session
    finally:
        session.close()

