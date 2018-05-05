import os
import flaskMemo
import unittest
import tempfile

class FlaskMemoTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskMemo.app.config['DATABASE'] = tempfile.mkstemp()
        flaskMemo.app.testing = True
        self.app = flaskMemo.app.test_client()
        with flaskMemo.app.app_context():
            flaskMemo.flaskMemo.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskMemo.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/empty')
        assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()