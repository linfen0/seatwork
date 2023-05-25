from base import physical_base
import numpy as np
alpha=[9.05,8.40,8.65,8.40,8.60]
alpha=np.array([alpha],dtype=np.float32)
newproject=physical_base.physicDataProcess(alpha)
newproject.Directuncertainly(0,0.05)