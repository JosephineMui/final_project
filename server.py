'''
This module sets up a Flask web application that provides an endpoint for emotion detection. 
It defines two routes: 
    1. '/emotionDetector' accepts a text input and returns the detected emotions and their scores
    2. '/' renders the main page of the application. The emotion detection is performed using the 
        emotion_detector function imported from the EmotionDetection module.   
The application is designed to run on localhost at port 5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    '''
    This function is the route handler for the '/emotionDetector' endpoint. 
    It retrieves the text to analyze from the query parameters, calls the 
    emotion_detector function to get the emotion scores, and returns a 
    formatted response with the dominant emotion and its score.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    scores = emotion_detector(text_to_analyze)

    # Check if the emotion detection returned an error
    if "error" in scores:
        return scores["error"]

    dominant = scores["dominant_emotion"]
    if dominant == "None":
        return "Invalid text! Please try again!"

    emotions = [f"'{emotion}': {score}" for emotion, score in scores.items()
                if emotion != "dominant_emotion"]
    joint = ", ".join(emotions)

    # Replace the last comma with "and" for better readability
    if ", " in joint:
        last_comma_index = joint.rfind(", ")
        joint = joint[:last_comma_index] + " and" + joint[last_comma_index + 1:]

    return (f"For the given statement, the system response is {joint}. "
            f"The dominant emotion is {dominant}.")

@app.route("/")
def render_index_page():
    '''
    This function is the route handler for the root endpoint ('/'). It renders the 
    index.html template, which serves as the main page of the application.
    '''
    # Render the index.html template as the main page of the application
    return render_template("index.html")

if __name__ == "__main__":
    # This function executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)
