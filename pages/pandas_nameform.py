import streamlit as st
import pandas as pd
import numpy as np

# ファイルのURL
u = "https://python.atelierkobato.com/wp-content/uploads/2019/08/name_s.csv"
# ファイルをデータフレームとして読み込む
data = pd.read_csv(u,  encoding="SHIFT-JIS")

st.write(str(len(data)))
st.dataframe(data.head(5))

st.write('苗字surnameの個数',data["苗字"].count())
st.write('男性maleの名前の個数',data["名前(男)"].count())
st.write('女性femaleの名前の個数 ',data["名前(女)"].count())
