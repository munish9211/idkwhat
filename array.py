import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,10]])
d=np.linalg.det(a)
if d!=0:
  print(d)