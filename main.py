import MyRandom
import numpy as np
import MRG32k3a
x=[]
for i in range (0,5000):
    # x.append(MyRandom.random())
    MRG32k3a.random()


print("均值：",np.mean(x))
print("方差：",np.var(x))



# MRG32k3a.random()
