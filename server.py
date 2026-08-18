"""
Flask server application for Emotion Detection.
Provides routes to render the main web interface and analyze
input text using the Watson Emotion Detection package.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main web interface (index.html).
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def send_emotion_detector():
    """
    Receives text from query parameters, passes it to the emotion detector,
    and returns a formatted string response or an error message if invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    # Call the emotion detection function
    response = emotion_detector(text_to_analyze)
    # Check for invalid or blank inputs
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    # Format output for valid response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
