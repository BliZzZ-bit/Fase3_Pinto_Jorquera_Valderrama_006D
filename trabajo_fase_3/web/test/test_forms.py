from django.test import TestCase
from web.forms import AutorForm
from web.models import Autor

class AutorFormTest(TestCase):
    def test_valid_form(self):
        autor = Autor.objects.create(pnombre='Armando', papellido='Mocha')
        data = {'pnombre':autor.pnombre, 'papellido':autor.papellido,}
        form = AutorForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        autor = Autor.objects.create(pnombre='', papellido='Cebolla')
        data = {'pnombre':autor.pnombre, 'papellido':autor.papellido,}
        form = AutorForm(data=data)
        self.assertFalse(form.is_valid())


        