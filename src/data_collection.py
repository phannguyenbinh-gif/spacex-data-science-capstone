"""SpaceX API collection example for the capstone."""
import requests
import pandas as pd

SPACEX_LAUNCHES_URL = "https://api.spacexdata.com/v4/launches/past"

def fetch_launches(url=SPACEX_LAUNCHES_URL):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return pd.json_normalize(response.json())

if __name__ == "__main__":
    df = fetch_launches()
    print(df.head())
    print("Rows:", len(df))
