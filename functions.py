import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay



# Charger les données
def load_data_kidney(x):
    data = pd.read_csv(x)
    return data

def load_data_banknote():
    banknote_authentication = fetch_ucirepo(id=267) 
    # data (as pandas dataframes) 
    X = banknote_authentication.data.features 
    y = banknote_authentication.data.targets 
    data = pd.concat([X, y], axis=1)
    return data



def preprocess(data):
    clean_data = data.copy()
    clean_data.replace("?", np.nan, inplace=True)

    # Nettoyer les valeurs des colonnes
    clean_data = clean_data.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

    # Remplacer les NaN dans les colonnes numériques par la moyenne
    numeric_cols = clean_data.select_dtypes(include=[np.number]).columns
    clean_data[numeric_cols] = clean_data[numeric_cols].apply(lambda x: x.fillna(x.mean()), axis=0)

    # Remplacer les NaN dans les colonnes catégorielles par la catégorie la plus fréquente
    categorical_cols = clean_data.select_dtypes(include=[object]).columns
    clean_data[categorical_cols] = clean_data[categorical_cols].apply(lambda x: x.fillna(x.mode().iloc[0]), axis=0)

    # Convertir les colonnes binaires en 1 et 0
    binary_cols = ['classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
    for col in binary_cols:
        unique_values = clean_data[col].unique()
        if col == 'classification':
            clean_data[col] = clean_data[col].replace({'ckd': 1, 'notckd': 0}) #on précise pour la colonne classification que l'on souhaite 1 si la personne est malade et 0 sinon
        elif len(unique_values) == 2:
            clean_data[col] = clean_data[col].replace({unique_values[0]: 0, unique_values[1]: 1})
    
    clean_data.replace('?', np.nan, inplace=True)

    imputer = SimpleImputer(strategy='mean')  # or 'median', 'most_frequent'
    clean_data = imputer.fit_transform(clean_data)
    clean_data_df = pd.DataFrame(clean_data, columns=data.columns)

    return clean_data_df

def prepare_data(data, column_target):
    input = data.drop(column_target, axis=1)
    target = data[column_target]
    X_train, X_test, y_train, y_test = train_test_split(input, target, test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train



def train_model(Models, X_train, y_train):
    for name, model in Models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
    print("Training complete.")

def evaluate_model(Models, X_test, y_test):
    scores = {}
    for name, model in Models.items():
        print(f"Evaluating {name}...")
        score = model.score(X_test, y_test)
        scores[name] = score
    print("Evaluation complete.")
    return scores

def histogram(data):
    data.hist(bins=50, figsize=(20,15))
    plt.show()

def heatmap(data):
    plt.figure(figsize=(20,20))
    corr = data.corr()
    sns.heatmap(corr, 
        xticklabels=corr.columns,
        yticklabels=corr.columns, annot=True)
    plt.show()

def Confusion_matrix(X_test, y_test, Models):
    y_test_int = y_test.astype(int)
    for name, model in Models.items():
        print(f"Confusion Matrix for {name}:")
        y_pred = model.predict(X_test).astype(int)
        cm = confusion_matrix(y_test_int, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.title(f"Confusion Matrix for {name}")
        plt.show()