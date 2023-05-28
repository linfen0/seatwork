from base import physical_base
import numpy as np
cita0=np.array([[179.10,179.10,179.10,179.05,179.05]],dtype=np.float64)
cita=np.array([[189.00,189.05,189.20,189.05,189.10]],dtype=np.float64)
alpha=cita[:]-cita0[:]
np.set_printoptions(precision=2, suppress=True)
print(alpha)
#alpha=[9.05,8.40,8.65,8.40,8.60]
#alpha=np.array([alpha],dtype=np.float32)
newproject=physical_base.physicDataProcess(alpha)
