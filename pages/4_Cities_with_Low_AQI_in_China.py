import streamlit as st
import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from datetime import datetime

with st.spinner("正在加载数据，请稍候..."):
    import time
    time.sleep(15)

# 获取当前北京时间的小时数
current_time = datetime.now().strftime("%Y年%m月%d日%H") + "时"

# 创建一个网页标题为"中国AQI最低的前20个城市"，颜色为绿色
st.title("中国AQI最低的前20个城市:grinning_face_with_star_eyes:")
st.markdown('<style>h1{color: lightskyblue;}</style>', unsafe_allow_html=True)

# 创建副标题，显示数据获取时间
st.caption(f"数据获取时间：{current_time}（北京时间）")

def main():
    # 读取CSV文件
    data = pd.read_csv("air_quality_ranking_best_location.csv")

    # 过滤掉经纬度为空的数据
    data = data.dropna(subset=["纬度", "经度"])

    # 创建Geopandas GeoDataFrame
    geometry = gpd.points_from_xy(data['经度'], data['纬度'])
    gdf = gpd.GeoDataFrame(data, geometry=geometry)

    # 将GeoDataFrame转换为GeoJSON格式
    geojson_data2 = gdf.to_json()

    # 创建KeplerGL地图对象
    map_2 = KeplerGl(height=600)

    config = {'version': 'v1',
              'config': {'mapStyle': {'styleType': 'satellite'}}}

    # 添加数据到KeplerGL对象
    map_2.add_data(data=geojson_data2, name="中国AQI最低的前20个城市")
    map_2.config = config


    # 显示地图对象在Streamlit中
    keplergl_static(map_2,center_map=True)

if __name__ == "__main__":
    main()
