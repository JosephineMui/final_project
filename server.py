from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    scores = emotion_detector(text_to_analyze)
    return jsonify(f"For the given statement, the system response is {scores}")