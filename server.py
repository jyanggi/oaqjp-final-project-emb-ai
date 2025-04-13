"""
This is the server script for the Emotion Detection application. 
It uses Flask to provide a web service that allows users to input text and get 
the analysis of emotions from the text.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index page.

    This function returns the index.html template where users can input text 
    for emotion analysis.

    Returns:
        html: The index.html template for the user interface.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """
    Processes the text input from the user, runs emotion detection, and 
    returns the analysis result.

    If no input is provided, the function will return a 400 error with a 
    message. If the dominant emotion is None, an error message is returned.

    Returns:
        json: JSON response containing the emotion analysis or an error message.
    """
    try:
        text_to_analyze = request.json.get('text_to_analyze', '').strip()

        if not text_to_analyze:
            return jsonify({
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }), 400

        emotion_data = emotion_detector(text_to_analyze)
        if emotion_data.get('dominant_emotion') is None:
            return jsonify({'message': 'Invalid text! Please try again!'}), 400

        return jsonify(emotion_data)

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500


if __name__ == '__main__':
    """
    Starts the Flask app to run the server on localhost at port 5000.

    This will make the application accessible at http://127.0.0.1:5000.
    """
    app.run(debug=True)
