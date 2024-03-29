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
st.write('')




st.subheader("chr関数を利用してアスキーコードを文字列に変換")
st.code('''
[chr(x) for x in range(97,123)]  #英小文字
''')
ascstr = ','.join([chr(x) for x in range(97,123)])
st.write(ascstr)
st.write('')
st.write('')








st.subheader("string.ascii_lowercase")
st.code('''
import string
a_z = string.ascii_lowercase
print(a_z)

import itertools
tttt = []
kkkk = itertools.product(a_z, repeat=4)
for i in kkkk:
    combi = i[0]+i[1]+i[2]+i[3]
    tttt.append(combi+ '00001')
print(len(tttt))
print(tttt[-20:])
''')
import string
a_z = string.ascii_lowercase
st.write(a_z)

import itertools
tttt = []
kkkk = itertools.product(a_z, repeat=4)
for i in kkkk:
    combi = i[0]+i[1]+i[2]+i[3]
    tttt.append(combi+ '00001')
st.write(len(tttt))
st.write(tttt[-20:])
st.write('')
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
st.write('')
st.write('')



st.subheader("re 正規表現2")
st.code('''
import re
s_text = 'RoboCop eats baby food. BABY FOOD'
vowel_regex = re.compile(r'[aeiouAEIOU]') #母音のみ指定
print(vowel_regex.findall(s_text))
consonant_regex = re.compile(r'[^aeiouAEIOU]') #　^キャレット記号：補集合＝以外
print(consonant_regex.findall(s_text))

## ^〜で始まる  $〜で終わる　.一文字(ワイルドカード、改行以外、含む場合はre.DOTALLを第二引数)
## 大文字小文字を区別しない　re.I  (=re.IGNORECASE)
''')
import re
s_text = 'RoboCop eats baby food. BABY FOOD'
vowel_regex = re.compile(r'[aeiouAEIOU]')
st.write(vowel_regex.findall(s_text))
consonant_regex = re.compile(r'[^aeiouAEIOU]') #キャレット記号：補集合＝以外
st.write(consonant_regex.findall(s_text))
st.write('')
st.write('')



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
print(d)
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

    
    
    
    
    
    
    
    
st.subheader("ベン図")
st.code('''
import random
list1 = [chr(random.randint(97,122)) for x in range(12)]
list2 = [chr(random.randint(97,122)) for x in range(12)]
s1 = set(list1)
print(sorted(s1))
s2 = set(list2)
print(sorted(s2))
print('和集合：', sorted(s1 | s2) )# .union(s2)
print('積集合：', sorted(s1.intersection(s2)) )# &が&amp;に変換され記号は失敗
print('差s1-2集合：', sorted(s1 - s2) )# .difference(s2)
print('対称差集合：', sorted(s1 ^ s2) )#.symmetric_difference(s2)
#辞書型からリストに戻す　 list(s1_s2)
''')
import random
list1 = [chr(random.randint(97,122)) for x in range(12)]
list2 = [chr(random.randint(97,122)) for x in range(12)]
s1 = set(list1)
st.write(sorted(s1))
s2 = set(list2)
st.write(sorted(s2))
st.write('和集合：', sorted(s1 | s2) )# .union(s2)
st.write('積集合：', sorted(s1.intersection(s2)) )# &が&amp;に変換され記号は失敗
st.write('差s1-2集合：', sorted(s1 - s2) )# .difference(s2)
st.write('対称差集合：', sorted(s1 ^ s2) )#.symmetric_difference(s2)
from PIL import Image
image = Image.open('pages/venn.png')
st.image(image, caption='Venn diagram')
st.write('')
st.write('')
