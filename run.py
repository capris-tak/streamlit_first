#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#cd Documents/JupytarNotebook
#jupyter nbconvert --to python run.ipynb
#streamlit run run.py


# In[1]:
import streamlit as st
from PIL import Image

st.title('ファイル処理や文字表示のテスト')
st.caption('画像表示')
st.subheader('ローカルファイル読み込み')
image = Image.open('6450.jpg')
st.image(image, caption='説明表示',use_column_width=True)
         
         
         
code = """
import streamlit as st
st.title('streamlitでWebアプリを最速で作ってネット公開)
st.caption('サプーの')
st.subheader('VTuber サプー')
#画像
image = Image.open('wordcloud.png')
st.image(image, width=500)
#動画
video_file = video('XXXXX.mov', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
"""
st.code(code, language='python')


#テキストボックス
name = st.text_input('名前')
print(name)

#ボタン

#複数選択
hobby = st.multiselect(
    '趣味',
    ('スポーツ','読書','プログラミング','映画鑑賞','釣り','料理'))


# In[ ]:





# In[ ]:




