from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_predictor(text_to_analyse)
    emotion_predictions = response['emotionPredictions'][0]['emotion']
    return f"For the given statement, the system response is\
            'anger': {emotion_predictions['anger']},\
            'disgust': {emotion_predictions['disgust']},\
            'fear': {emotion_predictions['fear']},\
            'joy': {emotion_predictions['joy']},\
            'sadness': {emotion_predictions['sadness']}. The \
            dominant emotion is {dominant_emotion}"
    

@app.route('/')
def render_index_page():
    '''
    Initiate the rendering of main application over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)