from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import openai  # OpenAI GPT API
from transformers import pipeline  # For multimodal AI like CLIP or image summarization
import os

# Initialize Flask app, spaCy NLP, and AI models
app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
CORS(app)

# OpenAI API setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Multimodal AI setup (example: using Hugging Face pipeline)
image_analysis = pipeline("image-classification", model="openai/clip-vit-base-patch32")

@app.route('/process_command', methods=['POST'])
def process_command():
    """Process voice/text commands and return actions or insights."""
    data = request.json
    command = data.get('command', '').lower()

    # Voice command actions
    if "scroll down" in command:
        return jsonify({"action": "scroll", "direction": "down"})
    elif "scroll up" in command:
        return jsonify({"action": "scroll", "direction": "up"})
    elif "click" in command:
        # Extract specific intents like clicking a link or button
        doc = nlp(command)
        if "link" in command:
            return jsonify({"action": "click", "target": "link"})
        elif "button" in command:
            return jsonify({"action": "click", "target": "button"})

    # AI-powered commands
    elif "summarize" in command:
        text = data.get('text', '')
        summary = summarize_text(text)
        return jsonify({"action": "summarize", "summary": summary})
    elif "describe image" in command:
        image_url = data.get('image_url', '')
        description = analyze_image(image_url)
        return jsonify({"action": "describe", "description": description})

    return jsonify({"error": "Command not recognized"}), 400

    

def summarize_text(text):
    """Generate a summary of the given text using OpenAI GPT."""
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"Summarize the following content: {text}",
            max_tokens=100
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error summarizing text: {str(e)}"

def analyze_image(image_url):
    """Analyze the image and generate a description using CLIP or similar model."""
    try:
        # Load the image and pass it through the pipeline
        results = image_analysis(image_url)
        descriptions = [f"{res['label']} ({res['score']*100:.2f}%)" for res in results]
        return "Detected objects: " + ", ".join(descriptions)
    except Exception as e:
        return f"Error analyzing image: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)