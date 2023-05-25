from phyproject import MearsureVolumeSpped
import numpy as np

x=[21.65,22.25,22.85,23.22,23.07]

y=[37.8,37.8,37.8,37.8,37.8]

x2=[24.71,25.08,24.21,24.27,23.78]

dataTable1=np.array([x,y],dtype=np.float32)
dataTable2=np.array([x2,y],dtype=np.float32)
project_volume=[]

project_volume.append(MearsureVolumeSpped.MearsureVolumeSpped(dataTable2,37.8))
project_volume.append(MearsureVolumeSpped.MearsureVolumeSpped(dataTable1,37.8))

for i in range(len(project_volume)):
    project_volume[i].Directuncertainly(0,0.02)
    project_volume[i].Directuncertainly(1,0.001)
    project_volume[i].indirecUncertainty()
