from base import physical_base
import numpy as np
# 在这个名为alpha的list里面，填你自己测量的旋光度的数据，之后运行即可
alpha=[8.15,8.40,8.55,8.30,8.50]
alpha=np.array([alpha],dtype=np.float32)
newproject=physical_base.physicDataProcess(alpha)
newproject.Directuncertainly(0,0.05)
