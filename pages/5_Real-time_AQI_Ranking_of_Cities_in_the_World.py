from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image

@st.cache
def crawl_data():
    # 设置Edge浏览器驱动路径
    browser = webdriver.Edge(executable_path=r'C:\appsforwebgis\msedgedriver.exe')

    # 打开网站
    browser.get("https://www.iqair.cn/cn/world-air-quality-ranking")

    # 获取页面源代码
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # 关闭浏览器
    browser.quit()

    table = soup.find("table", class_="mb30")

    # 创建CSV文件并写入标题行
    with open("city_ranking_of_world.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["排名", "城市", "美国AQI","关注度"])

        # 写入热门城市空气质量和污染排名
        for row in table.tbody.find_all("tr"):
            # 排名
            rank = row.find_all("td")[0].get_text().strip()
            # 城市
            location = row.find_all("td")[2].get_text().strip()
            # 空气质量指数
            aqi = row.find_all("td")[3].get_text().strip()
            # 关注度
            attention = row.find_all("td")[4].get_text().strip()
            # 写入CSV文件
            writer.writerow([rank, location, aqi , attention])



def load_data():
    # 读取CSV文件
    df = pd.read_csv("city_ranking_of_world.csv")
    return df

@st.cache
def get_dataframe():
    df = load_data()
    return df

# 爬取数据
crawl_data()

# 加载数据
df = get_dataframe()

# 获取当前北京时间的小时数
current_time = datetime.now().strftime("%Y年%m月%d日%H") + "时"

# 显示网页标题
st.title("世界热门城市AQI实时排名:eyes:")
st.markdown('<style>h1{color: pink;}</style>', unsafe_allow_html=True)

# 创建副标题，显示数据获取时间
st.caption(f"数据获取时间：{current_time}（北京时间）")

# 分页显示表格
page_size = 20  # 每页显示的数据条数
total_pages = len(df) // page_size + 1  # 总页数

# 获取当前页码
current_page = st.sidebar.number_input("当前页码", min_value=1, max_value=total_pages, value=1, step=1)

# 计算当前页数据的起止索引
start_idx = (current_page - 1) * page_size
end_idx = start_idx + page_size

# 显示当前页的表格数据
table_style = '''
    <style>
        table {
            border-collapse: collapse;
        }
        th {
            background-color: lavenderblush;
            color: white;
            font-weight: bold;
        }
        td, th {
            padding: 20px;
            border: 3px solid #cccccc;
        }
        tr:nth-child(even) {
            background-color: lavenderblush;
        }
        tr:nth-child(odd) {
            background-color: #ffffff;
        }
    </style>
'''
st.markdown(table_style, unsafe_allow_html=True)

# 创建新的数据框，只选择需要显示的列
display_df = df.iloc[start_idx:end_idx, [0, 1, 2, 3]]  # 选择排名、城市、美国AQI、关注度四列
st.table(display_df)

# 显示当前页码和总页数
st.sidebar.markdown(f"当前页码：{current_page}/{total_pages}")

# 输出完成信息
st.success("数据已成功加载和显示。")

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(current_dir, "photo_US_AQI.jpg")
image = Image.open(str(image_path),mode='r')
st.image(image, use_column_width=True)


