import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

f = plt.figure()
data = np.random.normal(size=(20, 6)) + np.arange(6)/2
sns.set_style('whitegrid')
sns.boxplot(data=data)
#plt.show()
f.savefig('figure1.png')