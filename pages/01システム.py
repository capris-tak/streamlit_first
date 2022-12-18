import streamlit as st
import platform
import sys

st.title("01 システム")


st.subheader("sys")
st.code('''
import sys
print('Python Version : '+ sys.version)
print(f'VER:{sys.version_info}')
''')
st.write('Python Version : '+ sys.version)
st.write(f'VER : {sys.version_info}')



st.subheader("platform")
st.code('''import platform
print(f"Python Version: {platform.python_version()}")
print('OS : '+ platform.system())
print('OSリリース情報 : '+ platform.release())
print('OSバージョン情報 : '+ platform.version())
print('OSとバージョン : '+ platform.platform())
''')
st.write(f"Python Version: {platform.python_version()}")
st.write('OS : '+ platform.system())
st.write('OSリリース情報 : '+ platform.release())
st.write('OSバージョン情報 : '+ platform.version())
st.write('OSとバージョン : '+ platform.platform())



