# 🛡️ AI Fake Internship & Job Offer Detector

### 💡 Project Overview
This project is an **AI-powered security tool** designed to protect students and job seekers from recruitment scams. By leveraging **Machine Learning (NLP)** and a modern **FastAPI** backend, the application analyzes job descriptions or uploaded PDF offer letters to calculate a "Scam Probability" score and highlight potential red flags.

---

###1. 🚀 Key Features
* **Dual Analysis Modes:** Supports both raw text paste and **PDF document uploads**.
* **ML-Powered Scoring:** Uses a **Logistic Regression** model trained on 17,000+ data points to identify linguistic patterns of fraud.
* **Explainable AI:** Provides specific warnings (e.g., asking for security deposits or using unofficial communication channels).
* **OCR-Aware Logic:** Detects if a PDF is a scanned image (unreadable) and alerts the user.
* **Modern UI:** A responsive, dark-mode dashboard built with **Tailwind CSS** and featuring real-time loading states.

---

### 🧠 Technical Stack
* **Backend:**
    * **FastAPI:** High-performance REST API framework.
    * **Uvicorn:** ASGI server for running the application.
    * **Pydantic:** Data validation and settings management.
* **Machine Learning (NLP):**
    * **Scikit-Learn:** For the Logistic Regression classifier.
    * **TF-IDF Vectorization:** To convert text data into numerical features.
    * **Joblib:** For model serialization and persistence.
* **Frontend:**
    * **JavaScript (Fetch API):** For asynchronous communication with the backend.
    * **Tailwind CSS:** For professional styling.
* **Document Processing:**
    * **PyPDF:** To extract text layers from digital PDF documents.

---

### 🛠️ Installation & Setup

1. **Clone the Project:**
   ```bash
   git clone [https://github.com/yourusername/ai-scam-detector.git](https://github.com/yourusername/ai-scam-detector.git)
   cd ai-scam-detector

   2.Install Requirements: Make sure you have Python installed, then run:
   pip install fastapi uvicorn pydantic scikit-learn pandas joblib pypdf python-multipart

   3.Train the Machine Learning Model: Ensure fake_job_postings.csv is in the folder, then run:

   python train_model.py
   This creates the scam_model_v1.pkl file.

   4.Run the Backend Server:

   uvicorn main:app --reload

   The API will be live at http://127.0.0.1:8000.

   5.Open the Application: Simply open index.html in your web browser.

📊 Machine Learning Pipeline
Vectorization: The model uses TF-IDF to weigh words based on their importance. Suspicious words like "deposit," "wire," or "whatsapp" carry higher weights in scam detection.

Probability Calculation: Instead of a simple "Yes/No," the model uses predict_proba to provide a nuanced percentage of risk.

CORS Integration: The backend uses CORSMiddleware to securely allow the frontend to request data, preventing "undefined" errors in the browser.

📌 API Endpoints
Method	Endpoint	Description
POST	/predict	Analyzes raw text input from the user.
POST	/predict-pdf	Extracts and analyzes text from an uploaded PDF.


🌟 Future Scope
OCR Support: Integrating Tesseract to read text from scanned images/photos.

Browser Extension: Real-time scanning while browsing LinkedIn or Indeed.

Deep Learning: Transitioning to BERT transformers for better contextual understanding.
