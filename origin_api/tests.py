import uuid
from rest_framework.test import APITestCase

URL = "http://127.0.0.1:8000/address"

DATA = {
    "address": "3582, 13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
    "output_format": "json",
}


class AddressTests(APITestCase):
    def test_with_missing_line1_field(self):
        data = {"output_formate": "json"}
        response = self.client.post(URL, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("address", response.data)

    def test_with_missing_output_format_field(self):
        data = {
            "address": "3582, 13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008"
        }
        response = self.client.post(URL, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("output_format", response.data)

    def test_with_json_output_format(self):
        data = DATA
        data["output_format"] = "json"
        response = self.client.post(URL, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("address", response.data)
        self.assertIn("coordinates", response.data)

    def test_with_xml_output_format(self):
        data = DATA
        data["output_format"] = "xml"
        response = self.client.post(URL, data)
        self.assertEqual(response.status_code, 200)

    def test_with_incorrect_output_format_field(self):
        data = DATA
        data["output_format"] = str(uuid.uuid4())
        response = self.client.post(URL, data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("output_format", response.data)
