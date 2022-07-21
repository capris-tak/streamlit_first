import streamlit as st
import pandas as pd

st.subheader('氏名自動生成')

# ファイルのURL
u = "https://python.atelierkobato.com/wp-content/uploads/2019/08/name_s.csv"
# ファイルをデータフレームとして読み込む
data = pd.read_csv(u,  encoding="SHIFT-JIS")

st.write(str(len(data)),' 個のデータ')
st.dataframe(data)

st.write('苗字surnameの個数:',str(data["苗字"].count()))
st.write('男性maleの名前の個数:',str(data["名前(男)"].count()))
st.write('女性femaleの名前の個数:',str(data["名前(女)"].count()))

# 苗字(surname)の個数
ct_s = data["苗字"].count()
# 男性(male)の名前の個数
ct_m = data["名前(男)"].count()
# 女性(female)の名前の個数
ct_f = data["名前(女)"].count()


import numpy as np
def name_generator():    
    # 苗字(surname)の個数
    ct_s = data["苗字"].count()    
    # 男性(male)の名前の個数
    ct_m = data["名前(男)"].count()
    # 女性(female)の名前の個数
    ct_f = data["名前(女)"].count()
    
    # 性別をランダムに選択
    sex = np.random.choice(["f", "m"])    
    # 乱数を生成("苗字"の行番号)
    rd_s = np.random.randint(0, ct_s)
    
    if sex == "m":
        k = 2
        sex_label = "男"
        rd_n = np.random.randint(0, ct_m)
    else:
        k = 4
        sex_label = "女"
        rd_n = np.random.randint(0, ct_f)

    # データフレームの配列にアクセス
    dv = data.values
    # 氏名とふりがなを作成
    name = dv[rd_s, 0] + " " + dv[rd_n, k]
    ph = dv[rd_s, 1] + " " + dv[rd_n, k + 1]
    # 関数の戻り値
    return (name, ph, sex_label)

np.random.seed(0)
for i in range(20):
    name = name_generator()
    st.write(str(i+1),str(name))
