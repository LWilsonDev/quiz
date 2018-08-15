import unittest
import os, random
from questions import questions
from app import *



class TestQuestions(unittest.TestCase):
    '''
    Test that when game starts, question 1 is shown
    '''
    def test_first_question(self):
        self.assertEquals(session['current_question'], 1)
    
    

#http://flask.pocoo.org/docs/0.12/testing/#accessing-and-modifying-sessions
#with app.test_client() as c:
#    with c.session_transaction() as sess:
#        sess['app.secret_key'] = os.urandom(24)
#        #http://flask.pocoo.org/docs/0.12/testing/#accessing-and-modifying-sessions
        
        

if __name__ == '__main__':
    unittest.main()