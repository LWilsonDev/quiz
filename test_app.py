import unittest
import os, random
from questions import questions
from app import *


# Possible features to test:

# Question matches answer
# If answer is correct, count goes up
# If incorrect, guess count goes up 
# If incorrect again, message shows, count doesnt go up, no more answers can be submitted
# current question count can't be more than len(questions)
# incorrect answers don't increase the correct answer count
# low score  = true if score < len(questions)/2, false if >= len(questions)/2


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