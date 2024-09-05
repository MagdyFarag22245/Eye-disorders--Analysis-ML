import numpy as np
import pandas as pd
import streamlit as st # type: ignore
import base64

# Page content
st.markdown("<h1 style='text-align: center;'>Eye-disorders</h1>", unsafe_allow_html=True)

st.markdown('''<h6 style='text-align: center;'>
    This app is created to analyze and predict Eye disorders</h6>''', unsafe_allow_html=True)

# Function to load and encode the image
def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return encoded_image

# Load the image from the path
image_path = "D:/Study/Epsilon DS/Eye-Project/sources/eye_gif.gif"
encoded_image = load_image(image_path)

# Centering the image using HTML with st.markdown
st.markdown(
    f"""
    <div style='display: flex; justify-content: center;'>
        <img src='data:image/gif;base64,{encoded_image}' style='width:50%; height:auto;'/>
    </div>
    """,
    unsafe_allow_html=True
)


# Function to load and encode the image
# import base64

# # Function to load and encode the image
# def load_image(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_image = base64.b64encode(image_file.read()).decode()
#     return encoded_image

# # Load the image from the path
# image_path = "D:/Study/Epsilon DS/Eye-Project/sources/eye_gif.gif"
# encoded_image = load_image(image_path)

# # Centering the images side-by-side using HTML with st.markdown
# st.markdown(
#     f"""
#     <div style='display: flex; justify-content: center;'>
#         <div style='flex: 1; display: flex; justify-content: center;'>
#             <img src='data:image/gif;base64,{encoded_image}' style='width:60%; height:auto;'/>
#         </div>
#         <div style='flex: 1; display: flex; justify-content: center;'>
#             <img src='data:image/gif;base64,{encoded_image}' style='width:60%; height:auto;'/>
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

