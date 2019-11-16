import numpy as np


print('01 <-np.random.normal')
X = np.random.normal(loc=1, scale=10, size=(12000, 100000))
print(X)

print('02 <- np.mean')
m = np.mean(X, axis=0)
print(m)

print('03 <- np.std')
std = np.std(X, axis=0)
print(std)

print('04 <- X_norm')
X_norm = ((X - m)/std)
print(X_norm)

num_user=input('->')