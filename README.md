# ID Document Fraud Detection System

## Project Overview
This project is a prototype system that analyzes an uploaded ID document image and generates a fraud risk report indicating whether the document may be genuine or suspicious.

The system uses a deep learning model to classify ID documents such as Aadhaar Card, Driving License, and PAN Card, and performs simple image quality analysis to detect potential tampering.

This project was developed as part of a technical assessment to demonstrate:
- Problem understanding
- AI-based document classification
- Fraud detection reasoning
- Model deployment using Streamlit and Docker

---

## Features

- Upload an ID document image
- Validate image format
- Detect document type (Aadhaar / Driving License / PAN Card)
- Perform basic tampering analysis
- Generate a structured fraud detection report
- User interface built with Streamlit
- Containerized deployment using Docker

---

## Technologies Used

- Python
- Streamlit
- ONNX Runtime
- OpenCV
- NumPy
- Pillow
- Docker

## Limitations

This prototype is designed for demonstration purposes. The goal is not perfect accuracy but to showcase the approach to document fraud detection and AI system integration.

---

## Future Improvements

- Add OCR for extracting document information
- Detect tampering using advanced forensic techniques
- Improve classification accuracy with larger datasets
- Deploy as a cloud API service
- Add authentication and logging

---

##Docker running code

docker run -p 8501:8501 id-fraud-detector

or

docker run -p 8501:8501 mrprabhul/id-fraud-detector

docker run -d -p 8501:8501 id-fraud-detector

docker run -d -p 8501:8501 --name id-fraud-app id-fraud-detector

docker ps

## Author

Prabhul P S  
AI / ML Engineer
