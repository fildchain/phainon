import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

#设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

#读取数据集。并将字符编码指定为gbk，防止中文报错
insurance_df =pd.read_csv('student_data_adjusted_rounded.csv', encoding='utf-8')

#将期末考试分数定义为目标输出变量
output = insurance_df['期末考试分数']

#使用作为特征列
features = insurance_df[['学号','性别','专业','每周学习时长（小时）','上课出勤率','期中考试分数','作业完成率']]
#对特征列进行独热编码
features = pd.get_dummies(features)

#从features和output这两个数组中将数据集划分为训练集和测试集
#训练集为80%,测试集为20%(1-80%)
#返回的x_train和y_train为划分得到的训练集特征和标签
#x_test和y_test为划分得到的测试集特征和标签
#这里特征和目标输出变量是一个意思

x_train,x_test,y_train,y_test = train_test_split(features,output,train_size=0.8)

#构建一个随机森林回归模型的实例
rfr = RandomForestRegressor()

#使用训练集数据x_train和y_train来拟合训练模型
rfr.fit(x_train,y_train)

#用训练好的模型rfr对测试集数据x_test进行预测，将预测结果存储在y_pred中
y_pred = rfr.predict(x_test)
#计算模型的可决系数(R-squared)
#- R-squared接近0，表示模型仅能做出与平均值相当的预测
#- R-squared接近1，表示模型对数据的变异有很好的解释能力
#- R-squared的值界定在0~1
#- 当R-squared值超过0.5以上时才被认为模型有良好的预测能力

r2 = r2_score(y_test,y_pred)

#使用with语句，简化文件操作
#open()函数和'wb'参数用于创建并写入字节流
#pickle.dump()方法将模型对象转化成字节流

with open('rfr_model.pkl','wb') as f:
    pickle.dump(rfr,f)

print('保存成功，已生成相关文件。')


print(f'该模型的可决系数(R-squared)是:{r2}')
