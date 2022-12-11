import streamlit as st

#config
st.set_page_config(
    page_title="Nagasaki Data Map",
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
st.title('😎 Nagasaki Data Map')
st.write(
    """
    [![Follow](https://img.shields.io/twitter/follow/mnmksr?style=social)](https://www.twitter.com/mnmksr)
    [![Follow](https://img.shields.io/github/followers/Ken46373?style=social&label=Follow)](https://github.com/Ken46373)
    """
)

st.info(
    """
    このWebサイトは長崎市が公開している[オープンデータ](https://odcs.bodik.jp/422011/)を使用しています。
    """,
    icon="🚀",
)
st.success(
    """
    免責事項
    """,
    icon="✅",
)

st.write('#')

st.write(
    """
    ### How to use - 使い方 - 
    Welcome to our roadmap! 👋 This app shows some projects we're working on or have 
    planned for the future. Plus, there's always more going on behind the scenes — we 
    sometimes like to surprise you ✨
    """
)


# sidebar
st.sidebar.caption('Version: 1.0.0 / Updated: 2022.12.03')