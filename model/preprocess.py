import pandas as pd
import argparse

def preprocess(input_path, output_train_path, output_val_path):
    # First Minimal Preprocessing
    df = pd.read_csv(input_path)

    df = df.dropna()

    df_train = df[:int(0.8 * len(df))]
    df_val = df[int(0.8 * len(df)):]

    df_train.to_csv(output_train_path, index=False)
    df_val.to_csv(output_val_path, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output_train", required=True)
    parser.add_argument("--output_val", required=True)
    args = parser.parse_args()

    preprocess(args.input, args.output_train, args.output_val)