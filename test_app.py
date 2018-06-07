import unittest
from app import *

class QuizTests(unittest.TestCase):
    def test_ask_question(self):
        self.assertEqual(ask_question(0), "What is 2 + 2?")
    
    
        
      
      
if __name__ == "__main__": 
      unittest.main()        