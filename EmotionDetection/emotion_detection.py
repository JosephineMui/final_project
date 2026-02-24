import json
import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    # Check if the input text is empty or blank
    # if not text_to_analyze.strip():
    #     return {"message": "Input text is empty or blank. Please provide valid text for emotion detection."}

    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, headers=HEADERS, json=payload)
    if response.status_code == 400:
        return {"anger": "None",     
                "disgust": "None",
                "fear": "None",
                "joy": "None",
                "sadness": "None",
                "dominant_emotion": "None"}
    
    scores = {}
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]
        for emotion, score in emotions["emotion"].items():
            scores[emotion] = score

        max_key = max(scores, key=scores.get)
        scores["dominant_emotion"] = max_key
        return scores
    else:
        return {"error": "Failed to fetch emotion data"}