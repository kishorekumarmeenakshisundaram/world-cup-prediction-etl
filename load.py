import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def create_postgres_engine():
    load_dotenv()

    db_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=int(os.getenv("POSTGRES_PORT")),
        database=os.getenv("POSTGRES_DB")
    )
    engine = create_engine(db_url)
    return engine

def load_to_postgres(df,table_name="team_strength_predictions"):
    engine=create_postgres_engine()

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{len(df)} rows loaded into {table_name}")