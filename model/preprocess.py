import pandas as pd
import argparse

def preprocess(input_path, output_train_path, output_val_path):
    # First Minimal Preprocessing
    df = pd.read_csv(input_path)

    df = df.dropna()

    # Mapping Species to Id
    mapSpecieToId = {species: idx for idx, species in enumerate(df['species'].unique())}
    df['species'] = df['species'].map(mapSpecieToId)

    # Map Gender to Id
    mapGenderToId = {gender: idx for idx, gender in enumerate(df['sex'].unique())}
    df['sex'] = df['sex'].map(mapGenderToId)

    # Map Island to Id
    mapIslandToId = {island: idx for idx, island in enumerate(df['island'].unique())}
    df['island'] = df['island'].map(mapIslandToId)

    # Split into train and val, with shuffle and a constant random seed
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

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