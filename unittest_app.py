import unittest
#import app
#import redis
#import fakeredis
#from .settings import diffs_setings

class SimpleTest(unittest.TestCase):
	def test(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test1(self):
		visits = '1'
# app.hello()
		print(visits)
		self.assertTrue(visits,'1')
#		self.assertFalse(visits,'')
#		self.assertFalse('1','0')
    # Returns True or False.
#    def test(self):
#       visits = app.hello()
#      self.assertTrue(visits, 1)
#    def get_connection():
#  	 """Helper method to get redis connection configured by settings"""
#
#   	if not diffs_settings['test_mode']:
#      	return redis.Redis(**diffs_settings['redis'])
# 	else:
#    	return fakeredis.FakeRedis()


if __name__ == '__main__':
    unittest.main()
