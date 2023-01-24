import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# variables
SalePrice = []
BsmtFinSF1 = []

# import CSV file
with open('LOGITData.csv','r') as csv_file:
    data = csv.reader(csv_file, delimiter=',')

    # read data into arrays
    for row in data:
        if row[0] == 'Fireplaces':
            continue
        SalePrice.append(int(row[1]))
        BsmtFinSF1.append(int(row[3]))

## Problem 1.2    
# scatter plot
plt.scatter(BsmtFinSF1, SalePrice, color = 'blue', marker='o', s= 5)
plt.xlabel('BsmtFinSF1')
plt.ylabel('SalePrice')
plt.tight_layout()

# remove excess ticks
xTickDistance = 500
yTickDistance = 50000
plt.xticks(np.arange(0,max(BsmtFinSF1)+xTickDistance, xTickDistance))
plt.yticks(np.arange(0,max(SalePrice)+yTickDistance, yTickDistance))

# lowess line
from statsmodels.nonparametric.smoothers_lowess import lowess
lowess = lowess(SalePrice, BsmtFinSF1, frac=0.3)
plt.plot(lowess[:,0], lowess[:,1], color='red', linewidth=2)

# show plot -> save and flush
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
