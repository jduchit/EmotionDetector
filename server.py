import os
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Get the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        # Return an error if no text is provided
        return jsonify({"error": "No text provided for analysis"}), 400

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    if isinstance(result, dict):
        # Format the output as required
        response_text = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        )
        # Return the formatted response
        return jsonify({"response": response_text})
    else:
        # Return an error if there was an issue with emotion detection
        return jsonify({"error": "Error in emotion detection"}), 500

if __name__ == '__main__':
    # Set Flask environment to production to suppress warning
    os.environ['FLASK_ENV'] = 'production'
    
    # Run the Flask application using Gunicorn server
    app.run(host='0.0.0.0', port=8080, threaded=True)