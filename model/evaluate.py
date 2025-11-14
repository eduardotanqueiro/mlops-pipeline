import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
import yaml


def load_params(path="params.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    params = load_params()

    model = joblib.load('ckpt/model.pkl')
    
    df = pd.read_csv(params['data']['processed_base_path']+"_val.csv")
    
    X = df.drop('species', axis=1)
    y = df['species']

    preds = model.predict(X)
    
    acc = accuracy_score(y, preds)
    f1 = f1_score(y, preds, average='weighted')

    print({"accuracy": acc, "f1_score": f1})