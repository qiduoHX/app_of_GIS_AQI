import streamlit as st
import os
from PIL import Image

with st.spinner("正在加载数据，请稍候..."):
    import time
    time.sleep(3)

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

col1,col2 = st.columns(2)


with col1:
    image_path1 = os.path.join(current_dir, "photo_flowers.jpg")
    image1 = Image.open(str(image_path1),mode='r')
    st.image(image1,caption="晴空万里")

# 在第二列显示第二张图片
with col2:
    image_path2 = os.path.join(current_dir, "photo_polution.jpg")
    image2 = Image.open(str(image_path2),mode='r')
    st.image(image2,caption="雾霾笼罩")

def display_aqi_info(aqi_range):
    aqi_info = {
        "0~50": {
            "空气质量级别": "一级",
            "空气质量指数类别": "优",
            "表示颜色": "绿色",
            "对健康影响情况": "空气质量令人满意，基本无空气污染。",
            "建议采取措施": "继续保持良好的生活习惯，无需特殊防护措施，各类人群可正常活动。"
        },
        "51~100": {
            "空气质量级别": "二级",
            "空气质量指数类别": "良",
            "表示颜色": "黄色",
            "对健康影响情况": "空气质量可接受，但某些污染物可能对少数异常敏感人群健康有较弱影响。",
            "建议采取措施": "极少数异常敏感人群应减少户外活动。"
        },
        "101~150": {
            "空气质量级别": "三级",
            "空气质量指数类别": "轻度污染",
            "表示颜色": "橙色",
            "对健康影响情况": "易感人群症状有轻度加剧，健康人群出现刺激症状。",
            "建议采取措施": "儿童、老年人及心脏病、呼吸系统疾病患者应减少长时间、高强度的户外锻炼。"
        },
        "151~200": {
            "空气质量级别": "四级",
            "空气质量指数类别": "中度污染",
            "表示颜色": "红色",
            "对健康影响情况": "进一步加剧易感人群症状，可能对健康人群心脏、呼吸系统有影响。",
            "建议采取措施": "儿童、老年人及心脏病、呼吸系统疾病患者避免长时间、高强度的户外锻炼，一般人群适量减少户外运动。"
        },
        "201~300": {
            "空气质量级别": "五级",
            "空气质量指数类别": "重度污染",
            "表示颜色": "紫色",
            "对健康影响情况": "心脏病、呼吸系统疾病患者症状显著加剧，运动耐受力降级，健康人群普遍出现症状。",
            "建议采取措施": "儿童、老年人及心脏病、呼吸系统疾病患者应停留在室内，停止户外运动，一般人群减少户外运动。"
        },
        ">300": {
            "空气质量级别": "六级",
            "空气质量指数类别": "严重污染",
            "表示颜色": "褐红色",
            "对健康影响情况": "健康人群运动耐受力降低，有明显强烈症状，提前出现某些疾病。",
            "建议采取措施": "儿童、老年人和病人应当留在室内，停止户外运动，避免体力消耗，一般人群应避免户外运动。"
        }
    }

    aqi_info_selected = aqi_info.get(aqi_range, {})

    if aqi_info_selected:
        st.markdown(f"<font color='DeepSkyBlue'>:grapes:空气质量级别 : </font>" + aqi_info_selected.get("空气质量级别", ""), unsafe_allow_html=True)
        st.markdown(f"<font color='DeepSkyBlue'>:melon:空气质量指数类别 : </font>" + aqi_info_selected.get("空气质量指数类别", ""), unsafe_allow_html=True)
        st.markdown(f"<font color='DeepSkyBlue'>:watermelon:表示颜色 : </font>" + aqi_info_selected.get("表示颜色", ""), unsafe_allow_html=True)
        st.markdown(f"<font color='DeepSkyBlue'>:tangerine:对健康影响情况 : </font>" + aqi_info_selected.get("对健康影响情况", ""), unsafe_allow_html=True)
        st.markdown(f"<font color='DeepSkyBlue'>	:banana:建议采取措施 : </font>" + aqi_info_selected.get("建议采取措施", ""), unsafe_allow_html=True)
    else:
        st.write("请选择有效的AQI范围")

# 设置网页标题
st.title("不同AQI等级介绍")

# 设置下拉框选项
aqi_ranges = ["0~50", "51~100", "101~150", "151~200", "201~300", ">300"]
selected_aqi_range = st.selectbox("请选择AQI范围", aqi_ranges)

# 显示对应的文本介绍
display_aqi_info(selected_aqi_range)

