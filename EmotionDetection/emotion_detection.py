import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    # Send request to Watson NLP API
    response = requests.post(url, json=payload, headers=headers)
    
    # Convert response text to a Python dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the dictionary containing all emotion scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Determine the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the target dictionary format
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }