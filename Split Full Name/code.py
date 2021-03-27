import pandas as pd 
import numpy as np

class NameData:
  def __init__(self, inpFile, chunksize):

    # initialize variables
    self.inpFile = inpFile
    self.chunksize = chunksize
    self.tempList = []
    
    # read input file in chunks of 5 records
    # and append chunk in a list
    for chunk in pd.read_csv(self.inpFile, chunksize=self.chunksize):
        self.tempList.append(chunk)
    
    # concatenate all those chunks
    self.finalDf = pd.concat(self.tempList, axis=0)

  # Seperate first, middle and last names from full-name
  def extract_first_middle_last(self):
    self.finalDf['First_Name'] = np.nan
    self.finalDf['Middle_Name'] = np.nan
    self.finalDf['Last_Name'] = np.nan

    # iterate over all records
    for idx,row in self.finalDf.iterrows():
      temp = row['Full Name'].split()
      if len(temp) == 1:
        self.finalDf['First_Name'].iloc[idx] = temp[0]
      elif len(temp) == 2:
        self.finalDf['First_Name'].iloc[idx] = temp[0]
        self.finalDf['Last_Name'].iloc[idx] = temp[1]
      else:
        self.finalDf['First_Name'].iloc[idx] = temp[0]
        self.finalDf['Last_Name'].iloc[idx] = temp[-1]
        self.finalDf['Middle_Name'].iloc[idx] = ' '.join(str for str in temp[1:len(temp)-1])

    firstName_df = self.finalDf['First_Name'].dropna().drop_duplicates().reset_index(drop=True)
    middleName_df = self.finalDf['Middle_Name'].dropna().drop_duplicates().reset_index(drop=True)
    lastName_df = self.finalDf['Last_Name'].dropna().drop_duplicates().reset_index(drop=True)
    tempDf =  pd.concat([firstName_df, middleName_df, lastName_df], axis=1).reset_index(drop=True)
    output = pd.concat([self.finalDf, tempDf], axis=1).reset_index(drop=True)
    output.to_csv('output.csv', index=False)


sample_file = 'sample_names.csv'
chunksize = 5
nd = NameData(sample_file, chunksize)
nd.extract_first_middle_last()