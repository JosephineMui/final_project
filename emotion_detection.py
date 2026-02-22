import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#Input json: { "raw_document": { "text": text_to_analyse } }

def emotion_detector(text_to_analyze):
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.text
    else:
        return {"error": "Failed to fetch emotion data"}