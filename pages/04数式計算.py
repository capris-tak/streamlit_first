import streamlit as st
from sympy import *
from sympy.abc import *

st.title("数式")

st.write('Latex')

st.code('''
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
''')

#積分∫3𝑥2𝑑𝑥
#integrate(3*x**2, x)
