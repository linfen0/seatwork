#python创建特定类的对象
#p=class("填写参数")
#pytho根本不需要声明，同样元素个数也不用声明
#本题不用测不确定度
'''
将实验数据储存在numpy数组后,指定行,计算该行的不确定度,
指定两行对这两行计算线性回归
'''
import math 
import numpy as np

class physicDataProcess:
    def __init__(self,datatable:np.ndarray):
        '''dataTable is a ndarry object'''
        self.datatable=datatable
        self.processedDatatable=self.datatable
        
        self.UncertaintyList=[]
        self.UncertaintyRList=[]
        self.averageList=[]
        
    def covertOrinData(self): 
        pass
    def Directuncertainly(self,row_index:int,instrumentAccura:np.float32):
        '''直接测量不确定度/标准不确定度'''
        processedDataX=self.processedDatatable[row_index]
        print('\n'*3+'#'*5+f"第{row_index}行的信息"+'#'*5)
        print("*"*5+"误差"+5*"*")
        average=np.mean(processedDataX)
        print(f"维度{row_index}的平均数{average:.5g}")
        sum=0
        for x in processedDataX:
            sum+=((x-average)**2)
        sigmaA=math.sqrt(sum/((len(processedDataX)-1)*len(processedDataX)))
        sigmaB=instrumentAccura/(math.sqrt(3))
        Uncertainty=math.sqrt(sigmaA**2+sigmaB**2)
        UncertaintyR=Uncertainty/average
        print(f"不确定度表:A类误差(保留3位有效数字):{sigmaA:.5g}|B类误差(保留2位有效数字):{sigmaB:.3g}|直接测量量合成不确定度{Uncertainty:.2g}|直接测量量相对合成不确定度{UncertaintyR:.2g}")
        
        self.UncertaintyList.append(Uncertainty)
        self.UncertaintyRList.append(UncertaintyR)
        self.averageList.append(average)

    def indirecUncertainty(self):
        '''间接测量量的不确定度'''
        pass

    def leastSquares(self,row_indexs:tuple):
        '''决定具体使用那两个维度的数据进行线性回归,第一个为自变量.第二个为因变量'''
        xlist=self.processedDatatable[row_indexs[0]]
        ylist=self.processedDatatable[row_indexs[1]]
        averageX=np.mean(xlist)
        averageY=np.mean(ylist)
        print("\n"+"x平均数"+f"{(averageX):}","y平均数"+f"{averageY:}")
        sum=0;
        sumsquaresX=0;
        for i in range(0,len(xlist)):
            sum=sum+(xlist[i]*ylist[i])
            sumsquaresX=sumsquaresX+(xlist[i]**2)
        averageXmultiY=sum/len(xlist)
        print("x*y平均数"+f"{(averageXmultiY):}")
        averagesquaresX=sumsquaresX/len(xlist)
        print("x*x平均数"+f"{averagesquaresX:}")
        print("(-x)*(-x):"+f"{averageX**2:}")
        print("(-y)*(-x):"+f"{averageX*averageY:}")
        #print(averageXmultiY,averagesquaresX)
        
        lineSlop=(averageXmultiY-(averageX*averageY))/(averagesquaresX-(averageX**2))
        lineIntercept=averageY-(lineSlop*averageX)
        print("\n"+f"最小二乘计算的斜率为:{lineSlop:.6g}" )
        print("\n"+f"最小二乘计算的截距为:{lineIntercept:.6g}")  
        return lineSlop,lineIntercept



#------------------------------main--------------------
