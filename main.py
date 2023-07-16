import streamlit as st
import pandas as pd
import numpy as np

#config
st.set_page_config(
    page_title="Nagasaki City Data",
    page_icon="🥷",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "# Nagasaki City Data Visualization!"
    }
)

# top
st.title('Nagasaki City Data 2023')
st.write(
    """
    [![Follow](https://img.shields.io/badge/Threads-@knsrmnm-lightblue)](https://www.threads.net/knsrmnm)
    [![Follow](https://img.shields.io/badge/Instagram-@knsrmnm-pink)](https://www.instagram.com/knsrmnm)
    [![Follow](https://img.shields.io/github/followers/knsrmnm?style=social&label=Follow)](https://github.com/knsrmnm)
    """
)
st.write('#')
st.info('このWebサイトは長崎市が公開しているオープンデータを利用しています。', icon="ℹ️")

st.write('#')
st.write(
    """
    ### 人口動態（各年）
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=["男性", "女性"]
    )
st.bar_chart(chart_data)

st.write('#')
st.write(
    """
    ### 外国人人口
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)
chart_data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["🇨🇳中国", "🇰🇷韓国", "🇺🇸アメリカ"])
st.bar_chart(chart_data)

st.write('#')
st.write(
    """
    ### 転入・転出
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)

st.divider()

st.write('#')
st.write(
    """
    ### AED設置箇所
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)
st.metric(label="設置箇所数", value="70 箇所")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

st.write('#')
st.write(
    """
    ### 公衆無線LANアクセスポイント
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)
st.metric(label="アクセスポイント数", value="70 箇所")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

st.write('#')
st.write(
    """
    ### 文化財
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)
st.metric(label="総数", value="70")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)