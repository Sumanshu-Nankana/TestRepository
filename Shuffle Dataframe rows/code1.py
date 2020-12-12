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
    df2 = df_c1.sample(frac=1).reset_index(drop=True)

    for i in nan_index:
        line = pd.DataFrame({col: np.nan}, index=[i-1])
        df2 = df2.append(line, ignore_index=False)
        df2 = df2.sort_index().reset_index(drop=True)

    final_df = pd.concat([df,df2],axis=1)
    final_df = final_df[cols]
    final_df.to_csv('shuffle1.csv',index=False)

# pass any columns which we want to shuffle
shuffle_df_one_col(col)