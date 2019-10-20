import unittest
import app
class SimpleTest(unittest.TestCase):
    # Returns True or False.
def get_connection():
    """Helper method to get redis connection configured by settings"""
    import redis
    import fakeredis
    from .settings import diffs_settings

    if not diffs_settings['test_mode']:
        return redis.Redis(**diffs_settings['redis'])
    else:
        return fakeredis.FakeRedis() 

    def test(self):
        visits = app.hello()

        self.assertTrue(visits, 1)

if __name__ == '__main__':
    unittest.main()

