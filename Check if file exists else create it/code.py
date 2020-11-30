import os
import pandas as pd

if os.path.exists('sample_file.csv') == False:
    df = pd.DataFrame({'A' : [], 'B' : [], 'C' : []})
    df.to_csv('sample_file.csv', index=False)
else:
    print("File already exists")
