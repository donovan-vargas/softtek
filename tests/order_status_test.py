import json
import unittest
import sys
import os
from softtek import app

app.testing = True


class TestApi(unittest.TestCase):

    def test_main(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sys.path.append(os.getcwd())
            f = open('tests/data/order_status_data.json', )
            data = json.load(f)
            result = client.post(
                '/orders_status/',
                json=data
            )
            f.close()
            self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
