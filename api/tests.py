from django.urls import reverse
from django.test import TestCase
from rest_framework import status


class AccountTests(TestCase):
    def test_get_data_from_api(self):
        response = self.client.get('/api/appointments')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["den@gmail.com"],
                         [{"end_time": "2017-02-02T12:00:00", "id": 8, "start_time": "2017-02-02T12:00:00"}])
