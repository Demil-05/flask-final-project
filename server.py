''' Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask('Emotion Detector')
@app.route('/emotionDetector')
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_predictor()
        function. The output returned shows the emotions, their scores
        and the dominant emotion for the provided text.'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_predictor(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again."
    return f"For the given statement, the system response is\
                'anger': {response['anger']},\
                'disgust': {response['disgust']},\
                'fear': {response['fear']},\
                'joy': {response['joy']},\
                'sadness': {response['sadness']}.\
                The dominant emotion is {response['dominant_emotion']}"
@app.route('/')
def render_index_page():
    '''Initiate the rendering of main application over the Flask channel'''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
