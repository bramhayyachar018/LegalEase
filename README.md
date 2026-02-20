# ⚖️ LegalEase – AI-Powered Legal Documentation Generator

LegalEase is a web-based Generative AI application that dynamically generates structured legal documents such as employment contracts, lease agreements, NDAs, and more using the Google Gemini API.

This project demonstrates secure API integration, full-stack development using Flask, and real-time AI-powered content generation.

---

## 🚀 Project Overview

LegalEase allows users to:

- Select a document type
- Enter relevant party details
- Submit required information
- Instantly generate professionally structured legal documents

The application integrates Google’s Gemini large language model to create legally formatted documents based on structured user input.

---

## 🛠 Technologies Used

 Backend
- **Python 3.x**
- **Flask** – Lightweight web framework
- **Google Generative AI (Gemini API)** – AI document generation
- **google-genai SDK** – Official Gemini Python SDK
- **python-dotenv** – Secure environment variable management

# Frontend
- **HTML5**
- **CSS3**
- **JavaScript (Vanilla JS)**
- **Fetch API** – For asynchronous POST requests

# Development Tools
- **Virtual Environment (venv)**
- **Git & GitHub** – Version control

## 🏗 System Architecture

1. User fills form on frontend.
2. JavaScript sends data via POST request using Fetch API.
3. Flask backend receives structured JSON data.
4. Backend constructs a dynamic prompt.
5. Prompt is sent to Gemini model (`gemini-flash-latest`).
6. AI-generated document is returned as structured JSON.
7. Frontend dynamically renders the document.

---

## 📂 Project Structure

```
LegalEase/
│
├── app.py                
├── requirements.txt      
├── .env                  
│
├── templates/
│   └── index.html        
│
└── static/
    └── style.css        
```

---


## 📄 Supported Document Types

- Employment Contract
- Lease Agreement
- Non-Disclosure Agreement (NDA)
- Service Agreement
- Partnership Agreement
- Loan Agreement
- Freelance Contract

(The system can be extended to support more document types.)

---

## 🎨 UI Features

- Modern responsive layout
- Dynamic field labels based on document type
- Loading indicator
- Button disable during generation
- Smooth animations
- Styled document display section

---

## 🧠 AI Integration

- Uses Google Gemini model: `gemini-flash-latest`
- Prompt engineering ensures:
  - Structured clauses
  - Proper headings
  - Confidentiality section
  - Termination clause
  - Governing law
  - Signature block

---

## 🧩 Key Functionalities

- POST-based document generation
- Structured JSON responses
- Error handling with proper HTTP status codes
- Frontend validation before submission

---

## 📈 Future Improvements

- PDF download feature
- Document history storage
- User authentication
- Cloud deployment (Render / Railway / GCP)
- Enhanced document formatting

---

## 🎓 Academic Context

This project was developed as part of a Google Cloud Generative AI initiative to demonstrate:

- Secure API integration
- Full-stack web development
- Generative AI implementation
- Prompt engineering
- Modern UI/UX practices
