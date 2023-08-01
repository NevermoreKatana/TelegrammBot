from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.database_models import Base

PG_USER = os.environ["PG_USER"]
PG_PASSWORD = os.environ["PG_PASSWORD"]
PG_DATABASE = os.environ["PG_DATABASE"]
PG_HOST = os.environ["PG_HOST"]



engine = create_engine(f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DATABASE}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
