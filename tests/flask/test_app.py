import unittest
import src.flask.app as flask_app

class TestFinaceApp(unittest.TestCase):
    def setUp(self) -> None:
        flask_app.app.config['TESTING'] = True
        flask_app.app.config['DEBUG'] = False
        self.app = flask_app.app.test_client()

    def test_ping(self):
        response = self.app.get("/ping").data.decode()
        print(response)
        self.assertTrue(response == 'pong')
