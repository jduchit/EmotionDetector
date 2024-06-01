import requests

def emotion_detector(text_to_analyze):
    # Define the URL for the EmotionPredict endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers for the HTTP request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Define the payload containing the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send a POST request to the EmotionPredict endpoint
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the 'text' attribute from the response JSON
            return response.json()['text']
        else:
            # Return an error message if the request was not successful
            return "Error: Failed to analyze emotion"
    except Exception as e:
        # Return an error message if an exception occurs during the request
        return f"Error: {e}"