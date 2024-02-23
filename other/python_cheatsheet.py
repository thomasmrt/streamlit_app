import streamlit as st
import pandas as pd
import OrcFxAPI as orca
import tkinter as tk
from tkinter import filedialog
from PIL import Image
im = Image.open("assets/kraken.png")


st.set_page_config(
    page_title="Python Cheatsheet",
    page_icon=im,
    layout="wide",)
    

' # Python Cheatsheet'


' ### Multiprocessing'
code_str = """import multiprocessing as mp
import tqdm


def multiprocessing(task, inputs, nb_process):
    pool = mp.Pool(nb_process)
    
    data = []
    for result in tqdm.tqdm(pool.imap(task, inputs), total=len(inputs)):
        data.append(result)
    
    return data"""
    
st.code(code_str, language='python')