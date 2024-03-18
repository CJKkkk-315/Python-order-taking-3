import pandas as pd
import numpy as np
import openpyxl

filelist = pd.read_table(r'file-name-list.txt',encoding='utf8', header=None)
filelist = filelist.values
aw = []
new_filelist = []
for i in filelist:
    if i[0][:4] not in aw:
        aw.append(i[0][:4])
        new_filelist.append(i)
data_output = np.zeros((1, 8))
for i in new_filelist:
    file_name = i[0]
    file = pd.read_excel(file_name, sheet_name='25关联方余额', header=None)
    file.fillna(0, inplace=True)
    file = file.values
    # print(file[:, 6].shape)
    for j in range(6, 3579):
        if file[j, 6] != 0:
            data_output = np.vstack((data_output, np.insert(file[j, 0:7],0,i[0]).reshape(1, -1)))
data_output = pd.DataFrame(data_output[1:, :])
data_output.to_excel('处理后的文件湖北test.xlsx', header=0, index=None)
