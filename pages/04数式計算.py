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


st.code('100 + Rational(3,21)')
st.latex(100 + Rational(3,21))



st.write('関数を定義 𝑓(𝑥)=𝑥2')
st.code('''
def f(x):
    return x**2
f(x)''')
def f(x):
    return x**2
st.latex(f(x))

st.code('f(sqrt(A)*3)')
st.latex(f(sqrt(A)*3))




st.code('x**2 + 3*x*y + 2*y**2')
st.latex(x**2 + 3*x*y + 2*y**2)


st.write('factor 関数で因数分解')
st.code('''
eq = x**2 + 3*x*y + 2*y**2
factor(eq)
''')
eq = x**2 + 3*x*y + 2*y**2
st.latex(factor(eq))





