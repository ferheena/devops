import unittest
import app
class SimpleTest(unittest.TestCase): 
    # Returns True or False.  
    def test(self):
        visits = app.hello()

        self.assertTrue(visits, 1) 

if __name__ == '__main__': 
    unittest.main() 
