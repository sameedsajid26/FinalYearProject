import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Comment this if the data visualisations doesn't work on your side
# %matplotlib inline
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

true_y = np.loadtxt('new_labels.txt')
pred_y = np.loadtxt('checkpoint/pred/prediction_mean.txt')
plt.scatter(true_y, pred_y)
plt.title('Testing Accuracy')
plt.xlabel('True value')
plt.ylabel('Predicted SFE value');
plt.legend(title="Gender", loc="upper right")
plt.legend(title="MAPE = 4.869 \nValidation MAPE = 5.547", loc="upper right")
plt.plot((-230,-130),(-230,-130),'r')


plt.show()

# labels = np.loadtxt('new_labels.txt')
# plt.plot(labels)
# plt.show()