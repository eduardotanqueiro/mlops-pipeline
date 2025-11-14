import pandas as pd
import argparse

def preprocess(input_path, output_path):
    # First Minimal Preprocessing
    df = pd.read_csv(input_path)

    df = df.dropna()

    df_train = df[:int(0.8 * len(df))]
    df_val = df[int(0.8 * len(df)):]

    df_train.to_csv(output_path + "_train.csv", index=False)
    df_val.to_csv(output_path + "_val.csv", index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    preprocess(args.input, args.output)
