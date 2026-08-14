import pandas as pd

from db_connection import engine


DATA_PATH = "data/processed/cleaned_superstore.csv"


# Load cleaned data
df = pd.read_csv(DATA_PATH)

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="mixed"
)

print(f"Loaded {len(df)} rows from CSV")

print(df[["Order Date", "Ship Date"]].dtypes)


# Upload data to PostgreSQL
df.to_sql(
    "orders",
    con=engine,
    schema="public",
    if_exists="replace",
    index=False
)

print("Data successfully loaded into PostgreSQL!")