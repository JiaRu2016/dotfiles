import sys
import pandas as pd

#print(sys.argv)

filepath = sys.argv[1]

if filepath.endswith('.feather'):
    df = pd.read_feather(filepath)
elif filepath.endswith('.parquet'):
    df = pd.read_parquet(filepath)
elif filepath.endswith('.pkl'):
    df = pd.read_pickle(filepath)
elif filepath.endswith('.csv'):
    df = pd.read_csv(filepath)
else:
    raise ValueError(f'can not infer file format from file name: {filepath}')

print(df)

