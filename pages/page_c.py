import streamlit as st
import platform

st.title("Page C")

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


st.subheader("sys")
st.code('''
import sys
print('Pythonのバージョン情報 : '+ sys.version)
print(f'VER:{sys.version_info}')
import numpy as np
print(np.__version__)#Numpyのバージョン確認
import pandas as pd
print(pd.__version__)#Pandasのバージョン確認
''')
