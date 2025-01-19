import streamlit as st
import os
from PIL import Image

# Directory to store uploaded pictures
UPLOAD_DIR = "uploaded_pictures"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Streamlit UI
st.title("Picture Browser, Uploader, and Predictor")

# Section to browse uploaded pictures
st.header("Uploaded Pictures")
uploaded_files = os.listdir(UPLOAD_DIR)

for file in uploaded_files:
    file_path = os.path.join(UPLOAD_DIR, file)
    image = Image.open(file_path)
    col1, col2, col3 = st.columns([3, 1, 1])
    
    with col1:
        st.image(image, caption=file, use_column_width=True)
    
    with col2:
        if st.button(f"Delete {file}", key=f"delete_{file}"):
            os.remove(file_path)
            st.warning(f"File '{file}' deleted successfully!")
            # Workaround: Use a form submission to reload the page
            st.write('<meta http-equiv="refresh" content="0; url=/" />', unsafe_allow_html=True)
    
    with col3:
        if st.button(f"Predict {file}", key=f"predict_{file}"):
            st.info(f"Prediction result for '{file}': [Prediction Placeholder]")

# Section to upload a new picture
st.header("Upload a New Picture")
uploaded_file = st.file_uploader("Choose a picture", type=["png", "jpg", "jpeg", "gif"])

if uploaded_file:
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' uploaded successfully!")
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # "Predict" button for the newly uploaded image
    if st.button("Predict Uploaded Image", key="predict_new"):
        st.info(f"Prediction result for '{uploaded_file.name}': [Prediction Placeholder]")



