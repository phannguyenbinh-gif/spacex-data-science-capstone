import pandas as pd, requests
def get_past_launches(url="https://api.spacexdata.com/v4/launches/past"):
    r=requests.get(url,timeout=20); r.raise_for_status()
    return pd.json_normalize(r.json())
