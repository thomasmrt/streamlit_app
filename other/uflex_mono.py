import sys
sys.path.insert(0,r'C:\Users\Thomas\source\repos\uflex_tools\postpro\mono')
from post_mono_UPDATE import post_results

from path import Path
import streamlit as st
import pandas as pd
import OrcFxAPI as orca
import tkinter as tk
from tkinter import filedialog


from PIL import Image
im = Image.open("assets/kraken.png")


st.set_page_config(
    page_title="Uflex mono",
    page_icon=im,
    layout="wide",)
st.warning("Tool still in development")

def select_file():
   root = tk.Tk()
   root.attributes('-topmost',True)
   root.withdraw()
   file_path = filedialog.askopenfilename(master=root)
   # root.destroy()
   return file_path


def run_calculation():

    return None


' # UFLEX - Monophase cable'

tabs = st.tabs(["Inputs", "Results"])
selected_folder_path = None
with tabs[0]:

    with st.container(border=True):


        col1, col2 = st.columns([0.01,0.99])


        with col2:
            """General 
            """
            
            nb_process = st.number_input("Number of process", value=4, min_value=0)
            convergence_target = st.number_input("Convergence target", value=0.001, min_value=0.000001, format='%f')

            st.write('Select UFLEX template file')
            
            file_select_button = st.button("Select File")
            if file_select_button:
                selected_folder_path = select_file()
                
            st.info('Result folder will be created in the same folder as basefile model', icon="ℹ️")
            
            
        
            
        
    with st.container(border=True):
        

        col1, col2 = st.columns([0.01,0.99])

        with col1:
            ea = st.checkbox("", value=True)
        with col2:
            """Axial stiffness assessment        
            """
        
            if ea:
                st.selectbox('Boundary condition', ['Both', 'Free rotation', 'Ends fixed'])
                nb_steps = st.number_input("Number of steps", value=40, min_value=0)
                data = pd.DataFrame(columns=['Tension',]  )


                st.write('Tensions applied')
                edited_df = st.data_editor(data, num_rows="dynamic", use_container_width=True)
    st.button('Run calculation', type='primary', on_click=run_calculation)
                
if selected_folder_path:
    with tabs[1]:
        folder = Path(selected_folder_path).parent
        res = post_results(folder)
        
        df = pd.concat(res['EA'])
        df['case'] = df.apply(lambda row: row["tension_level"] + ' ' +row["condition_limit"], axis=1)
        
        df = df[df['strain']>=0]
        import plotly.express as px

       
        fig = px.line(df, x="strain", y="tension", color='case')

        st.plotly_chart(fig, theme=None, use_container_width=True)
            
