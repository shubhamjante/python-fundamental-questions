import os
import glob

folder_path = './Programming Fundamentals using Python - Part 01/'
files = list()
output_folder = './temp'

for r, d, f in os.walk(folder_path):
    for file in f:
        if '.py' in file:
            files.append(os.path.join(r, file))

for file in files:
    file_name = file.split('/')[-1].split('.')[0]
    os.system("enscript -1 --line-numbers -p '{}/{}.ps' --highlight=python --color=1 --font=Courier7 '{}'". \
              format(output_folder, file_name, file))
    os.system("pstopdf './temp/{}.ps'".format(file_name))
    os.remove("./temp/{}.ps".format(file_name))
