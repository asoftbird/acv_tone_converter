import csv
from io_acv import saveACVFile, readACVFile, readACVFileRaw

data = []
rows_per_color = 15
rows_per_color *= 2

with open("correctioncurve-80808080-rgb2.2.txt", "r") as file:
    read = csv.reader(file, delimiter="\t", )
    for row in read:
        data.append(row)

color_data = []
skip_data = [['Cyan:'], ['Magenta:'], ['Yellow:'], ['Black:']]

for item in data:
    try:
        if item == []:
            continue
        elif item in skip_data:
            continue
        else:
            color_data.append([item[0], item[1]])
    except IndexError:
        pass

CMYK_channel = [int(float(item)*2.55) for sublist in color_data for item in sublist]
master_channel = [0, 0, 255, 255]

chunkified_data = [CMYK_channel[x:x+rows_per_color] for x in range(0, len(CMYK_channel), rows_per_color)]
chunkified_data.insert(0, master_channel)

saveACVFile("correctioncurve-80808080-rgb2.2.acv", chunkified_data)

print(CMYK_channel)