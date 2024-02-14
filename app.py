import streamlit as st
import fitz

st.title('Comment extractor')


uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  doc = fitz.Document(uploaded_file)
  
  list_comments = []
  for i in range(doc.page_count):
      page = doc[i]
      for annot in page.annots():
  
        list_comments.append({'page': i+1, 
                              'author': annot.info['title'],
                              'type': annot.info['subject'],
                              'content': annot.info['content']})
  
  df = pd.DataFrame(list_comments)
  xl = df.to_excel()
  st.download_button(
    label="Download data as CSV",
    data=xl,
    file_name='large_df.xlsx',)

  doc.close()
