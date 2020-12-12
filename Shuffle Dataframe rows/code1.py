# Shuffle CSV only 1 columns and DO NOt shuffle BLANK Values of that column

import pandas as pd
import numpy as np

def shuffle_df_one_col():
    # Read sample1 csv
    df = pd.read_csv('sample1.csv')
    # Let says we want to shuffle column C1
    nan_index = df[df['C1'].isnull()].index.values.tolist()
    # Create the seperate dataframe from column_1
    # and drop the column1 from original dataframe
    df_c1 = pd.DataFrame(df['C1'])
    df = df.drop(['C1'],axis=1)
    dfc1 = df_c1.dropna()

    # Shuffle dataframe after dropping blank rows
    df2 = dfc1.sample(frac=1).reset_index(drop=True)

    # insert back the blank rows at particular index
    for i in nan_index:
        line = pd.DataFrame({"C1": np.nan}, index=[i+0.5-1])
        df2 = df2.append(line, ignore_index=False)
        df2 = df2.sort_index().reset_index(drop=True)
    df2 = df2.sort_index().reset_index(drop=True)
    final_df = pd.concat([df,df2],axis=1)
    final_df = final_df[["C1", "C2", "C3"]]
    final_df.to_csv('shuffle1.csv',index=False)

# call the function
shuffle_df_one_col()