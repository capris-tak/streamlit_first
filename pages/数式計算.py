import streamlit as st
from sympy import *
from sympy.abc import *

st.write("Page B")


#積分∫3𝑥2𝑑𝑥
integrate(3*x**2, x)
