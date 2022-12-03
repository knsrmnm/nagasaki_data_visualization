import streamlit as st

#config
st.set_page_config(
    page_title="nagasaki data map",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# top
st.title('ナガサキデータマップ')
st.markdown('#### Nagasaki city open data visualization')
st.caption('Version: 1.0.0 / Updated: 2022.12.03')
st.info('長崎市が公開しているオープンデータを可視化しています。https://odcs.bodik.jp/422011/', icon='📊')
st.write('#')

# sidebar
st.sidebar.caption('Developed by [mnmksr](https://www.instagram.com/_minadev/)')
