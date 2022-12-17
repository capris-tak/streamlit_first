import streamlit as st

st.title("Page C")
st.write("Page C")


st.code('''import platform
print(f"Python Version: {platform.python_version()}")
print(f'VER:{sys.version_info}')
print('OS : '+ platform.system())
print('OSリリース情報 : '+ platform.release())
print('OSバージョン情報 : '+ platform.version())
print('OSとバージョン : '+ platform.platform())



import sys
print('Pythonのバージョン情報 : '+ sys.version)
import numpy as np
print(np.__version__)#Numpyのバージョン確認
import pandas as pd
print(pd.__version__)#Pandasのバージョン確認


''')
