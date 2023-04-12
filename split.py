import numpy as np
import pandas as pd


x_data = np.loadtxt('x2000_data_after_PCA.txt')


y_data = np.loadtxt('new_labels.txt')

# # y_data.dtype
# # # df = pd.DataFrame(data)
# # y_data.shape


from sklearn.model_selection import train_test_split

X_train_new, X_test_new, y_train_new, y_test_new = train_test_split(x_data, y_data, test_size=0.25, random_state=0)

np.savetxt('x_test.txt', X_test_new)
np.savetxt('x_train.txt', X_train_new)
np.savetxt('y_train.txt',y_train_new)
np.savetxt('y_test.txt',y_test_new)

print(np.std(np.loadtxt('x_train.txt')))
print(np.std(np.loadtxt('x_test.txt')))