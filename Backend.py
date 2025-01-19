from flask import Flask,  request, jsonify
from flask_cors import CORS
import spacy

# Initialize Flask app and spaCy NLP
app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
CORS(app)

@app.route('/process_command', methods=['POST'])
def process_command():
    # Get the command from the frontend
    data = request.json
    command = data.get('command', '').lower()

    # Process the command
    if "scroll down" in command:
        return jsonify({"action": "scroll", "direction": "down"})
    elif "scroll up" in command:
        return jsonify({"action": "scroll", "direction": "up"})
    elif "click" in command:
        # Extract intent, e.g., "Click the first link"
        doc = nlp(command)
        if "link" in command:
            return jsonify({"action": "click", "target": "link"})
        elif "button" in command:
            for token in doc:
                if token.like_num:  # Checks if the token is a number
                    button_number = int(token.text)
                    return jsonify({"action": "click", "target": f"button{button_number}"})
            return jsonify({"error": "Button number not found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
