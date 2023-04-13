
from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import PCA
import numpy as np

x_data = np.loadtxt('new_x_data.txt')
x_data.reshape(-1,1)

# x_test = np.loadtxt('x_test.txt')
# x_test.reshape(-1,1)

# Specifying the number of components to do the pca analysis
pca_f = PCA(n_components=300)
pca_f.fit(x_data)
x_data_new = pca_f.fit_transform(x_data)

# # save results
# np.savetxt('x_data_after_PCA.txt', x_data_new, fmt='%.16f')
# # np.savetxt('test_data_after_PCA.txt', x_test_new, fmt='%.16f')

#specifying the variance to keep after pca
pca = PCA(0.9)
X_pca = pca.fit_transform(x_data)
print(X_pca.shape)

np.savetxt('x2000_data_after_PCA.txt', X_pca, fmt='%.16f')




