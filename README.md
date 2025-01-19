# NW-Hacks-2025
 Submission for NW Hacks 2025
# Navis - Accessibility Awareness

Navis is an innovative web accessibility tool that leverages multimodal AI and voice commands to enhance user navigation and interaction with websites. It features a dynamic interface with voice-enabled commands for seamless interaction, making web content more accessible to users with disabilities.

## Features

- **Voice Commands**: Navigate and interact with the website using intuitive voice commands.
  - **Scroll**: "Scroll up", "Scroll down"
  - **Click**: "Click button X" (where X is a button number, e.g., "Click button 1")
  - **Navigate**: "Go to page X" (e.g., "Go to Home", "Go to Demo")
- **Dynamic Styling**: Gradient color changes for page backgrounds and taskbars.
- **Multimodal AI**: Backend powered by OpenAI and Hugging Face models for advanced command recognition and processing.

---

## Installation and Setup

### Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **Node.js (for Tailwind setup, if needed)**

### Required Python Packages

Install the following dependencies using `pip`:

```bash
pip install flask flask-cors spacy transformers openai python-dotenv
```

## Setting Up OpenAI API Key
1. Create a `.env` file in the project root directory.
2. Add your OpenAI API key to the file:

   ```bash
   OPENAI_API_KEY=your-openai-api-key
   ```
## Usage

### Running the Backend

1. Start the backend server by running:

   ```bash
   python app.py
   ```
2. The server will be hosted at http://127.0.0.1:5000.

### Running the Frontend
1. Open home.html in your browser to start the application.
2. Navigate through the pages (Home, About, Demo) using the top navigation bar.
## Voice Commands

The following voice commands are supported:

- **Scroll Commands**:
  - `"Scroll up"` → Scrolls the page up.
  - `"Scroll down"` → Scrolls the page down.

- **Click Commands**:
  - `"Click button X"` → Clicks a specific button, where X is the button number (e.g., `"Click button 1"`).

- **Navigation Commands**:
  - `"Go to Home"`
  - `"Go to About"`
  - `"Go to Demo"`
  - `"Go to Download"`
## Credits

This project uses the following tools and technologies:

- [Tailwind CSS](https://tailwindcss.com/): For styling the frontend.
- [Google Fonts (Open Sans)](https://fonts.google.com/): For web typography.
- [OpenAI API](https://openai.com/): For natural language understanding.
- [Hugging Face Transformers](https://huggingface.co/transformers/): For multimodal AI (e.g., image classification with CLIP).
- [Flask](https://flask.palletsprojects.com/): For creating the backend API.
- [spaCy](https://spacy.io/): For command processing and NLP.

---

## Future Enhancements

- Integrate more voice commands for granular control.
- Add support for more multimodal AI features like image and audio analysis.
- Improve UI responsiveness for accessibility.
## License

This project is licensed under the MIT License. 

