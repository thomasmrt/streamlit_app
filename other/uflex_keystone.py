

import streamlit as st
import pandas as pd
import OrcFxAPI as orca
import tkinter as tk
from tkinter import filedialog
import sys
sys.path.insert(0,r'C:\Users\Thomas\source\repos\uflex_keystone')
sys.path.insert(0,r'C:\Users\Thomas\source\repos\uflex_tools')
import os
from keystone import keystone
from PIL import Image
from path import Path 
from general import plot_geo, run_uflex
import matplotlib.pyplot as plt

app_temp = Path(os.getcwd()) / 'temp'
if not os.path.exists(app_temp):
    os.makedirs(app_temp)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


im = Image.open("assets/kraken.png")


st.set_page_config(
    page_title="Uflex keystone",
    page_icon=im,
    layout="wide",)
st.warning("Tool still in development", icon="⚠️")
' # UFLEX - Keystone'

st.write(help(keystone))

with st.container(border=True):
    ' ### Geometry definition'
    
    col1, col2, col3 = st.columns([0.4, 0.4, 0.2])

    with col1:
        conductor_diameter = st.number_input("Conductor diameter", value=44.7, min_value=0.0, format='%f')
        diameter_central =  st.number_input("Conductor central", value=11.5, min_value=0.0, format='%f')
        mat_name = st.text_input("Material name", value="COPPER")
        mesh_factor = st.number_input("Mesh factor", value=2, min_value=0)
        compaction_factor = st.number_input("Compaction factor", value=1, min_value=0)
    with col2:
        data = pd.DataFrame({'Number of strand': [12,17,22,27,32],
                                     'Pitch': [550, -550, 550, -550, 550],
                                     'GEOM name': ['GEOM1', 'GEOM2', 'GEOM3', 'GEOM4', 'GEOM5'],
                                     'CROSS name': ['CROSS1', 'CROSS', 'CROSS3', 'CROSS4', 'CROSS5'],

                                     }
                            )
                            
        edited_data = st.data_editor(data, num_rows="dynamic", use_container_width=True)

    with col3:
        if st.button('Generate keystone', type='primary'):
            st.session_state.clicked = True 
        

       
if st.session_state.clicked:
    with st.container(border=True):
        ' ### Output'
        
        col4, col5 = st.columns([0.5, 0.5])
        
        with col4:

            
            text =keystone(conductor_diameter, 
                     diameter_central, 
                     layers=[int(e) for e in edited_data['Number of strand'].values], 
                     pitchs=[float(e) for e in edited_data['Pitch'].values], 
                     material_name=mat_name, 
                     outfolder=None,
                     names_geom=edited_data['GEOM name'].values, 
                     names_cross=edited_data['GEOM name'].values, 
                     mesh_factor=mesh_factor, 
                     compaction_factor=compaction_factor)
                     
            st.code(text, language="python")
            uflex_file = app_temp / 'keystone.2if'
            with open(uflex_file, "a") as f:
                f.write( text)
            
            run_uflex(uflex_file)
            geo_file = uflex_file.replace('.2if','.geo')
            fig = plot_geo(geo_file)
            plt.axis('off')
            
        with col5:
        
            st.pyplot(fig=fig)


            
            