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
```
### Configuration

**Tesseract OCR Path**: Ensure that Tesseract OCR is installed on your system. Set the path to the Tesseract executable in the code if necessary. For example:

```python
pyt.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
```
**File Paths**: Make sure to update any file paths in the code as needed for your local environment.

## Usage

### Run the Application
Navigate to the directory where the v2.py file is located and run the Streamlit app using:

```bash
streamlit run v2.py
```
### Upload an image
Upload an image file (PNG, JPG, or JPEG) through the Streamlit interface.

### Adjust settings
- **CLAHE Clip Limit**: Adjust the clip limit for CLAHE. This controls the contrast limit, where higher values can provide more definition but might increase noise, while lower values offer more natural contrast.

- **CLAHE Tile Grid Size**: Set the grid size for CLAHE. This parameter defines the size of the grid used for histogram equalization, influencing the local contrast enhancement.

- **Contrast Alpha**: Set the contrast level. This parameter scales the contrast of the image, where higher values increase contrast and lower values reduce it.

- **Brightness Beta**: Set the brightness level. This parameter adjusts the brightness of the image, where positive values increase brightness and negative values decrease it.

- **Contour Area Threshold**: Define the threshold for contour area to remove handwriting. This setting determines the minimum contour area considered for handwriting removal; larger values will remove larger contours.

### Process the image
- **Click "Invert Colors"**: Invert the image colors if needed. This can help in improving OCR results by providing a different contrast and color profile.

- **Click "Run OCR"**: Extract text from the processed image using Optical Character Recognition (OCR). This step will analyze the image and convert any visible text into editable text.

- **Click "Create PDF"**: Generate a PDF of the extracted text. This allows you to save the recognized text in a document format.

- **Download the enhanced image or PDF**: Use the provided download buttons to save the enhanced image or the generated PDF to your local system.

### Example
Here's how the image processing pipeline works:

- **Original Image**: Upload an image with handwritten text.

- **Enhanced Image**: Process the image to remove handwritten text.

- **Inverted Image**: Optionally invert colors to see if it improves OCR results.

- **Extracted Text**: View and download the extracted text as a PDF.
