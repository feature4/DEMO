import numpy as np
s = [1, 2, 3]
print(s)
s= np.append(s, [[4, 5, 6], [7, 8, 9]])
print(s)
s= np.append(s, [5, 7, 8])
print(s)
print(len(s))
s= np.pad(s, (0, 15 - len(s)), 'constant', constant_values = (0))
print(s)
print(len(s))