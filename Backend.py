from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import openai  # OpenAI GPT API
from transformers import pipeline  # For multimodal AI like CLIP or image summarization
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

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
    print(f"Received command: {command}")  # Debug print

    if not command:
        return jsonify({"error": "No command provided"}), 400

    # Voice command actions

    #page selection commands
    if "home page" in command or "go to home" in command or "homepage" in command:
        return jsonify({"action": "navigate", "target": "home"})
    elif "demo page" in command or "go to demo" in command:
        return jsonify({"action": "navigate", "target": "demo"})
    elif "about page" in command or "go to about" in command:
        return jsonify({"action": "navigate", "target": "about"})
    elif "download page" in command or "go to download" in command:
        return jsonify({"action": "navigate", "target": "download"})

    # scroll commands
    if "scroll down" in command:
        return jsonify({"action": "scroll", "direction": "down"})
    elif "scroll up" in command:
        return jsonify({"action": "scroll", "direction": "up"})
    # click commands
    elif "click" in command:
        # NLP processing for button clicks
        doc = nlp(command)
        print("Parsed tokens:")  # Debugging parsed tokens
        for token in doc:
            print(f"{token.text} -> {token.pos_}, {token.dep_}, like_num: {token.like_num}")

        button_number = None

        # Extract the button number or ordinal
        for token in doc:
            if token.text == "button":
                prev_token = doc[token.i - 1] if token.i > 0 else None
                next_token = doc[token.i + 1] if token.i + 1 < len(doc) else None

                # Check the previous or next token for a number or ordinal
                if next_token and (next_token.like_num or next_token.text in {"first", "second", "third", "fourth", "fifth"}):
                    ordinal_map = {
                        "first": "1",
                        "second": "2",
                        "third": "3",
                        "fourth": "4",
                        "fifth": "5"
                    }
                    button_number = ordinal_map.get(next_token.text, next_token.text)  # Use mapped value or direct number
                elif prev_token and (prev_token.like_num or prev_token.text in {"first", "second", "third", "fourth", "fifth"}):
                    ordinal_map = {
                        "first": "1",
                        "second": "2",
                        "third": "3",
                        "fourth": "4",
                        "fifth": "5"
                    }
                    button_number = ordinal_map.get(prev_token.text, prev_token.text)  # Use mapped value or direct number
                break

        if button_number:
            print(f"Button number extracted: {button_number}")  # Debug print
            return jsonify({"action": "click", "target": f"button{button_number}"})
        else:
            print("Button number not found or invalid.")  # Debug print
            return jsonify({"error": "Invalid button command"}), 400

    print(f"Command not recognized: {command}")  # Debug print
    return jsonify({"error": "Command not recognized"}), 400

if __name__ == "__main__":
    app.run(debug=True)
