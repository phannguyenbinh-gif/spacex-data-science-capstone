from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
def train_decision_tree(X,y,random_state=42):
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.30,random_state=random_state,stratify=y)
    model=DecisionTreeClassifier(max_depth=4,random_state=random_state).fit(Xtr,ytr)
    return model, accuracy_score(yte,model.predict(Xte))
