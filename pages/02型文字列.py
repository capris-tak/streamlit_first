import streamlit as st

st.title("02 型文字列")


st.subheader(".isXXX")
st.code('''
#print(r'That is \n \t \\ Carol\'s cat.')
print('hello123'.isalpha())#英語のみ
print('hello123'.isalnum())#英語と数字のみ
print('123'.isdecimal())#数字のみ
''')
st.write(r'That is \n \t \\ Carol\'s cat.')
st.write('hello123'.isalpha())
st.write('hello123'.isalnum())
st.write('123'.isdecimal())




