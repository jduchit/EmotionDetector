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
            # Parse the response JSON
            response_data = response.json()
            
            # Extract the required emotions and their scores
            emotions = response_data.get('emotion_predictions', [])
            emotion_scores = {emotion['emotion']: emotion['score'] for emotion in emotions}
            
            # Extract scores for anger, disgust, fear, joy, and sadness
            anger_score = emotion_scores.get('anger', 0)
            disgust_score = emotion_scores.get('disgust', 0)
            fear_score = emotion_scores.get('fear', 0)
            joy_score = emotion_scores.get('joy', 0)
            sadness_score = emotion_scores.get('sadness', 0)
            
            # Determine the dominant emotion
            scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(scores, key=scores.get)
            
            # Return the formatted output
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        else:
            # Return an error message if the request was not successful
            return f"Error: Failed to analyze emotion, status code: {response.status_code}"
    
    except requests.exceptions.Timeout:
        # Handle timeout exception
        return "Error: Request timed out"
    except requests.exceptions.RequestException as e:
        # Handle any other exceptions related to the request
        return f"Error: {e}"