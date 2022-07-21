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
st.write("This is a sample home page in the apps.")
st.markdown("### Sample Data")

link = '[話題のPyScript！](http://capris.html.xdomain.jp/python/index.html)'
st.sidebar.markdown(link, unsafe_allow_html=True)
st.sidebar.write('HTMLファイルにPythonが書けるWebブラウザで動くPython')

