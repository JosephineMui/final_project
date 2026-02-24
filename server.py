from flask import Flask, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    scores = emotion_detector(text_to_analyze)
    return jsonify(f"For the given statement, the system response is {scores}")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Render the index.html template as the main page of the application
    return render_template("index.html")

if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)

    # Run the Flask app with debug mode enabled for development purposes
    # app.run(debug=True)