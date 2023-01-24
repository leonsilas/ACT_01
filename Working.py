import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# variables
Fireplaces = []
SalePrice = []
LotArea = []
BsmtFinSF1 = []

# import CSV file
with open('LOGITData.csv','r') as csv_file:
    data = csv.reader(csv_file, delimiter=',')

    # read data into arrays
    for row in data:
        if row[0] == 'Fireplaces':
            continue
        Fireplaces.append(int(row[0]))
        SalePrice.append(int(row[1]))
        LotArea.append(int(row[2]))
        BsmtFinSF1.append(int(row[3]))

# show plot -> save and flush
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
