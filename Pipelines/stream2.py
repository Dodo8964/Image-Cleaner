import cv2
import numpy as np
import streamlit as st
from PIL import Image

def process_image(image, alpha, beta):
    # Apply the contrast and brightness adjustments
    g_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary inverse threshold to isolate the handwriting
    _, thresholded = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours of the handwriting
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw white over the contours to "erase" the handwriting
    for contour in contours:
        if cv2.contourArea(contour) > 30:  # You can adjust this value as needed
            cv2.drawContours(image, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    
    # Invert the colors
    inverted_image = cv2.bitwise_not(image)
    
    return inverted_image

st.title("Handwriting Removal and Inversion")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    ori = image.copy()

    # Sidebar sliders for alpha and beta values
    alpha = st.sidebar.slider("Contrast (alpha)", 0.0, 10.0, 0.7, 0.1)
    beta = st.sidebar.slider("Brightness (beta)", -100, 100, 10, 1)
    
    # Process image
    result_image = process_image(image, alpha, beta)
    
    # Display images
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original Image")
        st.image(ori, use_column_width=True)
    
    with col2:
        st.header("Processed Image")
        st.image(result_image, use_column_width=True)
    
    # Save the result image
    result_pil = Image.fromarray(result_image)
    result_pil.save('handwriting_removed_and_inverted.png')
    st.write("Image saved as handwriting_removed_and_inverted.png")
