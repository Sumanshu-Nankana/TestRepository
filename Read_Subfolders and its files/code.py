import os
import pandas as pd
    
def read_subfolders_and_files(path):

    all_sub_folders = []
    main_folder = path

    # getting all sub-folders
    for child in os.listdir(main_folder):
        if child != '.ipynb_checkpoints':
            all_sub_folders.append(child)

    # making dictionary having key as sub_folder name and value as list of all files of that sub_folder
    dic = {}
    for i in all_sub_folders: 
        sub_path = os.path.join(main_folder,i)
        dic[sub_path] = os.listdir(sub_path)

    # create output file and write to it
    with open('output.csv','w') as f:
        for key,val in dic.items():
            fldr_name = key.split('/')[-1]
            for i in range(len(val)-1):
                file_name = val[i]
                file_path = os.path.join(key,val[i])
                with open(file_path) as temp:
                    header = temp.readline()
                    line = fldr_name + ',' + file_name + ',' + header + '\n'
                    f.write(line)
    df = pd.read_csv('output.csv', header=None)
    df.to_csv('output.csv',index=False)

# call the function
main_folder_path = 'Main_Folder'
read_subfolders_and_files(main_folder_path)