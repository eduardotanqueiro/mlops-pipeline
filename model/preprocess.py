import pandas as pd
import argparse

def preprocess(input_path, output_path):
    # First Minimal Preprocessing
    df = pd.read_csv(input_path)

    df = df.dropna(thresh=2)
    df.to_csv(output_path, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    preprocess(args.input, args.output)
