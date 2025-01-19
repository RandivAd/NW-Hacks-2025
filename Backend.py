from flask import Flask, request, jsonify
import spacy

# Initialize Flask app and spaCy NLP
app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

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
            return jsonify({"action": "click", "target": "button"})
    return jsonify({"error": "Command not recognized"}), 400

if __name__ == "__main__":
    app.run(debug=True)
