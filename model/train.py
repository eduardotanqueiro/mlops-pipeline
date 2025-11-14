import argparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os
import yaml


def load_params(path="params.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


def train(args):
    params = load_params()
    df = pd.read_csv(params['data']['processed_path'])

    X = df.drop('species', axis=1)
    y = df['species']


    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=50)
    model.fit(X_train, y_train)

    preds = model.predict(X_val)
    acc = accuracy_score(y_val, preds)

    os.makedirs('ckpt', exist_ok=True)

    # Give informative name to the model file, such as accuracy and parameters
    model_filename = f"ckpt/model_acc_{acc:.4f}_n_estimators_50.pkl"
    joblib.dump(model, model_filename)

    print(f"val_accuracy: {acc}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    train(args)