import requests
from bs4 import BeautifulSoup
import csv

with st.spinner("正在加载数据，请稍候..."):
    import time
    time.sleep(5)

# 发送请求并获取响应
url = "https://www.air-level.com/rank"
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.content, "html.parser")
tag = soup.find_all(class_='table table-hover table-condensed text-center')
data1 = []
data2 = []
a = 0
for i in tag:
    rows = i.find_all('tr')
    for row in rows:
        cols = row.find_all("td")
        if a > 0 and a <= 20:
            rank = cols[0].text.strip()
            city = cols[1].text.strip()
            aqi = cols[2].text.strip()
            quality = cols[3].text.strip()
            data1.append([rank, city, aqi, quality])
        if a > 21 and a <= 42:
            rank = cols[0].text.strip()
            city = cols[1].text.strip()
            aqi = cols[2].text.strip()
            quality = cols[3].text.strip()
            data2.append([rank, city, aqi, quality])
        a += 1

# 将数据保存为csv文件
with open("air_quality_ranking_worst.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "城市", "AQI", "空气质量等级"])
    for d in data1:
        writer.writerow(d)

with open("air_quality_ranking_best.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "城市", "AQI", "空气质量等级"])
    for d in data2:
        writer.writerow(d)
print("数据已写入csv文件")

# 读取CSV文件并创建写入文件对象
with open("air_quality_ranking_worst.csv", mode="r", encoding="utf-8") as f1, \
        open("air_quality_ranking_worst_location.csv", mode="w", encoding="utf-8", newline="") as f2:
    reader = csv.reader(f1)
    writer = csv.writer(f2)

    # 写入标题行和经纬度列的标题
    writer.writerow(next(reader) + ["纬度", "经度"])

    # 遍历每个城市，获取经纬度信息并写入CSV文件
    for row in reader:
        city_name = row[1]
        print(f"正在获取 {city_name} 的经纬度...")

        # 调用百度地图API获取经纬度信息
        url = f"http://api.map.baidu.com/geocoding/v3/?address={city_name}&city={city_name}&output=json&ak=fY4FeIfYcwsXsvUKkGXe6X3MF4Au0Z8y"
        response = requests.get(url)
        data = response.json()

        # 解析结果并写入CSV文件
        if data["status"] == 0 and data["result"]:
            lnglat = data["result"]["location"]
            writer.writerow(row + [lnglat["lat"], lnglat["lng"]])
        else:
            writer.writerow(row + ["", ""])
            print(f"{city_name} 经纬度获取失败！")

print("AQI最高城市经纬度获取完成！")

# 读取CSV文件并创建写入文件对象
with open("air_quality_ranking_best.csv", mode="r", encoding="utf-8") as f3, \
        open("air_quality_ranking_best_location.csv", mode="w", encoding="utf-8", newline="") as f4:
    reader = csv.reader(f3)
    writer = csv.writer(f4)

    # 写入标题行和经纬度列的标题
    writer.writerow(next(reader) + ["纬度", "经度"])

    # 遍历每个城市，获取经纬度信息并写入CSV文件
    for row in reader:
        city_name = row[1]
        print(f"正在获取 {city_name} 的经纬度...")

        # 调用百度地图API获取经纬度信息
        url = f"http://api.map.baidu.com/geocoding/v3/?address={city_name}&city={city_name}&output=json&ak=fY4FeIfYcwsXsvUKkGXe6X3MF4Au0Z8y"
        response = requests.get(url)
        data = response.json()

        # 解析结果并写入CSV文件
        if data["status"] == 0 and data["result"]:
            lnglat = data["result"]["location"]
            writer.writerow(row + [lnglat["lat"], lnglat["lng"]])
        else:
            writer.writerow(row + ["", ""])
            print(f"{city_name} 经纬度获取失败！")

print("AQI最低城市经纬度获取完成！")


import streamlit as st
import pandas as pd
import geopandas as gpd
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from datetime import datetime

# 获取当前北京时间的小时数
current_time = datetime.now().strftime("%Y年%m月%d日%H") + "时"

# 创建一个网页标题为"中国AQI最高的前20个城市"，颜色为褐红色
st.title("中国AQI最高的前20个城市:woman-facepalming:")
st.markdown('<style>h1{color: salmon;}</style>', unsafe_allow_html=True)

# 创建副标题，显示数据获取时间
st.caption(f"数据获取时间：{current_time}（北京时间）")

def main():
    # 读取CSV文件
    data = pd.read_csv("air_quality_ranking_worst_location.csv")

    # 过滤掉经纬度为空的数据
    data = data.dropna(subset=["纬度", "经度"])

    # 创建Geopandas GeoDataFrame
    geometry = gpd.points_from_xy(data['经度'], data['纬度'])
    gdf = gpd.GeoDataFrame(data, geometry=geometry)

    # 将GeoDataFrame转换为GeoJSON格式
    geojson_data1 = gdf.to_json()

    # 创建KeplerGL地图对象
    map_1 = KeplerGl(height=600)

    config = {'version': 'v1',
              'config': {'mapStyle': {'styleType': 'satellite'}}}

    # 添加数据到KeplerGL对象
    map_1.add_data(data=geojson_data1, name="中国AQI最高的前20个城市")
    map_1.config = config


    # 显示地图对象在Streamlit中
    keplergl_static(map_1,center_map=True)

if __name__ == "__main__":
    main()














