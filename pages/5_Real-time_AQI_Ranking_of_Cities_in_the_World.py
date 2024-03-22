import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image

with st.spinner("正在加载数据，请稍候..."):
    import time
    time.sleep(2)

@st.cache
def crawl_data():
    url = "https://www.iqair.cn/cn/world-air-quality-ranking"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    data = []
    for row in table.tbody.find_all("tr"):
        rank = row.find_all("td")[0].get_text().strip()
        city = row.find_all("td")[2].get_text().strip()
        aqi = row.find_all("td")[3].get_text().strip()
        attention = row.find_all("td")[4].get_text().strip()
        data.append([rank, city, aqi, attention])

    with open("city_ranking_of_world.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["排名", "城市", "美国AQI","关注度"])
        writer.writerows(data)


def load_data():
    df = pd.read_csv("city_ranking_of_world.csv")
    return df


@st.cache
def get_dataframe():
    df = load_data()
    return df


crawl_data()

df = get_dataframe()

current_time = datetime.now().strftime("%Y年%m月%d日%H") + "时"

st.title("世界热门城市AQI实时排名:eyes:")
st.markdown('<style>h1{color: pink;}</style>', unsafe_allow_html=True)

st.caption(f"数据获取时间：{current_time}（北京时间）")

page_size = 20
total_pages = len(df) // page_size + 1

current_page = st.sidebar.number_input("当前页码", min_value=1, max_value=total_pages, value=1, step=1)

start_idx = (current_page - 1) * page_size
end_idx = start_idx + page_size

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

display_df = df.iloc[start_idx:end_idx, [0, 1, 2, 3]]
st.table(display_df)

st.sidebar.markdown(f"当前页码：{current_page}/{total_pages}")

st.success("数据已成功加载和显示。")

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "photo_US_AQI.jpg")
image = Image.open(str(image_path), mode='r')
st.image(image, use_column_width=True)
