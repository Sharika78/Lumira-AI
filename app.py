import streamlit as st
import tensorflow as tf

# Page configuration
st.set_page_config(
    page_title="Lumira AI - Multi-Modal Medical Imaging",
    page_icon="🏥",
    layout="wide"
)

@st.cache_resource
def load_all_models():
    # Define direct resolve URLs from your Hugging Face repository
    neuro_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_neuro_model.h5"
    cardio_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_cardio_model.h5"
    bone_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_bone_model.h5"

    # Use Keras's built-in robust file downloader and loader
    neuro_path = tf.keras.utils.get_file("lumira_neuro_model.h5", neuro_url)
    cardio_path = tf.keras.utils.get_file("lumira_cardio_model.h5", cardio_url)
    bone_path = tf.keras.utils.get_file("lumira_bone_model.h5", bone_url)

    neuro = tf.keras.models.load_model(neuro_path, compile=False)
    cardio = tf.keras.models.load_model(cardio_path, compile=False)
    bone = tf.keras.models.load_model(bone_path, compile=False)
    
    return neuro, cardio, bone

# App Title and Description
st.title("Lumira AI - Multi-Modal Medical Imaging")
st.write("Welcome to Lumira AI! Please wait while the medical models are initialized.")

# Load models with a spinner
with st.spinner("Initializing Medical AI Models... Please wait."):
    neuro_model, cardio_model, bone_model = load_all_models()

st.success("All models loaded successfully!")

# Sidebar for navigation or modality selection
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the Medical Domain", ["Neuro (Brain)", "Cardio (Chest)", "Bone (Orthopedic)"])

if app_mode == "Neuro (Brain)":
    st.header("Brain Scan Analysis")
    st.write("Upload a brain MRI scan for neurological evaluation.")
    uploaded_file = st.file_uploader("Choose a Neuro image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Brain Scan", use_column_width=True)
        if st.button("Predict Neuro Model"):
            st.write("Running prediction...")

elif app_mode == "Cardio (Chest)":
    st.header("Cardio & Chest X-Ray Analysis")
    st.write("Upload a chest X-ray for cardiac and pulmonary evaluation.")
    uploaded_file = st.file_uploader("Choose a Cardio image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Chest X-Ray", use_column_width=True)
        if st.button("Predict Cardio Model"):
            st.write("Running prediction...")

elif app_mode == "Bone (Orthopedic)":
    st.header("Bone Fracture & Orthopedic Analysis")
    st.write("Upload an X-ray of bones for fracture detection.")
    uploaded_file = st.file_uploader("Choose a Bone image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Bone X-Ray", use_column_width=True)
        if st.button("Predict Bone Model"):
            st.write("Running prediction...")
