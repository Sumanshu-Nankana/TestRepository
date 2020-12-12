# Shuffle CSV only 1 columns and DO NOt shuffle BLANK Values of that column

import pandas as pd
import numpy as np

def shuffle_df_one_col(col):
    df = pd.read_csv('sample1.csv')
    cols = df.columns
    nan_index = df[df[col].isnull()].index.values.tolist()
    df_c1 = pd.DataFrame(df[col])
    df = df.drop([col],axis=1)
    df_c1.dropna(inplace=True)
    df_c1[col] = df_c1[col].sample(frac=1).values
    
    for i in nan_index:
        line = pd.DataFrame({col: np.nan}, index=[i-1])
        df_c1 = df_c1.append(line, ignore_index=False)
        df_c1 = df_c1.sort_index().reset_index(drop=True)
    print(df_c1)
    df = pd.concat([df,df_c1],axis=1)
    df = df[cols]
    df.to_csv('shuffle1.csv',index=False)

# pass any columns which we want to shuffle
shuffle_df_one_col('C1')