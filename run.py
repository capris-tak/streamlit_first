#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#cd Documents/JupytarNotebook
#jupyter nbconvert --to python run.ipynb
#streamlit run run.py


# In[1]:
import streamlit as st

import pandas as pd
import numpy as np

st.title('Home')
st.write('1 基本操作　　2 Streamlit　3 数学　4 文字文章操作　5 画像')


link = '[話題のPyScript！　HTMLファイルにPythonが書けるWebブラウザで動くPython](http://capris.html.xdomain.jp/python/index.html)'
st.markdown(link, unsafe_allow_html=True)
