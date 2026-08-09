import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# --- Page Config & Custom CSS for Background Animation ---
st.set_page_config(page_title="Lumira AI", layout="wide")

# Custom CSS for the animated background
# It uses a gentle diagonal gradient animation that is non-distracting
animated_bg_css = """
<style>
    /* Targeting the main content area */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
    }

    /* Targeting the sidebar area for a consistent feel */
    [data-testid="stSidebar"] {
        background-color: rgba(20, 25, 40, 0.9); /* Translucent dark for sidebar */
    }

    /* Keyframes for the gradient flow animation */
    @keyframes gradientAnimation {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    
    /* Making text and elements more readable against the animated bg */
    h1, h2, h3, h4, h5, h6, .stMarkdown {
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }
    
    /* Customizing the diagnostic result boxes for clarity */
    .stAlert {
        border-radius: 10px;
    }
</style>
"""

# Inject the custom CSS
st.markdown(animated_bg_css, unsafe_allow_html=True)

# --- App Title and UI Elements ---
st.title("🏥 Lumira AI - Multi-Modal Medical Imaging Diagnosis")

# Load Models
@st.cache_resource
def load_all_models():
    # Note: LFS may be required if these files are too large
    neuro = tf.keras.models.load_model('lumira_neuro_model.h5')
    cardio = tf.keras.models.load_model('lumira_cardio_model.h5')
    bone = tf.keras.models.load_model('lumira_bone_model.h5')
    return neuro, cardio, bone

# Add a spinner while models load
with st.spinner("Initializing Medical AI Models... Please wait."):
    neuro_model, cardio_model, bone_model = load_all_models()

# Sidebar Setup
st.sidebar.header("Scan Parameters")
module_type = st.sidebar.selectbox(
    "Select Scan Type",
    ["Brain / Neuro (CT/MRI)", "Chest / Cardio (X-Ray)", "Bone / Ortho (X-Ray)"]
)
st.sidebar.info("This is an AI decision support system.")

# Main UI
uploaded_file = st.file_uploader("Upload Medical Scan Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Use context manager for PIL Image
    with Image.open(uploaded_file).convert('RGB') as image:
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Uploaded Scan", use_container_width=True)
        
        with col2:
            st.subheader("Diagnostic Result")
            
            # Preprocessing
            resized_img = image.resize((150, 150))
            img_array = np.array(resized_img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            # Inference Logic
            if st.button("Analyze Image"):
                # Use a new spinner for inference
                with st.spinner(f"Analyzing {module_type} scan..."):
                    if "Neuro" in module_type:
                        pred = neuro_model.predict(img_array)[0][0]
                        # Assume 0 is tumor based on previous chat interaction
                        status = "Tumor / Lesion Detected" if pred < 0.5 else "Normal (No Abnormality)"
                        confidence = (1 - pred) if pred < 0.5 else pred
                    elif "Cardio" in module_type:
                        pred = cardio_model.predict(img_array)[0][0]
                        # Assume 0 is cardiomegaly based on previous interaction
                        status = "Cardiomegaly / Abnormality Detected" if pred < 0.5 else "Normal (Healthy Heart)"
                        confidence = (1 - pred) if pred < 0.5 else pred
                    else: # Bone
                        pred = bone_model.predict(img_array)[0][0]
                        # Threshold updated to pred < 0.5 as requested
                        status = "Fracture Detected" if pred < 0.5 else "Normal (No Fracture)"
                        confidence = (1 - pred) if pred < 0.5 else pred
                
                # Display Output with improved clarity against animated bg
                st.write("---")
                if "Detected" in status:
                    st.error(f"**Result:** {status}", icon="⚠️")
                else:
                    st.success(f"**Result:** {status}", icon="✅")
                    
                st.info(f"**Model Confidence:** {confidence * 100:.2f}%", icon="📊")

else:
    # Instructions if no file uploaded
    st.info("👈 Please select a scan type and upload an image to begin.")
