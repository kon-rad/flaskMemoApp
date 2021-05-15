import os
from flaskMemo import create_app, db
import unittest
import tempfile


class FlaskMemoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.memo = {'title': 'Go on vacation'}

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()


    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
#
#    def test_empty_db(self):
#        rv = self.app.get('/empty')
#        assert b'No entries here so far' in rv.data
        
    def test_app_exists(self):
        self.assertFalse(flaskMemo.app is None)

#    def test_app_is_testing(self):
#        self.assertTrue(app.config['TESTING'])
#
#    def test_memo_creation(self):
#        """Test API can create a memo (POST request)"""
#        res = self.app.post('/memos', data=self.memo)
#        self.assertEqual(res.status_code, 201)
#        self.assertIn('App idea', str(res.data))
#
#    def test_api_can_get_all_memos(self):
#        """Test API can get a memo (GET request)."""
#        res = self.app.post('/memos/', data=self.memo)
#        self.assertEqual(res.status_code, 201)
#        res = self.app.get('/memos/')
#        self.assertEqual(res.status_code, 200)
#        self.assertIn('App idea', str(res.data))

    # def test_api_can_get_memo_by_id(self):
    #     """Test API can get a single memo by using it's id."""
    #     rv = self.app.post('/memos/', data=self.memo)
    #     self.assertEqual(rv.status_code, 201)
    #     result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
    #     result = self.app.get(
    #         '/memos/{}'.format(result_in_json['id']))
    #     self.assertEqual(result.status_code, 200)
    #     self.assertIn('App idea', str(result.data))

    # def test_memo_can_be_edited(self):
    #     """Test API can edit an existing memo. (PUT request)"""
    #     rv = self.app.post(
    #         '/memos/',
    #         data={'title': 'foo bar baz'})
    #     self.assertEqual(rv.status_code, 201)
    #     rv = self.app.put(
    #         '/memos/1',
    #         data={
    #             "title": "foo foo bar bar baz baz"
    #         })
    #     self.assertEqual(rv.status_code, 200)
    #     results = self.app.get('/memos/1')
    #     self.assertIn('foo foo bar bar', str(results.data))

    # def test_memo_deletion(self):
    #     """Test API can delete an existing memo. (DELETE request)."""
    #     rv = self.app.post(
    #         '/memos/',
    #         data={'title': 'foo bar baz'})
    #     self.assertEqual(rv.status_code, 201)
    #     res = self.app.delete('/memos/1')
    #     self.assertEqual(res.status_code, 200)
    #     # Test to see if it exists, should return a 404
    #     result = self.app.get('/memos/1')
    #     self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()