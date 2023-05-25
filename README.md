# 大学物理实验数据处理
大学物理实验的实验处理部分繁琐又机械，都什么年代了，还在用传统手算的方式进行实验数据处理，就离谱，所以我写了个程序来把自己从手按计算器的痛苦中解放出来
# 包含的实验处理
- 平均数计算，不确定度的计算
-  最小二乘法：计算斜率，截距
## 使用流程
### 1.环境安装
> 克隆后，在存放本仓库的文件夹中打开终端并输入：
> pip install -r requirements.txt
### 2.使用本仓库
#### 1.使用已经实例化的.py文件，进行特定的实验的实验处理.
- zheshelv.py 测量溶液的折射率和浓度
- xuanguangdu.py 测量旋光性溶液的旋光度
- mearsureVolume_instance.py 测量声速
#### 2.自己对需要的实验进行实例化
- 具体操作见代码内的注释，来构建自己的代码
