from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

class FlightTestCase(APITestCase):
    

    def setUp(self):
        self.factory=APIRequestFactory()

    def test_flight_list_as_guest_user(self):
        request=self.factory.get('/flight/flights')





# # Install the package in your Django project:
# pip install coverage
# # Run the tool inside the project folder:
# coverage run --omit='*/env/*' manage.py test
# # After the first pass you can get a coverage report with:
# coverage report
# # You can also generate an HTML report with (a new folder called htmlcov will
# appear inside the project root):
# coverage html