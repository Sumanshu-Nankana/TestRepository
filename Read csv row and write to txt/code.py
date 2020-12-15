# First Method
def read_csvrow_and_write_2_txt():
    import pandas as pd
    df = pd.read_csv('sample.csv')
    out_file = open('output.txt', 'w')
    for idx,row in df.iterrows():
        row = row['col1']+','+row['col2']+','+row['col3']+'\n'
        out_file.write(row)
    out_file.close()

read_csvrow_and_write_2_txt()
    
# Second Method
def read_csvrow_and_write_2_txt1():
    out_file1 = open('output1.txt', 'w')
    with open('sample.csv','r') as f:
        lines = f.readlines()
        for line in lines:
            out_file1.write(line)
    out_file1.close()

read_csvrow_and_write_2_txt1()