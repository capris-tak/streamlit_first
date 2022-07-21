import streamlit as st
import pandas as pd
import numpy as np

# ファイルのURL
u = "https://python.atelierkobato.com/wp-content/uploads/2019/08/name_s.csv"
# ファイルをデータフレームとして読み込む
data = pd.read_csv(u,  encoding="SHIFT-JIS")

st.write(str(len(data)))
st.dataframe(data.head(5))

# 苗字(surname)の個数
ct_s = data["苗字"].count()
# 男性(male)の名前の個数
ct_m = data["名前(男)"].count()
# 女性(female)の名前の個数
ct_f = data["名前(女)"].count()

st.write(ct_s, ct_m, ct_f)
