import pandas as pd
import streamlit as st

def creds_entered():
    if st.session_state["user"].strip() == "qrb@1234" and st.session_state["passwd"].strip() == "icai@1234":
          st.session_state["authenticated"] = True
    else:
          st.session_state["authenticated"] = False
          st.error("Invalid Username/Password  :face_with_raised_eyebrow:")

def authenticate_user():
       if "authenticated" not in st.session_state:
               st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
               st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
               return False
       else:
            if st.session_state["authenticated"]:
                 return True
            else:
                 st.text_input(label="Username :", value="", key="user", on_change=creds_entered)
                 st.text_input(label="Password :", value="", key="passwd", type="password", on_change=creds_entered)
                 return False
            
if authenticate_user():
      
      # Title of the app
      st.title("TR Review-Data Viewer")

      # Load Excel file (force first row as header)
      df = pd.read_excel("streamlit test.xlsx", header=1)

      # Show the dataframe in a bigger box
      st.dataframe(df, height=600, width=1000)