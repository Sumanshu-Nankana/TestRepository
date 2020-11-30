import pandas as pd

def create_jcl():
    # read csv file
    try:
        df = pd.read_csv("sample_excel.csv")
    except:
        print("Unable to find csv file")
        exit()

    # iterate over dataframe rows
    for idx,row in df.iterrows():

        # save row values
        input_val = row[1]
        output_val = row[2]

        # open sample input and output txt file
        try:
            input_jcl = open('input.txt','r')
        except:
            print("Unable to find Input JCL")
            exit()
        
        try:
            output_jcl = open('output.txt','r')
        except:
            print("Unable to find Output JCL")
            exit()

        # read input and output text file
        input_file = input_jcl.readlines()
        output_file = output_jcl.readlines()

        # new output file names
        inp_row = 'inp_row' + str(idx) + '1'
        inp_file = open(inp_row,'w')
        out_row = 'out_row' + str(idx) + '2'
        out_file = open(out_row,'w')

        # iterate over sample input file and write to new file
        for line in input_file:
            if 'INPJB000' in line:
                inpjb_name = 'INPJB' + str(idx) + '1'
                inp_file.write(line.replace('INPJB000',inpjb_name))
                df.loc[idx,'inp_job'] = inpjb_name
            elif 'PKM.TR.SOURCE.B8' in line:
                inp_file.write(line.replace('PKM.TR.SOURCE.B8',input_val))
            else:
                inp_file.write(line)

        # iterate over sample output file and write to new file
        for line in output_file:
            if 'OUTJB000' in line:
                outjb_name = 'OUTJB' + str(idx) + '2'
                out_file.write(line.replace('OUTJB000',outjb_name))
                df.loc[idx,'out_job'] = outjb_name
            elif 'KM.TR.SOURCE.B9' in line:
                out_file.write(line.replace('PKM.TR.SOURCE.B9',output_val))
            else:
                out_file.write(line)
        
        # update the same excel with job-names in columns
        df.to_csv('sample_excel.csv',index=False)

        # close all the files
        input_jcl.close()
        output_jcl.close()
        inp_file.close()
        out_file.close()

# call the function
create_jcl()