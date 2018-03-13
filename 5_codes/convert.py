
import os
import sys

files_dir = sys.argv[1]

for file_name in os.listdir(files_dir):
    file_path = files_dir + file_name
    file_in = open(file_path, 'r')

    tmp_list = []
    for line in file_in:
        tmp_list.append(line.strip())

    print '\t'.join([file_name, ' '.join(tmp_list)])
