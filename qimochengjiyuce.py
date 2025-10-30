import streamlit as st
import pickle
import pandas as pd

def introduce_page():
    """当选择简介页面时，将呈现该函数的内容"""
    st.write("#欢迎使用！")
    st.sidebar.success("单击↩ 成绩预测")
    st.markdown(
        """
        #期末成绩预测应用💰
        这个应用利用机器学习模型来预测期末成绩，为学校教书育人提供参考。
        ##背景介绍
        - 开发目标：帮助教师评估学生的学习成果，以实现良好教学的目的。
        - 模型算法：利用随机森林回归算法训练期末成绩预测模型。
        ##使用指南
        - 输入准确完整的学生信息，可以得到更准确的成绩预测。
        - 预测结果可以对学生学习效果和教师教学效果进行直接、客观的反馈，但仅供参考。
        - 有任何问题欢迎联系我们的技术支持。
        技术支持:email:: support@example.com
        """
    )

def predict_page():
    """当选择预测成绩页面时，将呈现该函数的内容"""
    st.markdown(
        """
        ##使用说明
        这个应用利用机器学习模型来预测成绩费用，为学校教书育人提供参考。
        - **输入信息**：在下面输入学生的个人信息、学习信息等。
        - **成绩预测**：应用会预测学生的未来期末成绩。
        """
    )
    with st.form('user_inputs'):
        sex = st.radio('性别', options=['男性', '女性'])
        zhuanye = st.selectbox('专业', ('工商管理', '人工智能', '财务管理', '电子商务','大数据管理'))
        xuehao = st.number_input('学号',step=1, min_value=0)
        time = st.number_input("每周学习时长(小时)", step=1, min_value=0)
        chuqinlv =st.number_input('上课出勤率', min_value=0.0)
        zuoyewanchenglv = st.number_input('作业完成率', min_value=0.0)
        qizhongfenshu =st.number_input("期中考试分数", min_value=0.0)
        submitted = st.form_submit_button('成绩预测')
    if submitted:
        sex_female, sex_male = 0, 0
        if sex == '女性':
            sex_female = 1
        elif sex == '男性':
            sex_male = 1
        zhuanye_gs, zhuanye_rg, zhuanye_cw, zhuanye_dz,zhuanye_ds  = 0, 0, 0, 0, 0
        if zhuanye == '工商管理':
            region_gs = 1
        elif zhuanye == '人工智能':
            zhuanye_rg = 1
        elif zhuanye == '财务管理':
            zhuanye_cw = 1
        elif zhuanye == '电子商务':
            zhuanye_dz = 1
        elif zhuanye  == '大数据管理':
            zhuanye_ds = 1

        format_data = [sex_female, sex_male,
                       zhuanye_gs, zhuanye_rg, zhuanye_cw, zhuanye_dz,zhuanye_ds,
                       xuehao,time ,chuqinlv ,zuoyewanchenglv,qizhongfenshu] 


        with open('rfr_model.pkl', 'rb') as f:
            rfr_model = pickle.load(f)

        format_data_df = pd.DataFrame(data=[format_data], columns=rfr_model.feature_names_in_)
        predict_result = rfr_model.predict(format_data_df)[0]
        st.write('根据您输入的数据，预测该学生的期末成绩是：', round(predict_result, 2))
        st.write("技术支持:email:: support@example.com")

st.set_page_config(
    page_title="期末成绩预测",
    page_icon="💰",
)

nav = st.sidebar.radio("导航菜单", ["项目介绍", "专业数据分析","成绩预测"])
if nav == "项目介绍":
    introduce_page()
else:
    predict_page()
