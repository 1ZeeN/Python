import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,11)
y = x**2
plt.plot(x,y)

# generate table
row_labels = ['Sx', 'Sy', 'Sx2']
table_vals = [[11], [21], [31]]

the_table = plt.table(cellText=table_vals,
                     colWidths=[0.1] * len(row_labels),
                     rowLabels=row_labels,
                     loc='best')
plt.legend(loc='best')
plt.show()