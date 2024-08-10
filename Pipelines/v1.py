import cv2
import streamlit as st
import numpy as np
from PIL import Image

# Title of the app
st.title("Document Contrast Enhancement with CLAHE and Handwriting Removal")

# Upload the image
uploaded_file = st.file_uploader("Choose a document image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert the uploaded file to an OpenCV image
    image = np.array(Image.open(uploaded_file).convert('L'))

    # Sidebar for CLAHE and contrast/brightness settings
    st.sidebar.header("CLAHE and Enhancement Settings")
    clip_limit = st.sidebar.slider("CLAHE Clip Limit", 1.0, 40.0, 4.0, 0.1)
    tile_grid_size = st.sidebar.slider("CLAHE Tile Grid Size", 2, 16, 8, 1)
    alpha = st.sidebar.slider("Contrast Alpha", 0.0, 50.0, 1.5, 0.01)
    beta = st.sidebar.slider("Brightness Beta", -255, 255, 0, 1)

    # Sidebar for handwriting removal settings
    st.sidebar.header("Handwriting Removal Settings")
    contour_area_threshold = st.sidebar.slider("Contour Area Threshold", 10, 500, 30, 1)

    # Create a CLAHE object (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_grid_size, tile_grid_size))

    # Apply CLAHE to the grayscale image
    clahe_image = clahe.apply(image)

    # Increase contrast using convertScaleAbs
    enhanced_image = cv2.convertScaleAbs(clahe_image, alpha=alpha, beta=beta)

    # Apply a binary inverse threshold to isolate the handwriting
    _, thresholded = cv2.threshold(enhanced_image, 100, 255, cv2.THRESH_BINARY_INV)

    # Find contours of the handwriting
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw white over the contours to "erase" the handwriting
    for contour in contours:
        if cv2.contourArea(contour) > contour_area_threshold:
            cv2.drawContours(enhanced_image, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    
    # Invert the colors
    # Convert the processed image back to PIL format for display in Streamlit
    handwriting_removed_image = Image.fromarray(enhanced_image)

    # Create two columns for side-by-side display
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.fromarray(image), caption='Original Image', use_column_width=True)

    with col2:
        st.image(handwriting_removed_image, caption='Handwriting Removed Image', use_column_width=True)

    # Option to download the processed image
    st.download_button(
        label="Download Enhanced Image",
        data=handwriting_removed_image.tobytes(),
        file_name="enhanced_document.jpg",
        mime="image/jpeg"
    )
