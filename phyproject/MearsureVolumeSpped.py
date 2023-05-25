'''
实验:驻波法和相位比较法测量声速\n
将实验数据储存在numpy数组后,指定行
计算该行的不确定度,
指定两行,对这两行进行线性回归
'''
from base import physical_base
import math 
import numpy as np
class MearsureVolumeSpped(physical_base.physicDataProcess):
    '''预先处理的'''
    def __init__(self, datatable: np.ndarray,frequence:float):
        super().__init__(datatable)
        self.frequence=frequence
        
    def bestEstimateValue(self):
        bestEstimateValue=2*self.averageList[0]*self.frequence
        print(f"最佳估计值{bestEstimateValue:}")
        return bestEstimateValue
        
    def indirecUncertainty(self):
        sum=0
        for uncertaintyR in self.UncertaintyRList:
            sum=sum+uncertaintyR**2
        indirecuncertaintyR=math.sqrt(sum)
        indirecuncertainty=indirecuncertaintyR*(self.bestEstimateValue())
        print(f"间接测量 相对不确定度{indirecuncertaintyR:.6g},\n间接测量 的不确定度{indirecuncertainty:.5g}")

        return  indirecuncertaintyR,indirecuncertainty
    def covertOrinData(self):
        '''mm单位*khz最后单位是m/s'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        return 0