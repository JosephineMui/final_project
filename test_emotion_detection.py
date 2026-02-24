import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test with a sample input
        expected_emotion1 = "joy"
        detected_emotion1 = emotion_detector("I am glad this happened")
        self.assertEqual(detected_emotion1["dominant_emotion"], expected_emotion1)

        expected_emotion2 = "anger"
        detected_emotion2 = emotion_detector("I am really mad about this")
        self.assertEqual(detected_emotion2["dominant_emotion"], expected_emotion2)

        expected_emotion3 = "disgust"
        detected_emotion3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(detected_emotion3["dominant_emotion"], expected_emotion3)

        expected_emotion4 = "sadness"
        detected_emotion4 = emotion_detector("I am so sad about this")
        self.assertEqual(detected_emotion4["dominant_emotion"], expected_emotion4)

        expected_emotion5 = "fear"
        detected_emotion5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(detected_emotion5["dominant_emotion"], expected_emotion5)

if __name__ == '__main__':
    unittest.main()