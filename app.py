import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client (Latest SDK)
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_document():
    try:
        data = request.get_json()

        document_type = data.get("document_type")
        party_one = data.get("party_one")
        party_two = data.get("party_two")
        start_date = data.get("start_date")
        additional_terms = data.get("additional_terms")

        # Basic validation
        if not document_type or not party_one or not party_two:
            return jsonify({
                "status": "error",
                "message": "Required fields are missing."
            }), 400

        prompt = f"""
        Generate a professionally structured {document_type}.
        Do NOT leave placeholders. Fill realistic values if needed.

        Party One: {party_one}
        Party Two: {party_two}
        Start Date: {start_date}
        Additional Terms: {additional_terms}

        Include:
        - Clear headings
        - Numbered clauses
        - Confidentiality clause
        - Termination clause
        - Governing law
        - Signature section
        """

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return jsonify({
            "status": "success",
            "document": response.text
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)