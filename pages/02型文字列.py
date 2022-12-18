import streamlit as st

st.title("02 型文字列")


st.subheader(".isXXX")
st.code('''
print(r'That is \n \t \\ Carol\'s cat.')
print('hello123'.isalpha())#英語のみ
print('hello123'.isalnum())#英語と数字のみ
print('123'.isdecimal())#数字のみ
''')
st.write(r'That is \n \t \\ Carol\'s cat.')
st.write('hello123'.isalpha())
st.write('hello123'.isalnum())
st.write('123'.isdecimal())
st.write('')




st.subheader("re 正規表現")
st.code('''
import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #　\d\d\d　は　\d{3}　と書ける
mo = phone_num_regex.search('私の電話番号は415-555-4242です。あとは123-456-7890です。')
print('見つかった番号は' + mo.group())
fao = phone_num_regex.findall('私の電話番号は415-555-4242です。あとは123-456-7890です。')
print('見つかった番号は' + str(fao))

## \d数字 \w単語 \s空白　\D \W \Sはそれら以外
## (xx)? 0-1回      (xx)* 0〜      (xx)+ 1〜
## (Ha){3} HaHaHa          (Ha){3,5} HaHaHa  |  HaHaHaHa|  |  HaHaHaHaHa
## 貪欲greedyマッチ HaHaHaHaHa   非貪欲マッチ HaHaHa  (Ha){3,5}?
''')
import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #　\d\d\d　は　\d{3}　と書ける
mo = phone_num_regex.search('私の電話番号は415-555-4242です。あとは123-456-7890です。')
st.write('見つかった番号は' + mo.group())
fao = phone_num_regex.findall('私の電話番号は415-555-4242です。あとは123-456-7890です。')
st.write('見つかった番号は' + str(fao))



st.subheader("zipでリスト型（list）を辞書型(dictionary)にする")
st.code('''
# リスト
adr_no = ['150-0013','150-0021','150-0022']
address = ['東京都渋谷区恵比寿','東京都渋谷区恵比寿西','東京都渋谷区恵比寿南']
# リストを辞書へ統合
adr_dict = dict(zip(adr_no,address))
print(adr_dict)
for ad_key,ad_val in adr_dict.items():
    print(ad_key,ad_val)
''')
adr_no = ['150-0013','150-0021','150-0022']
address = ['東京都渋谷区恵比寿','東京都渋谷区恵比寿西','東京都渋谷区恵比寿南']
adr_dict = dict(zip(adr_no,address))
st.write(adr_dict)
for ad_key,ad_val in adr_dict.items():
    st.write(ad_key,ad_val)
st.write('')
    
    
st.subheader("defaultdict")
st.code('''
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)

from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
d
''')
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
st.write(d)

from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
st.write(d)
st.write('')

    
