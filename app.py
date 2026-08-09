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
    neuro_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_neuro_model.h5"
    cardio_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_cardio_model.h5"
    bone_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_bone_model.h5"

    neuro_path = tf.keras.utils.get_file("lumira_neuro_model.h5", neuro_url)
    cardio_path = tf.keras.utils.get_file("lumira_cardio_model.h5", cardio_url)
    bone_path = tf.keras.utils.get_file("lumira_bone_model.h5", bone_url)

    try:
        # safe_mode=False handles newer/older layer config arguments mismatch
        neuro = tf.keras.models.load_model(neuro_path, compile=False, safe_mode=False)
    except Exception as e:
        neuro = None
        st.error(f"Neuro Model Load Error: {e}")

    try:
        cardio = tf.keras.models.load_model(cardio_path, compile=False, safe_mode=False)
    except Exception as e:
        cardio = None
        st.error(f"Cardio Model Load Error: {e}")

    try:
        bone = tf.keras.models.load_model(bone_path, compile=False, safe_mode=False)
    except Exception as e:
        bone = None
        st.error(f"Bone Model Load Error: {e}")
    
    return neuro, cardio, bone

# App Title and Description
st.title("Lumira AI - Multi-Modal Medical Imaging")
st.write("Welcome to Lumira AI! Please wait while the medical models are initialized.")

# Load models with a spinner
with st.spinner("Initializing Medical AI Models... Please wait."):
    neuro_model, cardio_model, bone_model = load_all_models()

st.success("App initialized successfully!")

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
            if neuro_model is not None:
                st.write("Running prediction...")
            else:
                st.error("Neuro model is not loaded properly.")

elif app_mode == "Cardio (Chest)":
    st.header("Cardio & Chest X-Ray Analysis")
    st.write("Upload a chest X-ray for cardiac and pulmonary evaluation.")
    uploaded_file = st.file_uploader("Choose a Cardio image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Chest X-Ray", use_column_width=True)
        if st.button("Predict Cardio Model"):
            if cardio_model is not None:
                st.write("Running prediction...")
            else:
                st.error("Cardio model is not loaded properly.")

elif app_mode == "Bone (Orthopedic)":
    st.header("Bone Fracture & Orthopedic Analysis")
    st.write("Upload an X-ray of bones for fracture detection.")
    uploaded_file = st.file_uploader("Choose a Bone image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Bone X-Ray", use_column_width=True)
        if st.button("Predict Bone Model"):
            if bone_model is not None:
                st.write("Running prediction...")
            else:
                st.error("Bone model is not loaded properly.")
