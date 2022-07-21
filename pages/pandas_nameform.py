import streamlit as st
import pandas as pd
import numpy as np

# ファイルのURL
u = "https://python.atelierkobato.com/wp-content/uploads/2019/08/name_s.csv"
# ファイルをデータフレームとして読み込む
data = pd.read_csv(u,  encoding="SHIFT-JIS")

st.write(str(len(data)))
st.dataframe(data.head(5))
