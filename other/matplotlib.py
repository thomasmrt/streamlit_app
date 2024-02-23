import sys
sys.path.insert(0,r'C:\Users\Thomas\source\repos\fatigue-calculation-tool')


import streamlit as st
import pandas as pd
import OrcFxAPI as orca
import tkinter as tk
from tkinter import filedialog
from PIL import Image

from manual_calc import CalculateStress
import matplotlib.pyplot as plt
from math import sin, radians
import numpy as np
from path import Path


im = Image.open("assets/kraken.png")

st.set_page_config(
    page_title="Python Cheatsheet",
    page_icon=im,
    layout="wide",)
    
' # Matplotlib '

import streamlit as st
import time
i = st.slider('How old are you?', 0, 100, 50)


fig, axs = plt.subplots(2,2)
plt.subplots_adjust(wspace=0, hspace=0)
ax = axs[0,0]

ax2 = axs[1,0]
t = range(0,100)
curv_x = [sin(e/10) for e in t]
curv_y = np.zeros(len(t))
tension= np.zeros(len(t))


data = {'tension': tension,
        'curv_x': curv_x,
        'curv_y': curv_y}

stress_type = 'Bilinear'
stress_factors = {'Kt': 1,
                  'Kc': 0.5,
                  'Kcslip': 0.1,
                  'Kcstick':2,
                  'Ct': 0.2}
theta = 90
stress = CalculateStress(data, stress_type, stress_factors, theta)
ax.plot(curv_x, stress)
line, = ax2.plot(curv_x, [np.nan] * len(t))
the_plot = st.pyplot(plt)


def animate(i):  # update the y values (every 1000ms)
    line.set_xdata(curv_x[:i])
    line.set_ydata(t[:i])
    the_plot.pyplot(plt)


animate(i)