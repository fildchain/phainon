# 第8章/generate_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 读取数据集，并将字符编码指定为 gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')
# 删除缺失值所在的行
penguin_df.dropna(inplace=True)
# 将企鹅的种类定义为目标输出变量
output = penguin_df['企鹅的种类']
# 将去除年份列不作为特征列
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]
# 对特征列进行独热编码
features = pd.get_dummies(features)
# 将目标输出变量转换为离散数值
output_codes, output_uniques = pd.factorize(output)

# 从 features 和 output_codes 这两个数组中将数据集划分为训练集和测试集
# 训练集为 80%，测试集为 20% (1-80%)
# 返回的 x_train 和 y_train 为划分得到的训练集特征和标签
# x_test 和 y_test 为划分得到的测试集特征和标签
# 这里标签和目标输出变量是一个意思
x_train, x_test, y_train, y_test = train_test_split(features, output_codes, test_size=0.2)

# 构建一个随机森林分类器
rfc = RandomForestClassifier()

# 使用训练集数据 x_train 和 y_train 来拟合（训练）模型
rfc.fit(x_train, y_train)

# 用训练好的模型 rfc 对测试集数据 x_test 进行预测，将预测结果存储在 y_pred 中
y_pred = rfc.predict(x_test)

# 计算测试集上模型的预测准确率
# 方法是使用 accuracy_score 方法，比对真实标签 y_test 和预测标签 y_pred
# 返回预测正确的样本占全部样本的比例，即准确率
score = accuracy_score(y_test, y_pred)
print(f'该模型的准确率是: {score}')
