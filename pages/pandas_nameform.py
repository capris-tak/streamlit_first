import streamlit as st
import pandas as pd

# ファイルのURL
u = "https://python.atelierkobato.com/wp-content/uploads/2019/08/name_s.csv"
# ファイルをデータフレームとして読み込む
data = pd.read_csv(u,  encoding="SHIFT-JIS")