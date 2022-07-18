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
st.caption('白黒写真をアップロードしてカラー化まで自動化する')

st.subheader('ローカルファイル読み込み')
image1 = Image.open('6450.jpg')
image2 = Image.open('colorize.jpg')
#st.image(image, caption='説明表示',use_column_width=True)
         
         
col1, col2 = st.columns(2)
with col1:
    st.header("gray/sepia")
    st.image(image1, use_column_width=True)
with col2:
    st.header("color")
    st.image(image2, use_column_width=True)

st.subheader('アップロードファイル読み込んで表示')
uploaded_file = st.file_uploader('selsect jpg image', type=['png', 'jpg', 'jpeg'] )
if uploaded_file is not None:
         img = Image.open(uploaded_file)
         st.image(img, caption='uploaded',use_column_width=True)

#処理にバイナリーデータで渡す場合
#import io
#with io.BytesIO() as output:
#         img.save(output, format='JPEG')
#         binary_img=output.getvalue()

code = """
import streamlit as st
st.title('title')
st.caption('caption')
st.subheader('subheader')
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




