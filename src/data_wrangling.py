import pandas as pd
def prepare_features(df):
    X=pd.get_dummies(df[["FlightNumber","LaunchSite","Orbit","PayloadMass","Year"]],drop_first=False).astype(float)
    y=df["Class"].astype(int)
    return X,y
