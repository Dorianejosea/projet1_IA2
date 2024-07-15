import streamlit as st
from PIL import Image
import numpy as np
import cv2
import os
from descriptor import glcm, bitdesc

def calculate_histogram(image):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist
def calculate_features(image, descriptor):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    if descriptor == 'GLCM':
        return glcm(image)
    elif descriptor == 'BiT':
        return bitdesc(image)
    else:
        return calculate_histogram(image)

st.title("Application de téléversement et sélection d'images")

uploaded_files = st.file_uploader("Veuillez choisir des images s'il vous plait...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"Nombre d'images téléchargées : {len(uploaded_files)}")

    num_images = st.slider("Sélectionnez le nombre d'images à afficher", 1, len(uploaded_files), 1)

    st.write(f"Affichage des {num_images} premières images :")
    for i, uploaded_file in enumerate(uploaded_files[:num_images]):
        image = Image.open(uploaded_file)
        st.image(image, caption=f'Image {i+1}', use_column_width=True)
