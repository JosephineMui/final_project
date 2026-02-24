from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')

    scores = emotion_detector(text_to_analyze)

    dominant = scores["dominant_emotion"]
    emotions = [f"'{emotion}': {score}" for emotion, score in scores.items() if emotion != "dominant_emotion"]
    joint_emotions = ", ".join(emotions)

    # Replace the last comma with "and" for better readability
    if ", " in joint_emotions:
        last_comma_index = joint_emotions.rfind(", ")
        joint_emotions = joint_emotions[:last_comma_index] + " and" + joint_emotions[last_comma_index + 1:]
    return f"For the given statement, the system response is {joint_emotions}. The dominant emotion is {dominant}."

@app.route("/")
def render_index_page():
    # Render the index.html template as the main page of the application
    return render_template("index.html")

if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)
