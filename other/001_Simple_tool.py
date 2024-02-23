import streamlit as st
import pandas as pd
import OrcFxAPI as orca
from PIL import Image

if 'stage' not in st.session_state:
    st.session_state.stage = 0
    
def load_files(df):
    
    
    st.session_state.stage = 1
    for k, row in df.iterrows():
        
         m = orca.Model(row['Load case filename'])
         print('success')
        
    return None

im = Image.open("assets/kraken.png")


st.set_page_config(
    page_title="Fatigue calculation",
    page_icon=im,
    layout="wide",
)
st.warning("Tool still in development")
st.write("# Fatigue calculation tools")

tabs = st.tabs(["Load cases", "Components", "Analysis data", "SN curves"])

with tabs[0]:
    
    data = pd.DataFrame(columns=['Load case filename',
                                 'Line name',
                                 'From',
                                 'To',
                                 'Exposure time',
                                 ]
                        )


    
    edited_df = st.data_editor(data, num_rows="dynamic", use_container_width=True)
    
    st.write("Number of cases :", len(edited_df.index))
    
    st.button('Load', on_click=load_files, args=[edited_df])
    
    if st.session_state.stage >= 1:
        st.write('stage 1')


with tabs[1]:


    option = st.selectbox(
       "Stress calculation method",
       ('Linear', 'Bilinear', 'Bilinear with hysteresis'))

    st.write('You selected:', option)
    
    
    
    if option=='Linear':
        sf_cols = ['Kt', 'Kc']
    else:
        sf_cols = ['Kt', 'Kcstick', 'Kcslip', 'Ct']
    
    cols = ['Component name', *sf_cols, 'SN curve', 'Fatigue limit']

    data = pd.DataFrame(columns = cols)
    
    edited_df = st.data_editor(data, num_rows="dynamic")
    
with tabs[2]:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)