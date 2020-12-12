import pandas as pd
import numpy as np

def shuffle_df_without_blank():
    # read the csv - assuming there are no headers
    df = pd.read_csv('sample.csv',header=None)
    
    # setting the headers
    df.columns=['ID','Fname','Lname','State']
    
    # find index of blank rows
    nan_index = df[df['Fname'].isnull()].index.values.tolist()
    
    # frop blank rows
    df1 = df.dropna()
    
    # Shuffle dataframe after dropping blank rows
    df2 = df1.sample(frac=1).reset_index(drop=True)

    abc=[]
    for x in nan_index:
        abc.append(x+0.5-1)
    
    # insert back the blank rows at particular index
    for i in abc:
        line = pd.DataFrame({"ID": np.nan, "Fname": np.nan, "Lname": np.nan, "State": np.nan}, index=[i])
        df2 = df2.append(line, ignore_index=False)
        df2 = df2.sort_index().reset_index(drop=True)
    df2 = df2.sort_index().reset_index(drop=True)

    # Save the shuffle dataframe to csv file
    df2.to_csv('shuffle.csv',index=False)

# call the function
shuffle_df_without_blank()