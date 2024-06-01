import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(URL, json=Input_json, headers=Headers)
        response.raise_for_status()  # Raise an exception if the API call fails
        formatted_response = json.loads(response.text)
        return formatted_response
    except requests.RequestException as e:
        print(f"Error calling the API: {e}")
        return None