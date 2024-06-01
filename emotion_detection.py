import requests

def emotion_detector(text_to_analyze):
    # Define the URL for the EmotionPredict endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the headers for the HTTP request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Define the payload containing the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    try:
        # Send a POST request to the EmotionPredict endpoint with a timeout of 10 seconds
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the 'emotion_predictions' attribute from the response JSON
            return response.json()
        else:
            # Return an error message if the request was not successful
            return f"Error: Failed to analyze emotion, status code: {response.status_code}"
    
    except requests.exceptions.Timeout:
        # Handle timeout exception
        return "Error: Request timed out"
    except requests.exceptions.RequestException as e:
        # Handle any other exceptions related to the request
        return f"Error: {e}"