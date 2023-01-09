from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("data.csv")

X = df.drop(['track_id', 'genre_top'], axis=1)
y = df.genre_top

X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y)

tree = DecisionTreeClassifier(random_state=42)

tree.fit(X_train, y_train)

Pkl_Filename = "model_tree.pkl"  

import pickle
with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(tree, file)
