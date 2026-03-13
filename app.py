import streamlit as st
import numpy as np
from PIL import Image
import cv2
import onnxruntime as ort

st.title("ID Document Fraud Detection")

# Load ONNX model
session = ort.InferenceSession("model.onnx")

classes = [
    "Aadhaar Card",
    "Driving License",
    "PAN Card"
]

uploaded_file = st.file_uploader(
    "Upload an ID Document Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    file_type = image.format

    st.success(f"Valid Image Type: {file_type}")

    img = np.array(image)

    # Convert to grayscale for quality analysis
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()

    quality = int(min((blur_score / 300) * 100, 100))

    # Prepare image for model
    img_resized = cv2.resize(img, (224,224))
    img_resized = img_resized / 255.0
    img_resized = np.expand_dims(img_resized, axis=0).astype(np.float32)

    # ONNX inference
    input_name = session.get_inputs()[0].name
    output = session.run(None, {input_name: img_resized})

    prediction = output[0]

    confidence = float(np.max(prediction))

    if quality < 60:
        doc_type = "It's not an ID Document"
    else:
        doc_type = classes[np.argmax(prediction)]

    if quality > 60:
        assessment = "Likely Genuine"
    else:
        assessment = "Suspicious Document"

    st.subheader("Fraud Detection Report")

    st.write("**Image Type:**", doc_type)
    st.write("**Quality:**", f"{quality}%")
    st.write("**Assessment:**", assessment)