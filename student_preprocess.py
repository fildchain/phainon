import pandas as pd

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



print("下面是独热编码后，特征列的前5行数据:")
print(features.head())
print()   #换行分割

#查看数据框的各列信息
print("前5行数据目标输出数据:")
print(output.head())
