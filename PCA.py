# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:06:05 2022

@author: ZHANG Jun
"""

from sklearn.decomposition import IncrementalPCA
from sklearn.decomposition import PCA
import numpy as np

x_data = np.loadtxt('new_x_data.txt')
x_data.reshape(-1,1)

# x_test = np.loadtxt('x_test.txt')
# x_test.reshape(-1,1)

# pca_f = PCA(n_components=300)
# # pca_f.fit(x_data)
# x_data_new = pca_f.fit_transform(x_data)
# print(pca_f.explained_variance_)
# print(pca_f.explained_variance_ratio_)
# print(pca_f.explained_variance_ratio_.sum())
# print(pca_f.singular_values_)

# # x_test_new = pca_f.transform(x_test)

# # save model
# import joblib
# joblib.dump(pca_f, 'pca_model.joblib')

# # save results
# np.savetxt('x_data_after_PCA.txt', x_data_new, fmt='%.16f')
# # np.savetxt('test_data_after_PCA.txt', x_test_new, fmt='%.16f')

pca = PCA(0.9)
X_pca = pca.fit_transform(x_data)
print(X_pca.shape)

np.savetxt('x2000_data_after_PCA.txt', X_pca, fmt='%.16f')




