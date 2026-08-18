"""Classification model comparison example."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_launches.csv"

def main():
    df = pd.read_csv(DATA)
    X = pd.get_dummies(df[["LaunchSite","Orbit","PayloadMass"]], drop_first=False)
    y = df["Class"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=2, stratify=y
    )
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "SVM": SVC(),
        "DecisionTree": DecisionTreeClassifier(random_state=2),
        "KNN": KNeighborsClassifier(n_neighbors=3),
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        print(name, accuracy_score(y_test, model.predict(X_test)))

if __name__ == "__main__":
    main()
