import unittest
from emotion_detection import emotion_predictor

class testEmotionDetector(unittest.TestCase):
    def test_emotion_predictor(self):
        result1 = emotion_predictor('I am glad this happened')
        self.assertEqual(result1['dominant_emotion'], 'joy')
        
        result2 = emotion_predictor('I am really mad about this')
        self.assertEqual(result2['dominant_emotion'], 'anger')
        
        result3 = emotion_predictor('I feel disgusted just hearing about this')
        self.assertEqual(result3['dominant_emotion'], 'disgust')
        
        result4 = emotion_predictor('I am so sad about this')
        self.assertEqual(result4['dominant_emotion'], 'sadness')
        
        result5 = emotion_predictor('I am really afraid that this will happen')
        self.assertEqual(result5['dominant_emotion'], 'fear')

unittest.main()