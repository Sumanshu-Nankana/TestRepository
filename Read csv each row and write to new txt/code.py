# first method
def read_csv_row_and_write_2_new_txt():
    with open('sample.csv','r') as f:
        lines = f.readlines()
        for idx,line in enumerate(lines):
            filename = 'row'+str(idx)+'.txt'
            out_file = open(filename, 'w')
            out_file.write(line)
            out_file.close()
read_csv_row_and_write_2_new_txt()

# second method - this will not write column headers
def read_csvrow_and_write_2_txt1():
    import pandas as pd
    df = pd.read_csv('sample.csv')
    for idx,row in df.iterrows():
        filename = 'row'+str(idx)+'.txt'
        out_file = open(filename, 'w')
        row = row['col1']+','+row['col2']+','+row['col3']+'\n'
        out_file.write(row)
        out_file.close()
read_csvrow_and_write_2_txt1()