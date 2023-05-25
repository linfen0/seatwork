from base import physical_base
import numpy as np
#折射率
n1=[1.3550,1.3556,1.3555,1.3560]
#浓度
c1=[15.22,15.08,15.02,14.84]
datatable=np.array([n1,c1],dtype=np.float16)
#测量折射率(百分比)
project=physical_base.physicDataProcess(datatable)
print("折射率")
project.Directuncertainly(0,0.002)
print("溶液浓度")
project.Directuncertainly(1,0.05)