import streamlit as st
from sympy import *
from sympy.abc import *

st.title("数式")

st.write('Latex')

st.write('')
st.code('''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.write('積分 ∫3𝑥2𝑑𝑥')
st.code('integrate(3*x**2, x)')
st.latex(integrate(3*x**2, x))



st.code('x**2 + 3*x*y + 2*y**2')
st.latex(r'''x**2 + 3*x*y + 2*y**2''')
