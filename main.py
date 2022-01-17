import streamlit as st
import datetime
import requests

CATEGORIES = ['社会保障・衛生', '環境', '人口・世帯', '教育・文化・スポーツ・生活', '情報通信・科学技術']

# top
st.title('🦄長崎市オープンデータ可視化')
st.markdown('#### Nagasaki city open data visualization')
now = datetime.datetime.now()
strnow = now.strftime('%Y.%m.%d %H:%M:%S')
st.caption('最終更新 : ' + strnow)
st.info('📝長崎市が公開しているオープンデータを可視化しています。https://odcs.bodik.jp/422011/')
st.write('#')

# sidebar
category = st.sidebar.selectbox('カテゴリ選択', CATEGORIES)
st.sidebar.write('###')
st.sidebar.markdown('** 📖 利用方法 **')
question1 = st.sidebar.expander('question1')
question1.write('answer1')
question2 = st.sidebar.expander('question2')
question2.write('answer2')
question3 = st.sidebar.expander('question3')
question3.write('answer3')
st.sidebar.markdown('***')
st.sidebar.write('###')
st.sidebar.markdown('** ✏️ Release note **')
release_note = '''
v1.0.0
2022.01.17
'''
st.sidebar.code(release_note, language='text')
st.sidebar.caption('developed by [kenshiro minami](https://note.com/minamidev/)')

# main
st.markdown('#### ●' + str(category))
# url = 'https://data.bodik.jp/api/3/action/datastore_search?resource_id=db2b21b0-6470-4771-9661-332eeac4d2fc&limit=5'
# res = requests.get(url)
# st.write(res.json())
