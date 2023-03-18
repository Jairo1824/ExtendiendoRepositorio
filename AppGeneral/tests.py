from django.test import TestCase
from AppGeneral.models import Persona

# Create your tests here.
class URLTest(TestCase):
    def test_inicio(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)


class TestModels(TestCase):
    def setUp(self) :
        self.persona=Persona.objects.create(
            nombre="soy un nombre",
            apellido="soy una persona",
            fecha_nacimiento="1933-02-09",
            email="soyemail@email.com",
        )

    def test_modulo(self):
        self.assertEqual(self.persona.nombre,"soy un nombre")

    def setUp(self) :
        self.persona=Persona.objects.create(
            nombre="soy un nombre",
            apellido="soy una persona",
            fecha_nacimiento="1933-02-09",
            email="soyemailemail.com",
        )

    def test_modulo(self):
        self.assertFalse((self.persona.email))