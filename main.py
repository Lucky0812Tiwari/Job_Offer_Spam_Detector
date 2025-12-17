from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pypdf import PdfReader
import io
import joblib

app = FastAPI()

# 1. ENABLE CORS - This prevents the "undefined" error in the browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load the model
# Ensure this file exists in the same folder
try:
    model = joblib.load("scam_model_v1.pkl")
except Exception as e:
    print(f"Error loading model: {e}")

# 3. Define the Request Body for text input
class JobOffer(BaseModel):
    content: str

@app.post("/predict")
async def predict_text(offer: JobOffer):
    probs = model.predict_proba([offer.content])[0]
    scam_chance = round(probs[1] * 100, 2)
    
    # Ensure the key "scam_score" matches your frontend script
    return {
        "status": "⚠️ SUSPICIOUS" if scam_chance > 50 else "✅ LEGITIMATE",
        "scam_score": f"{scam_chance}%",
        "detailed_warnings": ["Text analyzed by ML model."],
        "message": "Analysis complete."
    }

@app.post("/predict-pdf")
async def predict_pdf(file: UploadFile = File(...)):
    # 1. Validation: Ensure it's a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    # 2. Read file into memory
    content = await file.read()
    pdf_reader = PdfReader(io.BytesIO(content))
    
    extracted_text = ""
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + " "

    # 3. Check if PDF is image-based or empty
    if len(extracted_text.strip()) < 10:
        return {
            "status": "⚠️ UNREADABLE",
            "scam_score": "N/A",
            "detailed_warnings": ["This PDF appears to be a scanned image or empty. Our AI cannot read text inside images yet."],
            "message": "Please paste the text manually or provide a digital PDF."
        }

    # 4. Run ML Prediction
    probs = model.predict_proba([extracted_text])[0]
    scam_chance = round(probs[1] * 100, 2)
    
    # Returning the exact keys the frontend expects
    return {
        "status": "⚠️ SUSPICIOUS" if scam_chance > 50 else "✅ LEGITIMATE",
        "scam_score": f"{scam_chance}%",
        "detailed_warnings": ["Digital text detected and analyzed."],
        "message": f"Analyzed {len(pdf_reader.pages)} pages of the document."
    }