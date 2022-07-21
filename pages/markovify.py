import streamlit as st

st.write('マルコフ連鎖で文章自動生成')
st.write('https://qiita.com/mapps/items/c0d3f1b73bc9ef398790')

#import Tokenizer
#import markovify
file = 'pages/Hermann_Hesse.txt' 
f = open(file, 'r', encoding="utf-8")
text = f.read()
#st.write(text)

from janome.tokenizer import Tokenizer
import pandas as pd
import collections
from wordcloud import WordCloud
