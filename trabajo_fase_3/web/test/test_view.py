from django.test import TestCase
from django.urls import reverse

from web.models import Autor

class AutorListViewTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        num_autores = 6

        for autor_id in range(num_autores):
            Autor.objects.create(
                pnombre=f'Juan{autor_id}',
                papellido=f'Repollo{autor_id}',
            ) 

    def test_view_urls_exists_at_desired_location(self):
        response = self.client.get('/web/autor/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_accesible_by_name(self):
        response = self.client.get(reverse('autor'))
        self.assertEqual(response.status_code, 200)

