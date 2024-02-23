# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:37:11 2023

@author: Thomas
"""

#!/usr/bin/env python
import sys
import fitz
from path import Path
import pandas as pd
import xlwings as xw
import pandas as pd


import tkinter as tk  
from tkinter import filedialog  


from PIL import Image
import streamlit as st

im = Image.open("assets/kraken.png")


st.set_page_config(
    page_title="Comments extractor",
    page_icon=im,
    layout="wide",
)


help="""
This tools allows you to simply extract comments from a PDF file in csv format

"""

st.markdown(body=' # Comments extractor', unsafe_allow_html=False, help=help)


def select_folder():
   root = tk.Tk()
   root.attributes('-topmost',True)
   root.withdraw()
   folder_path = filedialog.askopenfilename(master=root)
   # root.destroy()
   return folder_path

st.write('Select the PDF file to extract comments from')


selected_folder_path = st.session_state.get("folder_path", None)
folder_select_button = st.button("Select File")
if folder_select_button:
    selected_folder_path = select_folder()
    st.session_state.folder_path = selected_folder_path
      
if selected_folder_path:

    doc = fitz.Document(selected_folder_path)
   
    list_comments = []
    for i in range(doc.page_count):
        page = doc[i]
        for annot in page.annots():
          print(annot.line_ends)
          list_comments.append({'page': i, 
                                'author': annot.info['title'],
                                'type': annot.info['subject'],
                                'content': annot.info['content']})
    
    df = pd.DataFrame(list_comments)
    
    st.write('List of comments')
    st.dataframe(df, use_container_width=True)