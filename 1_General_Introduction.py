import streamlit as st
import os
from PIL import Image

# 设置网页名称
st.set_page_config(page_title='中国AQI简单集成平台')

with st.spinner("正在加载数据，请稍候..."):
    import time
    time.sleep(3)

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(current_dir, "photo_background.jpg")
image1 = Image.open(str(image_path),mode='r')
st.image(image1,caption="愿蓝天白云常在", use_column_width=True)


st.title("中国AQI标准简介:earth_asia:")
st.markdown(
    """
    <style>
        h1 {
            color: navy;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("基础概念")
st.markdown(
    """
    <style>
        h2 {
            color: navy;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 添加文本
text1 = """空气质量指数（Air Quality Index，缩写<span style="color:red">AQI</span>）又称空气质量指数或空气污染指数，是定量描述空气质量状况的非线性无量纲指数。
其数值越大、级别和类别越高、表征颜色越深，说明空气污染状况越严重，
对人体的健康危害也就越大，适用于表示城市的短期空气质量状况和变化趋势。"""
st.write(text1, unsafe_allow_html=True)

st.header("参与评价的污染物")
st.markdown(
    """
    <style>
        h2 {
            color: navy;
        }
    </style>
    """,
    unsafe_allow_html=True
)

text2 = """空气质量指数分级计算参考标准是GB 3095-2012《环境空气质量标准》（现行），
参与评价的污染物为<span style="color:red">SO2</span>、
<span style="color:red">NO2</span>、
<span style="color:red">PM10</span>、
<span style="color:red">PM2.5</span>、
<span style="color:red">O3</span>、
<span style="color:red">CO</span>等。
针对单项污染物的还规定了空气质量分指数。\n
1、一级： 空气污染指数 ≤50优级\n
2、二级： 空气污染指数 ≤100良好\n
3、三级： 空气污染指数 ≤150轻度污染\n
4、四级： 空气污染指数 ≤200中度污染\n
5、五级： 空气污染指数 ≤300重度污染\n
6、六级：空气污染指数>300严重污染
"""
st.write(text2, unsafe_allow_html=True)

st.header("AQI分级")
st.markdown(
    """
    <style>
        h2 {
            color: navy;
        }
    </style>
    """,
    unsafe_allow_html=True
)

text3 = """<span style="color:red">空气污染指数</span>的取值范围定为<span style="color:purple">0～500</span>，
其中0～50、51～100、101～200、201～300和大于300，
分别对应国家空气质量标准中日均值的 I级、II级、III级、IV级和V级标准的污染物浓度限定数值，
在实际应用中，又把III级和IV级分为III（1）级、III（2）级和IV（1） 级、IV（2）级。"""
text4 = """<span style="color:green">I级</span>，空气质量评估为优，对人体健康无影响；"""
text5 = """<span style="color:yellow">II级</span>，空气质量评估为良，对人体健康无显著影响；"""
text6 = """<span style="color:orange">III级</span>，为轻度污染，健康人群出现刺 激症状；"""
text7 = """<span style="color:red">IV级</span>，中度污染，健康人群普遍出现刺激症状；"""
text8 = """<span style="color:purple">V级</span>，严重污染，健康人群出现严重刺激症状。"""

st.write(text3, unsafe_allow_html=True)
st.write(text4, unsafe_allow_html=True)
st.write(text5, unsafe_allow_html=True)
st.write(text6, unsafe_allow_html=True)
st.write(text7, unsafe_allow_html=True)
st.write(text8, unsafe_allow_html=True)








