import streamlit as st
import pandas as pd
from st_pages import show_pages_from_config
from PIL import Image
import streamlit as st
import psutil
import time
im = Image.open("assets/kraken.png")


st.set_page_config(
    page_title="Home",
    page_icon=im,
    layout="wide",
)


show_pages_from_config(".streamlit/pages_sections.toml")



st.markdown(body='# Kraken tools', unsafe_allow_html=False)



cpu_percent = psutil.cpu_percent(interval=1)
st.metric(label="CPU usage", value=f"{cpu_percent} %")
   

memory_usage = psutil.virtual_memory()

st.metric(label="Memory usage", value=f"{memory_usage.percent} %")


my_bar = st.progress(0, text="")

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    progress_text = f"CPU usage: {cpu_percent}"

    my_bar.progress(cpu_percent/100, text=progress_text)