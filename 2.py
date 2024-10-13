import numpy as np
import pandas as pd
#1
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])
vertical = np.vstack((A, B))
horizontal = np.hstack((A, B))
#2
elements = np.intersect1d(A, B)
#3
nrange = A[(A >= 5) & (A <= 10)]
#4
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
newiris = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]
#5
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered = df[['Manufacturer', 'Model', 'Type']].iloc[::20]
#6
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
#7
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rowss = df_random[df_random.sum(axis=1) > 100]
