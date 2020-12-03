from django.test import TestCase



from web.models import Autor

class RecetaModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Autor.objects.create(pnombre='Mazapan', papellido='Hernandez')

    def test_autor_lenght(self):
        autor=Autor.objects.get(id=1)
        max_lenght = autor._meta.get_field('pnombre').max_length
        self.assertEquals(max_lenght,100)   

    def test_apellido_label(self):
        autor=Autor.objects.get(id=1)
        field_label = autor._meta.get_field('papellido').verbose_name
        self.assertEquals(field_label,'Apellido')


    def test_get_absolute_url(self):
        autor=Autor.objects.get(id=1)
        self.assertEquals(autor.get_absolute_url(),'/web/autor/1')

    
                 