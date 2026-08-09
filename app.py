import os
import urllib.request
import streamlit as st
import tensorflow as tf

@st.cache_resource
def get_model(file_name, url):
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(url, file_name)
    return tf.keras.models.load_model(file_name)

@st.cache_resource
def load_all_models():
    neuro_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_neuro_model.h5"
    cardio_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_cardio_model.h5"
    bone_url = "https://huggingface.co/sharika17/lumira-models/resolve/main/lumira_bone_model.h5"

    neuro = get_model('lumira_neuro_model.h5', neuro_url)
    cardio = get_model('lumira_cardio_model.h5', cardio_url)
    bone = get_model('lumira_bone_model.h5', bone_url)
    return neuro, cardio, bone

# Add a spinner while models load
with st.spinner("Initializing Medical AI Models... Please wait."):
    neuro_model, cardio_model, bone_model = load_all_models()
