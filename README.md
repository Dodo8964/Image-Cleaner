# Handwritten Text Remover

This project provides a pipeline for removing handwritten text from images and recreating the cleaned document into a PDF format. The application is built using OpenCV, pytesseract, and Streamlit.

## Features

- **Image Processing Pipeline**:
  - **Contrast Limited Adaptive Histogram Equalization (CLAHE)**: Enhances the contrast of the image to highlight distinguishing features of the text.
  - **Brightness and Contrast Adjustment**: Further enhances the image using the formula `image = image * alpha + beta`, where `alpha` represents contrast and `beta` represents brightness.
  - **Handwriting Removal**: Uses contour area thresholding to identify and remove handwritten text based on contour sizes.

- **Additional Features**:
  - **Color Inversion**: Invert image colors to potentially improve OCR accuracy.
  - **Download Enhanced Image**: Option to download the processed image with handwritten text removed.
  - **OCR Text Recognition**: Extracts text from the processed image using Optical Character Recognition (OCR).
  - **Create and Download PDF**: Option to create and download a PDF file containing the extracted text.

## Installation

To set up and run the application, you need to install the following Python packages:

- `opencv-python`
- `streamlit`
- `numpy`
- `Pillow`
- `pytesseract`
- `fpdf`

You can install these packages using pip:

```bash
pip install opencv-python streamlit numpy pillow pytesseract fpdf
