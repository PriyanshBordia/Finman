from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from .serializers import *


class EarningAPITests(APITestCase):
    def setUp(self):
        # Create some earnings for testing
        self.earning1 = Earning.objects.create(title="Earning One", author="Author One", published_date="2023-01-01")
        self.earning2 = Earning.objects.create(title="Earning Two", author="Author Two", published_date="2023-02-01")

    def test_get_earnings(self):
        url = reverse('earning-list')  # Assuming you're using a router with the basename 'earning'
        response = self.client.get(url)
        
        earnings = Earning.objects.all()
        serializer = EarningSerializer(earnings, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_earning(self):
        url = reverse('earning-detail', kwargs={'pk': self.earning1.pk})
        response = self.client.get(url)
        
        earning = Earning.objects.get(pk=self.earning1.pk)
        serializer = EarningSerializer(earning)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_earning(self):
        url = reverse('earning-list')
        data = {'title': 'Earning Three', 'author': 'Author Three', 'published_date': '2023-03-01'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Earning.objects.count(), 3)
        self.assertEqual(Earning.objects.get(pk=3).title, 'Earning Three')

    def test_update_earning(self):
        url = reverse('earning-detail', kwargs={'pk': self.earning1.pk})
        data = {'title': 'Updated Earning One', 'author': 'Updated Author One', 'published_date': '2023-01-01'}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.earning1.refresh_from_db()
        self.assertEqual(self.earning1.title, 'Updated Earning One')

    def test_delete_earning(self):
        url = reverse('earning-detail', kwargs={'pk': self.earning1.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Earning.objects.count(), 1)