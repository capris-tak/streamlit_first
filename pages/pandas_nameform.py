import streamlit as st
import pandas as pd
import numpy as np

# ファイルのURL
u = "https://python.atelierkobato.com/wp-content/uploads/2019/08/name_s.csv"
# ファイルをデータフレームとして読み込む
data = pd.read_csv(u,  encoding="SHIFT-JIS")

st.write(str(len(data)))
st.dataframe(data.head(5))

st.write('苗字surnameの個数:',str(data["苗字"].count()))
st.write('男性maleの名前の個数:',str(data["名前(男)"].count()))
st.write('女性femaleの名前の個数:',str(data["名前(女)"].count()))

#男性  乱数シードを設定
np.random.seed(10)
# 乱数を生成
rd_s = np.random.randint(0, ct_s)
rd_m = np.random.randint(0, ct_m)
# 氏名を作成
name = data.loc[rd_s, "苗字"]\
       + " " + data.loc[rd_m, "名前(男)"]
# ふりがな(phonetic)を作成
ph = data.loc[rd_s, "ふりがな1"]\
     + " " + data.loc[rd_m, "ふりがな2"]
# 氏名とふりがなをタプルにまとめる
name = (name, ph)
st.write(name)
